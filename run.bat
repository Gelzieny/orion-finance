@echo off

:: Ativar o ambiente virtual
call .\venv\Scripts\activate.bat


REM Mostrar URL de acesso
echo ====================================================
echo Aplicacao rodando! Acesse em: http://127.0.0.1:8080
echo ====================================================

:: Rodar a aplicação
uvicorn src.manage:app --host 0.0.0.0 --port 8080 --log-level debug --reload

:: Desativar o ambiente virtual
call deactivate
