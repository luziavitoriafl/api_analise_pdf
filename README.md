
# API de Análise e Continuação de Texto em PDF

Este projeto é uma API REST desenvolvida com FastAPI que permite o upload de arquivos PDF, extrai o texto deles usando a biblioteca `docling` e gera uma continuação do texto com um modelo de linguagem baseado em GPT-2 treinado em português.

---

## Funcionalidades

- Upload de arquivo PDF.
- Extração de texto em formato Markdown a partir do PDF.
- Geração de continuação textual do conteúdo extraído.
- Logs de eventos para monitoramento e depuração.

---

## Como rodar o projeto

### Pré-requisitos

- Python 3.11+
- Git
- Ambiente virtual recomendado (venv ou conda)

### Passos

1. Clone o repositório:
   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   cd api_analise_pdf

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute a API:

   ```bash
   uvicorn app.main:app --reload
   ```

5. Acesse a documentação interativa no navegador:

   ```
   http://127.0.0.1:8000/docs
   ```

---

## Endpoints

* **POST** `/upload-pdf`:
  Recebe um arquivo PDF, extrai o texto e retorna a continuação gerada.

  Exemplo de resposta:

  ```json
  {
    "message": "Arquivo recebido com sucesso",
    "texto_extraido": "Texto extraído do PDF em markdown...",
    "continuacao": "Texto gerado com continuação coerente..."
  }
  ```

---

## Estrutura do projeto

```
api_analise_pdf/
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── core/
│   │   └── logger.py
│   ├── services/
│   │   ├── docling_service.py
│   │   └── summarizer_service.py
│   ├── models/
│   │   └── gpt2-small-portuguese/ (modelo treinado)
│   ├── api/
│   │   └── schemas.py
│   └── main.py
├── arquivos/              # PDFs enviados
├── arquivos_gerados/      # Textos gerados
├── logs/                  # Logs da API
├── requirements.txt
└── README.md
```

---

## Tecnologias usadas

* [FastAPI](https://fastapi.tiangolo.com/)
* [Transformers (Hugging Face)](https://huggingface.co/docs/transformers/index)
* [Docling](https://github.com/wntrblm/docling)
* Python 3.11

---

## Logs

A API gera logs em `logs/api.log` para registrar eventos, avisos e erros, facilitando o monitoramento e depuração.

---

## Contato

Em caso de dúvidas ou sugestões, abra uma issue ou entre em contato.

---

Obrigado por usar a API!

```
