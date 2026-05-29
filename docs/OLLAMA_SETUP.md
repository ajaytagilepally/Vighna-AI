# Ollama Setup Guide

## What is Ollama?

Ollama is a tool for running large language models locally on your machine. It's completely free, requires no API keys, and works offline.

## Installation

### Windows

1. Download Ollama from https://ollama.ai/download/windows
2. Run the installer
3. Ollama will install and start automatically
4. You'll see an Ollama icon in the system tray

### macOS

1. Download Ollama from https://ollama.ai/download/mac
2. Open the .dmg file
3. Drag Ollama to Applications folder
4. Launch Ollama from Applications

### Linux

```bash
curl https://ollama.ai/install.sh | sh

# Start Ollama service
sudo systemctl start ollama
sudo systemctl enable ollama
```

## Verify Installation

```bash
# Check Ollama version
ollama --version

# Test connection
curl http://localhost:11434
# Should return: Ollama is running
```

## Available Models

### Recommended Models for Vighna AI

#### 1. Mistral (5B) - Best for Speed
```bash
ollama pull mistral
```
- **Size**: 5GB
- **Memory**: 4-8GB RAM
- **Speed**: Very Fast ⚡⚡⚡
- **Quality**: Good for code and chat
- **Best for**: Speed-focused applications

#### 2. Llama 2 (7B/13B) - Best for Quality
```bash
ollama pull llama2
```
- **Size**: 7GB (7B) or 13GB (13B)
- **Memory**: 8-16GB RAM
- **Speed**: Medium ⚡⚡
- **Quality**: Excellent for conversations
- **Best for**: General purpose AI

#### 3. Code Llama (7B/13B) - Best for Code
```bash
ollama pull codellama
```
- **Size**: 7GB (7B) or 13GB (13B)
- **Memory**: 8-16GB RAM
- **Speed**: Medium ⚡⚡
- **Quality**: Excellent for code generation
- **Best for**: Code-focused tasks

#### 4. Phi (3B) - Lightweight
```bash
ollama pull phi
```
- **Size**: 2GB
- **Memory**: 4GB minimum
- **Speed**: Very Fast ⚡⚡⚡
- **Quality**: Good but less capable
- **Best for**: Low-resource machines

#### 5. Neural Chat (7B) - Conversation
```bash
ollama pull neural-chat
```
- **Size**: 7GB
- **Memory**: 8GB RAM
- **Speed**: Medium ⚡⚡
- **Quality**: Good for conversations
- **Best for**: Chat interactions

## Pulling Models

### Pull a Model

```bash
# Pull Mistral (recommended for speed)
ollama pull mistral

# Pull Llama 2
ollama pull llama2

# Pull Code Llama for code generation
ollama pull codellama

# Pull multiple models
ollama pull mistral
ollama pull llama2
ollama pull codellama
```

### List Downloaded Models

```bash
ollama list
```

Output example:
```
NAME            	ID              	SIZE      MODIFIED
mistral:latest  	af00cd4f1a25    	5.4 GB    2 minutes ago
llama2:latest   	73ab2a65f8ce    	7.0 GB    1 hour ago
codellama:latest	3d3c0dd2da26    	7.7 GB    1 hour ago
```

### Delete a Model

```bash
ollama rm mistral
ollama rm llama2
```

## Running Ollama

### Start Ollama Service

**Windows/macOS**: 
- Ollama starts automatically in the background
- You'll see an icon in the system tray
- Click to access the menu

**Linux**:
```bash
# If installed as service
sudo systemctl start ollama

# Or run manually
ollama serve
```

### Verify Ollama is Running

```bash
# Test connection
curl http://localhost:11434

# Should return:
# Ollama is running
```

## Testing Models

### Command Line Test

```bash
# Chat with Mistral
ollama run mistral

# Type a message:
# >>> Hello, what is your name?
# < Model response...

# Type 'exit' to quit
```

### API Test

```bash
# Generate a response
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "mistral",
  "prompt": "Hello, how are you?"
}'

# Stream response
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "mistral",
  "prompt": "Write a Python function to calculate factorial",
  "stream": true
}'
```

## Configuration

### Environment Variables

Edit your `.env` file:

```env
# Use Mistral for speed
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=mistral
OLLAMA_CODE_MODEL=codellama
OLLAMA_TIMEOUT=120
```

### Model Parameters

#### Temperature
- **0.0-0.5**: Deterministic, good for code
- **0.5-0.7**: Balanced
- **0.7-1.0**: Creative, good for conversations

#### Top P
- **0.1-0.5**: Focused
- **0.5-0.9**: Balanced
- **0.9-1.0**: Diverse

## Performance Optimization

### For GPU Acceleration

#### NVIDIA GPUs

1. Install CUDA from https://developer.nvidia.com/cuda-downloads
2. Install cuDNN from https://developer.nvidia.com/cudnn
3. Ollama will automatically detect and use GPU

