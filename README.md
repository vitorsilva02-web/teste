# AutoMind AI

Protótipo inicial de uma plataforma web para organizar sintomas e códigos de falha automotivos.

## Estrutura

- `app.py`: API com FastAPI.
- `static/index.html`: interface web.
- `requirements.txt`: dependências Python.

## Executar localmente

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Acesse `http://127.0.0.1:8000`.

## Endpoints

- `GET /`: interface.
- `GET /health`: estado da aplicação.
- `POST /diagnostico`: recebe veículo, sintomas e códigos de falha.

## Estado atual

A versão 0.1.0 faz uma triagem simples baseada em palavras-chave. Ainda não utiliza um modelo de IA, não se conecta à porta OBD2 e não controla módulos do veículo. A integração com IA será implementada em etapa posterior.
