🧠 Projeto: Testes de Acessibilidade com IA

Este projeto realiza análise automatizada de acessibilidade em vídeos com transcrição por voz (voice-over), visão computacional e geração de relatórios em PDF e Markdown, utilizando:
	•	🎯 FastAPI (backend)
	•	⚛️ React com Vite (frontend)
	•	🤖 OpenAI GPT-4o, Whisper, YOLOv8
	•	📦 Deploy completo com Railway

⸻

📁 Estrutura do Projeto

acessibilidade-com-ia/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── railway.json
│   └── app/
│       ├── integracao/
│       ├── transcricao/
│       ├── visao/
│       └── relatorio/
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   ├── railway.json
│   ├── index.html
│   └── src/
│       ├── main.jsx
│       ├── style.css
│       └── components/App.jsx


⸻

⚙️ Como Rodar Localmente

🔹 Backend (FastAPI)

cd backend
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
uvicorn main:app --reload

	•	Acesse: http://localhost:8000/docs

⸻

🔹 Frontend (React + Vite)

cd frontend
npm install
npm run dev

	•	Acesse: http://localhost:5173

🔁 Lembre de atualizar o endpoint do backend em App.jsx se estiver rodando localmente.

⸻

☁️ Como Fazer Deploy na Railway

🔸 1. Criar Conta
	•	https://railway.app
	•	Conecte com seu GitHub

⸻

🔸 2. Deploy do Backend
	1.	Clique em “New Project” > “Deploy from GitHub”
	2.	Escolha o repositório e a pasta backend/
	3.	Railway detectará o railway.json:

{
  "build": "pip install -r requirements.txt",
  "start": "uvicorn main:app --host 0.0.0.0 --port $PORT"
}

	4.	Após o deploy:
	•	Vá em “Variables”
	•	Adicione sua chave da OpenAI:

OPENAI_API_KEY = sk-xxxx...



⸻

🔸 3. Deploy do Frontend
	1.	Crie novo projeto no Railway (ou use monorepo com configuração personalizada)
	2.	Escolha a pasta frontend/
	3.	Railway detectará o railway.json:

{
  "build": "npm install && npm run build",
  "start": "npx serve -s dist"
}

	4.	Após deploy, copie o domínio do frontend

⸻

📄 Funcionalidades
	•	🎤 Transcrição automática com Whisper
	•	👀 Análise de campos visuais com YOLOv8 + OpenCV
	•	🧠 Análise de acessibilidade com GPT-4o
	•	📑 Geração automática de PDF e Markdown
	•	🎛 Interface React com upload e visualização

⸻

👨‍💻 Autor

Projeto iniciado por [Luiz Assumpção] com suporte de IA.

