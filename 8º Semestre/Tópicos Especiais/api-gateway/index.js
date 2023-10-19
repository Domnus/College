const express = require('express');
const app = express();
const port = 8090;

// Rota para a aplicação A
app.get('/a', (req, res) => {
  res.json({ mensagem: 'Esta é a aplicação A' });
});

// Rota para a aplicação B
app.get('/b', (req, res) => {
  res.json({ mensagem: 'Esta é a aplicação B' });
});

// Redirecionamento com base na rota
app.use((req, res, next) => {
  const rota = req.path.toLowerCase();

  if (rota === '/a') {
    // Redireciona para a aplicação A (porta 3000)
    return res.redirect('http://localhost:3000');
  } else if (rota === '/b') {
    // Redireciona para a aplicação B (porta 3001)
    return res.redirect('http://localhost:3001');
  }

  // Rota não correspondente
  res.status(404).json({ mensagem: 'Rota não encontrada' });
});

app.listen(port, () => {
  console.log(`API Gateway rodando em http://localhost:${port}`);
});
