from fastapi import APIRouter, Body, HTTPException, Depends

from src.utils.utils import *
from src.models.users_model import Usuario
from src.dependencies.security_hash import *
from src.dependencies.conexao import ConexaoPostgres
from src.repository.users_repository import UsuarioRepository

users_controller = APIRouter()


def get_db_connection():
  return ConexaoPostgres() 
  
def get_user_repository(db: ConexaoPostgres = Depends(get_db_connection)):
  return UsuarioRepository(db)


@users_controller.post(
    "/list-usuario",
    tags=["Usuário"],
    summary="Listar usuários",
    description="""
    Esta rota retorna a lista de todos os usuários cadastrados no sistema.
    
    - **Retorno:** JSON contendo os dados dos usuários.
    - **Exemplo de uso:** `/list-usuario`
    - **Formato do JSON:**
        ```json
        [
            {
                "codigo": 1,
                "nome": "Gelzieny",
                "email": "exemplo@teste.com"
            }
        ]
        ```
    """
)
async def list_usuarios(data: dict = Body(...), repo: UsuarioRepository = Depends(get_user_repository)):
  filtros = retira_vazios(data)
  result = repo.get_usuarios(filtros)

  if not result:
    raise HTTPException(status_code=404,  detail= result)

  return result


@users_controller.post("/create-usuario", tags=["Usuário"], summary="Criar novo usuário",)
async def crete_users(user: Usuario = Body(), repo: UsuarioRepository = Depends(get_user_repository)):
  senha = hash_password(user.senha_usuario)
  
  param = {
    'user_name': user.nome_usuario,
    'password': senha,
    'email': user.email
  }
  
  campos_vazios = [campo for campo, valor in param.items() if not valor or str(valor).strip() == '']

  if campos_vazios:
    raise HTTPException(
      status_code=400,
      detail=f"Os seguintes campos são obrigatórios e estão vazios: {', '.join(campos_vazios)}"
    )
    
  return repo.registrar_user(param)  