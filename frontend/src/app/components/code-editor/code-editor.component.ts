import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-code-editor',
  templateUrl: './code-editor.component.html',
  styleUrls: ['./code-editor.component.css']
})
export class CodeEditorComponent implements OnInit {
  prompt = '';
  generatedCode = '';
  explanation = '';
  selectedLanguage = 'python';
  isLoading = false;
  codeLanguages = ['python', 'javascript', 'typescript', 'java', 'cpp', 'go', 'rust', 'csharp'];
  apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  ngOnInit() {}

  generateCode() {
    if (!this.prompt.trim()) return;

    this.isLoading = true;
    this.generatedCode = '';
    this.explanation = '';

    this.http.post<any>(`${this.apiUrl}/api/code/generate`, {
      prompt: this.prompt,
      language: this.selectedLanguage,
      temperature: 0.2
    }).subscribe(
      (response) => {
        this.generatedCode = response.code;
        this.explanation = response.explanation;
        this.isLoading = false;
      },
      (error) => {
        console.error('Error:', error);
        this.explanation = 'Error: ' + (error.error?.detail || 'Failed to generate code');
        this.isLoading = false;
      }
    );
  }

  analyzeCode() {
    if (!this.generatedCode.trim()) return;

    this.isLoading = true;
    this.explanation = '';

    this.http.post<any>(`${this.apiUrl}/api/code/analyze`, {
      code: this.generatedCode,
      language: this.selectedLanguage
    }).subscribe(
      (response) => {
        this.explanation = response.analysis;
        this.isLoading = false;
      },
      (error) => {
        console.error('Error:', error);
        this.explanation = 'Error: ' + (error.error?.detail || 'Failed to analyze code');
        this.isLoading = false;
      }
    );
  }

  copyCode() {
    if (this.generatedCode) {
      navigator.clipboard.writeText(this.generatedCode);
      alert('Code copied to clipboard!');
    }
  }

  clearCode() {
    this.generatedCode = '';
    this.explanation = '';
    this.prompt = '';
  }
}
