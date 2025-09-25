from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.utils.config import settings
from src.controller.users_controller import users_controller


app = FastAPI(
  title="Orion Finance API",
  description=(
    "Uma API robusta para gestão financeira pessoal. "
    "Permite que os usuários controlem despesas e receitas, "
    "gerenciem múltiplas contas bancárias, "
    "acompanhem investimentos, definam metas financeiras "
    "e organizem listas de compras e itens para casa. "
    "Construída com base em uma arquitetura de dados detalhada "
    "para uma visão completa e holística de suas finanças."
  ),
  version= settings.VERSION,
)

app.include_router(users_controller) 

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
  return RedirectResponse(url="/docs")

@app.get("/monitor", tags=["Health"])
async def statusaplicacao():
  return True

