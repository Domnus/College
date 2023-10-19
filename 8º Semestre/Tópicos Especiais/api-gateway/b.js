// Código para a aplicação B (porta 3001)
const express = require('express');
const app = express();
const port = 3001;

app.get('/', (req, res) => {
  res.json({ mensagem: 'Esta é a aplicação B' });
});

app.listen(port, () => {
  console.log(`Aplicação B rodando em http://localhost:${port}`);
});
