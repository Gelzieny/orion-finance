@echo off
set VENV_DIR=venv
set REQUIREMENTS=requirements.txt

REM Verifica se a venv existe
if not exist %VENV_DIR%\ (
    echo Criando venv em %VENV_DIR% ...
    python -m venv %VENV_DIR%
)

REM Ativa a venv
call %VENV_DIR%\Scripts\activate.bat

REM Instala dependencias (se existir requirements.txt)
if exist %REQUIREMENTS% (
    echo Instalando dependencias do %REQUIREMENTS% ...
    python -m pip install --upgrade pip
    pip install -r %REQUIREMENTS%
) else (
    echo Nenhum arquivo %REQUIREMENTS% encontrado. Pulando instalacao.
)

REM Desativa e sai
deactivate
echo Ambiente virtual configurado com sucesso!
exit /b
