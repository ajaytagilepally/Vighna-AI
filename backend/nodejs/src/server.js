const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors');
const dotenv = require('dotenv');
const morgan = require('morgan');
const axios = require('axios');

dotenv.config();

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: process.env.CORS_ORIGINS || "*",
    methods: ["GET", "POST"]
  }
});

const PORT = process.env.PORT || 3000;
const OLLAMA_HOST = process.env.OLLAMA_HOST || 'http://localhost:11434';
const OLLAMA_MODEL = process.env.OLLAMA_MODEL || 'mistral';

// Middleware
app.use(cors());
app.use(morgan('combined'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Health check
app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    service: 'Vighna AI Node.js Backend',
    ollama_host: OLLAMA_HOST,
    ollama_model: OLLAMA_MODEL
  });
});

// Root endpoint
app.get('/', (req, res) => {
  res.json({
    message: 'Vighna AI Node.js Backend',
    websocket: '/socket.io',
    health: '/health'
  });
});

// WebSocket connection
io.on('connection', (socket) => {
  console.log('New client connected:', socket.id);

  // Chat message event
  socket.on('chat', async (data) => {
    try {
      const { message, model } = data;
      const selectedModel = model || OLLAMA_MODEL;
      
      console.log(`Chat message: ${message}`);
      
      // Stream response from Ollama
      const response = await axios.post(
        `${OLLAMA_HOST}/api/generate`,
        {
          model: selectedModel,
          prompt: message,
          stream: true
        },
        { responseType: 'stream' }
      );

      let fullResponse = '';
      
      response.data.on('data', (chunk) => {
        try {
          const lines = chunk.toString().split('\n');
          for (const line of lines) {
            if (line) {
              const data = JSON.parse(line);
              const text = data.response || '';
              fullResponse += text;
              
              // Emit chunk to client
              socket.emit('chat-chunk', { chunk: text });
            }
          }
        } catch (e) {
          console.error('Error parsing response:', e);
        }
      });

      response.data.on('end', () => {
        socket.emit('chat-complete', { message: fullResponse });
      });

      response.data.on('error', (error) => {
        console.error('Stream error:', error);
        socket.emit('error', { message: 'Error processing request' });
      });
    } catch (error) {
      console.error('Chat error:', error.message);
      socket.emit('error', { message: error.message });
    }
  });

  // Code generation event
  socket.on('generate-code', async (data) => {
    try {
      const { prompt, language } = data;
      const codePrompt = `Generate ${language} code for: ${prompt}\n\nCode:`;
      
      console.log(`Code generation: ${prompt}`);
      
      // Get code from Ollama
      const response = await axios.post(
        `${OLLAMA_HOST}/api/generate`,
        {
          model: 'codellama',
          prompt: codePrompt,
          stream: false
        }
      );

      const code = response.data.response;
      socket.emit('code-generated', { code, language });
    } catch (error) {
      console.error('Code generation error:', error.message);
      socket.emit('error', { message: error.message });
    }
  });

  socket.on('disconnect', () => {
    console.log('Client disconnected:', socket.id);
  });
});

// Error handling
server.on('error', (error) => {
  console.error('Server error:', error);
});

// Start server
server.listen(PORT, () => {
  console.log(`\n🚀 Vighna AI Node.js Backend running on http://localhost:${PORT}`);
  console.log(`📡 WebSocket: ws://localhost:${PORT}/socket.io`);
  console.log(`🤖 Ollama Host: ${OLLAMA_HOST}`);
  console.log(`🧠 Model: ${OLLAMA_MODEL}\n`);
});

module.exports = server;
