"""
Gemini API Integration
=======================

Este script fornece um modelo para a integração com a API do Gemini usando Python.

Requisitos:
-----------
- Python 3.7+
- Biblioteca requests (caso use requisições HTTP diretas)
- Biblioteca google-generativeai (caso use a SDK oficial)

Instalação das dependências:
----------------------------
sh
pip install requests google-generativeai


Configuração:
-------------
Substitua YOUR_API_KEY pela sua chave da API Gemini.

Uso:
----
1. Inicialize a classe GeminiAPI com sua chave de API.
2. Use send_prompt(prompt) para enviar um prompt para a API e obter uma resposta.

Documentação da API:
--------------------
Acesse a documentação oficial para mais detalhes:
https://ai.google.dev/docs
"""

import requests
import google.generativeai as genai

class GeminiAPI:
    """
    Classe para integração com a API do Gemini.
    """
    
    def _init_(self, api_key: str):
        """
        Inicializa a API com a chave de autenticação.

        Args:
            api_key (str): Chave da API Gemini.
        """
        self.api_key = api_key
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")
    
    def send_prompt(self, prompt: str) -> str:
        """
        Envia um prompt para a API e retorna a resposta.

        Args:
            prompt (str): Texto a ser enviado para a API.

        Returns:
            str: Resposta gerada pelo modelo.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Erro na requisição: {str(e)}"

# Exemplo de uso
gemini = GeminiAPI("YOUR_API_KEY")
prompt = "Explique a teoria da relatividade de forma simples."
response = gemini.send_prompt(prompt)
print(response)