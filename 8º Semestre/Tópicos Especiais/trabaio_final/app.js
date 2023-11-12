document.addEventListener('DOMContentLoaded', () => {
    const map = L.map('map').setView([0, 0], 2); // Defina o centro do mapa conforme necessário
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
  
    // Mova a função para fora do bloco de inicialização
    async function consultarLocalizacao() {
      const dispositivoId = document.getElementById('dispositivoId').value.trim();
      
      if (dispositivoId) {
        try {
          const response = await fetch(`http://localhost:3001/ultima-localizacao/${dispositivoId}`, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
            },
          });
  
          const data = await response.json();
          console.log('Resposta da consulta:', data);
  
          if (response.status !== 200) {
            alert('Erro ao consultar a localização do dispositivo.');
            console.error(data.message);
          } else {
            const { latitude, longitude } = data; // Assumindo que o objeto retornado possui propriedades latitude e longitude
            // Agora, você pode usar a latitude e a longitude para marcar no mapa, dependendo da biblioteca de mapa que está usando.
            L.marker([latitude, longitude]).addTo(map);
          }
        } catch (error) {
          console.error('Erro na consulta de localização:', error);
          alert('Erro ao consultar a localização do dispositivo.');
        }
      } else {
        alert('Por favor, insira o ID do dispositivo.');
      }
    }
  
    // Adicione o evento de clique ao botão
    document.getElementById('consultarBtn').addEventListener('click', consultarLocalizacao);
  });
  