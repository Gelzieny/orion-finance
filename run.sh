# Salve como start.ps1
cd "C:\caminho\para\app\api-ollama-permissoes"

# Ativar o ambiente virtual
.\.venv\Scripts\Activate.ps1

# Rodar a aplicação
uvicorn manage:app --host 0.0.0.0 --port 8080 --log-level debug --reload

# Desativar o ambiente virtual
deactivate