#### AMD GPUs

1. Install ROCm from https://rocmdocs.amd.com/
2. Restart Ollama
3. Check if GPU is being used

#### Apple Silicon (M1/M2/M3)

- Ollama automatically detects and uses Metal acceleration
- No additional setup needed

### Monitoring GPU Usage

```bash
# NVIDIA
nvidia-smi

# AMD
rocm-smi

# macOS
sudo powermetrics --samplers gpu_power -n 1
```

## Troubleshooting

### Ollama Not Responding

```bash
# Check if it's running
curl http://localhost:11434

# If not running:
# Windows: Restart Ollama from system tray
# macOS: Restart Ollama application
# Linux: sudo systemctl restart ollama
```

### Port Already in Use

```bash
# Find process using port 11434
lsof -i :11434

# Kill the process
kill -9 <PID>

# Or change port in Ollama settings
export OLLAMA_HOST=0.0.0.0:9999
```

### Model Not Found

```bash
# List available models
ollama list

# Pull the model
ollama pull mistral
ollama pull llama2
ollama pull codellama
```

### High Memory Usage

```bash
# Use smaller models
ollama pull phi        # 2GB
ollama pull mistral    # 5GB
ollama pull neural-chat # 7GB

# Unload unused models
ollama rm llama2
```

### Slow Response

1. **Check CPU/GPU**: Is Ollama using GPU?
2. **Use faster model**: Try Mistral instead of Llama
3. **Reduce context**: Limit conversation history
4. **Close other apps**: Free up system resources

### Model Won't Load

```bash
# Check available disk space (need 5-15GB free)
df -h

# Remove unused models
ollama rm llama2

# Try pulling again
ollama pull mistral
```

## Advanced Configuration

### Custom Model Parameters

Create `Modelfile` in your project:

```dockerfile
FROM mistral

# Set model parameters
PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER top_k 40
PARAMETER num_ctx 2048

# Set system prompt
SYSTEM "You are a helpful coding assistant."
```

Build custom model:

```bash
ollama create my-mistral -f ./Modelfile
ollama run my-mistral
```

### Running on Different Port

```bash
# Linux/macOS
export OLLAMA_HOST=0.0.0.0:9999
ollama serve

# Windows (in PowerShell)
$env:OLLAMA_HOST="0.0.0.0:9999"
ollama serve
```

## Integration with Vighna AI

### Python Backend Integration

```python
import requests
import json

# Connect to Ollama
OLLAMA_HOST = "http://localhost:11434"
OLLAMA_MODEL = "mistral"

def chat_with_ollama(prompt):
    response = requests.post(
        f"{OLLAMA_HOST}/api/generate",
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

# Stream response
def chat_stream(prompt):
    response = requests.post(
        f"{OLLAMA_HOST}/api/generate",
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )
    for line in response.iter_lines():
        if line:
            data = json.loads(line)
            yield data["response"]
```

### Node.js Backend Integration

```javascript
const axios = require('axios');

const OLLAMA_HOST = 'http://localhost:11434';
const OLLAMA_MODEL = 'mistral';

async function chatWithOllama(prompt) {
  const response = await axios.post(
    `${OLLAMA_HOST}/api/generate`,
    {
      model: OLLAMA_MODEL,
      prompt: prompt,
      stream: false
    }
  );
  return response.data.response;
}

// Stream response
async function *chatStream(prompt) {
  const response = await axios.post(
    `${OLLAMA_HOST}/api/generate`,
    {
      model: OLLAMA_MODEL,
      prompt: prompt,
      stream: true
    },
    { responseType: 'stream' }
  );
  
  for await (const chunk of response.data) {
    const lines = chunk.toString().split('\n');
    for (const line of lines) {
      if (line) {
        const data = JSON.parse(line);
        yield data.response;
      }
    }
  }
}
```

## Resources

- **Ollama Official**: https://ollama.ai
- **GitHub**: https://github.com/ollama/ollama
- **API Documentation**: https://github.com/ollama/ollama/blob/main/docs/api.md
- **Model Library**: https://ollama.ai/library
- **Discord Community**: https://discord.gg/ollama

## Next Steps

1. ✅ Install Ollama: https://ollama.ai
2. ✅ Pull a model: `ollama pull mistral`
3. ✅ Verify running: `curl http://localhost:11434`
4. ✅ Update `.env` file in Vighna AI
5. ✅ Start Vighna AI services
6. ✅ Visit http://localhost:4200

## Tips for Best Results

1. **Start with Mistral**: Fast and good quality
2. **Use Code Llama for code**: Better at code generation
3. **Enable GPU**: 10-100x faster inference
4. **Monitor system resources**: Watch RAM and CPU usage
5. **Start small**: Pull one model, test, then add more
