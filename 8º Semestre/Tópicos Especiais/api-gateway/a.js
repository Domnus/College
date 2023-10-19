// Código para a aplicação A (porta 3000)
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.json({ mensagem: 'Esta é a aplicação A' });
});

app.listen(port, () => {
  console.log(`Aplicação A rodando em http://localhost:${port}`);
});
