import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
}

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {
  messages: Message[] = [];
  inputMessage = '';
  isLoading = false;
  apiUrl = 'http://localhost:8000';
  models: string[] = [];
  selectedModel = 'mistral';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.loadModels();
    this.addSystemMessage('Welcome to Vighna AI! Powered by Ollama. Type a message to start chatting.');
  }

  loadModels() {
    this.http.get<any>(`${this.apiUrl}/api/chat/models`).subscribe(
      (response) => {
        this.models = response.models || ['mistral', 'llama2'];
      },
      (error) => {
        console.error('Error loading models:', error);
        this.models = ['mistral', 'llama2', 'codellama'];
      }
    );
  }

  sendMessage() {
    if (!this.inputMessage.trim()) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: this.inputMessage,
      timestamp: new Date()
    };

    this.messages.push(userMessage);
    const prompt = this.inputMessage;
    this.inputMessage = '';
    this.isLoading = true;

    this.http.post<any>(`${this.apiUrl}/api/chat/send`, {
      message: prompt,
      model: this.selectedModel,
      temperature: 0.7
    }).subscribe(
      (response) => {
        const assistantMessage: Message = {
          id: Date.now().toString(),
          role: 'assistant',
          content: response.response,
          timestamp: new Date()
        };
        this.messages.push(assistantMessage);
        this.isLoading = false;
        this.scrollToBottom();
      },
      (error) => {
        console.error('Error:', error);
        this.addSystemMessage('Error: ' + (error.error?.detail || 'Failed to get response'));
        this.isLoading = false;
      }
    );
  }

  addSystemMessage(content: string) {
    this.messages.push({
      id: Date.now().toString(),
      role: 'assistant',
      content: content,
      timestamp: new Date()
    });
  }

  scrollToBottom() {
    setTimeout(() => {
      const container = document.querySelector('.messages-container');
      if (container) {
        container.scrollTop = container.scrollHeight;
      }
    }, 100);
  }

  clearChat() {
    this.messages = [];
    this.addSystemMessage('Chat cleared. Start a new conversation!');
  }
}
