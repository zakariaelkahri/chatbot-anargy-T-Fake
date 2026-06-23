# chatbot-anargy-T-Fake

Docker Compose setup for:

- FastAPI backend on `http://localhost:8000`
- React frontend on `http://localhost:3000`
- Ollama LLM service on `http://localhost:11434`

The LLM container pulls the `mistral-nemo` model at startup and stores it in the
`ollama-data` Docker volume.

## Run

```bash
docker compose up --build
```

Open the frontend:

```text
http://localhost:3000
```

Backend health check:

```text
http://localhost:8000/health
```

## Services

```text
backend/
  Dockerfile
  requirements.txt
  app/main.py

frontend/
  Dockerfile
  package.json
  src/

llm/
  Dockerfile
  requirements.txt
  start-ollama.sh
```
