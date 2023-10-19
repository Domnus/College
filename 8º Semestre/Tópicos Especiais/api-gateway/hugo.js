const express = require('express');
const app = express();
const httpProxy = require('http-proxy');

const apiAUrl = 'http://localhost:3000';
const apiBUrl = 'http://localhost:3001';

const proxyA = httpProxy.createProxyServer({ target: apiAUrl });
const proxyB = httpProxy.createProxyServer({ target: apiBUrl });

app.all('/8090/a/*', (req, res) => {
    proxyA.web(req, res);
});

app.all('/8090/b/*', (req, res) => {
    proxyB.web(req, res);
});

const PORT = 8090;
app.listen(PORT, () => {
    console.log(`API Gateway rodando na porta ${PORT}`);
});