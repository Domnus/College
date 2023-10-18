const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const sqlite3 = require('sqlite3').verbose();

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

const PORT = process.env.PORT || 3000;

// Configurar o banco de dados SQLite
const db = new sqlite3.Database(':memory:'); // Use ':memory:' para um banco de dados temporário em memória

// Criar tabela de dispositivos
db.serialize(() => {
  db.run('CREATE TABLE devices (id TEXT PRIMARY KEY, name TEXT, code TEXT, brand TEXT)');
});

// Middleware para análise de corpo JSON
app.use(express.json());

// Rota para obter todos os dispositivos
app.get('/devices', (req, res) => {
  db.all('SELECT * FROM devices', (err, rows) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json(rows);
  });
});

// Rota para obter um dispositivo por ID
app.get('/devices/:id', (req, res) => {
  const { id } = req.params;
  db.get('SELECT * FROM devices WHERE id = ?', [id], (err, row) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    if (!row) {
      return res.status(404).json({ error: 'Device not found' });
    }
    res.json(row);
  });
});

// Rota para criar um novo dispositivo
app.post('/devices', (req, res) => {
  const { id, name, code, brand } = req.body;
  db.run('INSERT INTO devices VALUES (?, ?, ?, ?)', [id, name, code, brand], (err) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    // Enviar mensagem para clientes WebSocket
    io.emit('device-created', { id, name, code, brand });
    res.json({ message: 'Device created successfully' });
  });
});

// Rota para atualizar um dispositivo
app.put('/devices/:id', (req, res) => {
  const { id } = req.params;
  const { name, code, brand } = req.body;
  db.run('UPDATE devices SET name = ?, code = ?, brand = ? WHERE id = ?', [name, code, brand, id], (err) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    // Enviar mensagem para clientes WebSocket
    io.emit('device-updated', { id, name, code, brand });
    res.json({ message: 'Device updated successfully' });
  });
});

// Rota para excluir um dispositivo
app.delete('/devices/:id', (req, res) => {
  const { id } = req.params;
  db.run('DELETE FROM devices WHERE id = ?', [id], (err) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    // Enviar mensagem para clientes WebSocket
    io.emit('device-deleted', { id });
    res.json({ message: 'Device deleted successfully' });
  });
});

// Iniciar o servidor WebSocket
io.on('connection', (socket) => {
  console.log('Client connected to WebSocket');

  // Evento quando um cliente se desconecta
  socket.on('disconnect', () => {
    console.log('Client disconnected from WebSocket');
  });
});

// Iniciar o servidor HTTP
server.listen(PORT, () => {
  console.log(`Server listening on http://localhost:${PORT}`);
});