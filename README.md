# Vighna AI 🤖

A comprehensive AI application combining **ChatGPT-like conversational intelligence** with **GitHub Copilot-like code generation** capabilities, powered by **Ollama** for completely free, lifetime access to local AI models.

## ✨ Features

- **Conversational AI**: Chat interface powered by local Ollama models (Llama 2, Mistral, etc.)
- **Code Generation**: AI-powered code completion and generation
- **Code Analysis**: Analyze, explain, and refactor code snippets
- **Context Awareness**: Maintain conversation history and multi-turn conversations
- **Real-time Streaming**: Stream responses for better UX
- **Completely Free**: No API keys, no subscriptions, runs locally
- **Code Editor**: Integrated editor with syntax highlighting
- **Conversation History**: Save and manage chat histories
- **Offline Capable**: Works without internet after setup

## 🎯 Why Ollama?

✅ **Completely Free** - No API keys, no subscriptions, no costs
✅ **Lifetime Access** - Run as many times as you want
✅ **Privacy First** - Your data never leaves your computer
✅ **Offline** - Works without internet after initial setup
✅ **Multiple Models** - Llama 2, Mistral, Phi, and more
✅ **Fast** - Runs locally with GPU acceleration support

## 🛠 Tech Stack

### Backend
- **Python**: FastAPI with async support for local model integration
- **Node.js**: Express.js server with WebSocket for real-time features
- **Ollama**: Local AI model runtime (Llama 2, Mistral)
- **SQLite/PostgreSQL**: Lightweight database for conversations
- **Redis**: Optional caching and session management

### Frontend
- **Angular**: 16+ with TypeScript
- **Angular Material**: Professional UI components
- **RxJS**: Reactive programming patterns
- **Monaco Editor**: Advanced code editor
- **Tailwind CSS**: Utility-first CSS framework

## 📋 Prerequisites

### System Requirements
- **RAM**: 8GB minimum (16GB recommended)
- **GPU**: Optional but recommended (NVIDIA/AMD)
- **Disk Space**: 10-20GB for models
- **OS**: Windows, macOS, or Linux

### Software Requirements
- **Node.js**: v18.0.0 or higher
- **Python**: 3.9 or higher
- **Angular CLI**: 16 or higher
- **Docker** (optional): For containerized deployment
- **Ollama**: Download from https://ollama.ai

## 🚀 Quick Start

### Step 1: Install Ollama

1. Download Ollama from https://ollama.ai
2. Install for your operating system
3. Open terminal/command prompt and verify:
   ```bash
   ollama --version
   ```

### Step 2: Pull Ollama Models

```bash
# Pull Llama 2 (recommended for general use)
ollama pull llama2

# Or pull Mistral (faster, more efficient)
ollama pull mistral

# Or pull both
ollama pull llama2
ollama pull mistral
ollama pull neural-chat  # Good for code
```

### Step 3: Start Ollama Server

```bash
# Ollama runs as a background service on port 11434
ollama serve
# Or just ensure Ollama is running in the background
```

### Step 4: Clone and Setup Vighna AI

```bash
# Clone the repository
git clone https://github.com/ajaytagilepally/Vighna-AI.git
cd Vighna-AI

# Copy environment file
cp .env.example .env
# No need to add API keys! Ollama runs locally.
```

### Step 5: Using Docker Compose (Recommended)

```bash
# Start all services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

Access:
- **Frontend**: http://localhost:4200
- **Python API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Node.js API**: http://localhost:3000

### Step 6: Manual Setup (Without Docker)

**Python Backend:**
```bash
cd backend/python
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app/main.py
```

**Node.js Backend:**
```bash
cd backend/nodejs
npm install
npm start
```

**Angular Frontend:**
```bash
cd frontend
npm install
ng serve
```

## 📚 Available Ollama Models

| Model | Size | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| **Mistral** | 5B | ⚡⚡⚡ Fast | Good | Code, Speed |
| **Llama 2** | 7B/13B | ⚡⚡ Medium | Excellent | Chat, General |
| **Neural Chat** | 7B | ⚡⚡ Medium | Good | Conversation |
| **Phi** | 3B | ⚡⚡⚡ Very Fast | Good | Lightweight |
| **Code Llama** | 7B/13B | ⚡⚡ Medium | Excellent | Code Generation |

```bash
# Pull different models
ollama pull llama2
ollama pull mistral
ollama pull neural-chat
ollama pull codellama
ollama pull phi
```

## 🔧 Configuration

### Environment Variables

Edit `.env` file:

```env
# Ollama Configuration (LOCAL - No API key needed!)
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=mistral  # or llama2, neural-chat, codellama
OLLAMA_CODE_MODEL=codellama  # For code generation

