const express = require('express');
const axios = require('axios');

const app = express();
const port = 3000;

function validateCep(cep) {
    return /^\d{8}$/.test(cep);
}

const viaCepApi = 'https://viacep.com.br/ws/';
const correiosApi = 'https://api.correios.com.br/cep/';

let circuitBreakerOpen = false;
let consecutiveFailures = 0;

// Função para chamar a API do ViaCEP
async function callViaCepApi(cep) {
    try {
        const response = await axios.get(`${viaCepApi}${cep}/json`);
        // Se a API do ViaCEP retornar com sucesso, retornar os dados
        const essentialData = {
            cep: response.data.cep,
            logradouro: response.data.logradouro,
            bairro: response.data.bairro,
            localidade: response.data.localidade,
            uf: response.data.uf,
        };
        return essentialData;
    } catch (error) {
        console.error('ViaCEP API error:', error.message);
        throw error;
    }
}

// Função para chamar a API do Correios
async function callCorreiosApi(cep) {
    try {
        const response = await axios.get(`${correiosApi}${cep}`);
        return response.data;
    } catch (error) {
        console.error('Correios API error:', error.message);
        throw error;
    }
}

app.get('/cep/:cep', async (req, res) => {
    try {
        const { cep } = req.params;

        if (!validateCep(cep)) {
            return res.status(400).json({ error: 'CEP inválido. Deve conter apenas números.' });
        }

        try {
            // Verificar se o circuit breaker está aberto
            if (circuitBreakerOpen) {
                // Se estiver aberto, chamar a API dos Correios como fallback
                const viaCepData = await callViaCepApi(cep);
                res.json(viaCepData);
                return;
            }

            // Tentar chamar a API do ViaCEP
            const viaCepResponse = await callCorreiosApi(cep);

            // Se a chamada for bem-sucedida, resetar o contador de falhas
            consecutiveFailures = 0;

            // Se a API do ViaCEP retornar com sucesso, retornar os dados
            const essentialData = {
                cep: viaCepResponse.cep,
                logradouro: viaCepResponse.logradouro,
                bairro: viaCepResponse.bairro,
                localidade: viaCepResponse.localidade,
                uf: viaCepResponse.uf,
            };
            res.json(essentialData);
        } catch (error) {
            // Tratamento de erros para a API do ViaCEP
            console.error(error);

            // Incrementar o contador de falhas
            consecutiveFailures++;

            // Se atingir um número de falhas consecutivas, abrir o circuit breaker
            if (consecutiveFailures >= 3) {
                circuitBreakerOpen = true;

                // Aguardar um tempo antes de tentar reabrir o circuit breaker
                setTimeout(() => {
                    circuitBreakerOpen = false;
                    consecutiveFailures = 0;
                }, 30000); // Aguardar 30 segundos antes de reabrir o circuit breaker
            }

            // Se ocorrer um erro, chamar a API dos Correios como fallback
            const correiosData = await callViaCepApi(cep);
            res.json(correiosData);
        }
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Erro interno do servidor' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