# Database (SQLite by default, no setup needed)
DATABASE_URL=sqlite:///./vighna_ai.db

# Backend Services
PYTHON_BACKEND_PORT=8000
NODEJS_BACKEND_PORT=3000
ANGULAR_FRONTEND_PORT=4200

# JWT (Generate a random string)
JWT_SECRET=your_super_secret_jwt_key_change_this
JWT_EXPIRATION=3600

# Application Settings
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=info

# CORS
CORS_ORIGINS=http://localhost:4200,http://localhost:3000
```

## 📖 Usage Examples

### Chat with AI

```bash
# Using Python API
curl -X POST http://localhost:8000/api/chat/sessions \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Chat",
    "type": "conversation"
  }'
```

### Generate Code

```bash
# Ask AI to generate code
curl -X POST http://localhost:8000/api/code/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Create a Python function to calculate factorial",
    "language": "python"
  }'
```

### Analyze Code

```bash
# Get code analysis
curl -X POST http://localhost:8000/api/code/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "code": "function sum(a, b) { return a + b; }",
    "language": "javascript"
  }'
```

## 📁 Project Structure

```
Vighna-AI/
├── backend/
│   ├── python/           # FastAPI backend
│   │   ├── app/
│   │   ├── models/
│   │   ├── services/
│   │   ├── routes/
│   │   └── requirements.txt
│   └── nodejs/           # Express backend with WebSocket
│       ├── src/
│       ├── services/
│       ├── routes/
│       └── package.json
├── frontend/             # Angular frontend
│   ├── src/
│   ├── app/
│   ├── assets/
│   └── angular.json
├── docker-compose.yml    # Docker setup
├── .env.example          # Environment template
├── docs/                 # Documentation
│   ├── API.md
│   ├── SETUP.md
│   ├── OLLAMA_SETUP.md
│   └── ARCHITECTURE.md
└── README.md
```

## 🐛 Troubleshooting

### Ollama Not Connecting

```bash
# Check if Ollama is running
curl http://localhost:11434

# Restart Ollama
ollama serve

# Check Ollama logs
# Windows: View logs in Ollama app
# macOS/Linux: Check background process
```

### Model Not Found

```bash
# List available models
ollama list

# Pull a model
ollama pull llama2
ollama pull mistral
```

### Port Already in Use

```bash
# Find process using port
lsof -i :8000   # Python
lsof -i :3000   # Node.js
lsof -i :4200   # Angular
lsof -i :11434  # Ollama

# Kill process
kill -9 <PID>
```

### High Memory Usage

```bash
# Use smaller models
ollama pull phi         # 3B - Very lightweight
ollama pull mistral     # 5B - Lightweight
ollama pull neural-chat # 7B - Balanced
```

## 📚 Documentation

- **[Setup Guide](./docs/SETUP.md)** - Detailed installation instructions
- **[Ollama Setup](./docs/OLLAMA_SETUP.md)** - Ollama configuration and models
- **[API Documentation](./docs/API.md)** - Complete API reference
- **[Architecture](./docs/ARCHITECTURE.md)** - System design and data flow

## 🚀 Performance Tips

1. **Use GPU**: NVIDIA/AMD GPU speeds up inference 10-100x
2. **Smaller Models**: Use Mistral/Phi for faster responses
3. **Quantization**: Ollama uses quantized models by default (4-bit)
4. **Parallel Requests**: Node.js handles concurrent WebSocket connections
5. **Caching**: Enable Redis for conversation caching

## 💡 Next Steps

1. Install Ollama: https://ollama.ai
2. Pull a model: `ollama pull mistral`
3. Start Ollama: `ollama serve`
4. Clone repo and follow Quick Start
5. Visit http://localhost:4200
6. Start chatting!

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

## 🎉 Features Coming Soon

- [ ] Multi-language support
- [ ] Voice chat interface
- [ ] Model fine-tuning
- [ ] Integration with more local models
- [ ] Advanced code analysis
- [ ] Export conversations
- [ ] Mobile app

## 💬 Support

If you encounter issues:

1. Check [Troubleshooting](#-troubleshooting) section
2. Review [Documentation](./docs/)
3. Open an [Issue](https://github.com/ajaytagilepally/Vighna-AI/issues)
4. Check [Ollama Documentation](https://github.com/ollama/ollama)

---

**Made with ❤️ for the open-source community**
