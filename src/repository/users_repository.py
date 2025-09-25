from fastapi import HTTPException

from src.utils.utils import *
from src.dependencies.conexao import ConexaoPostgres


class UsuarioRepository:
  def __init__(self, db_connection: ConexaoPostgres):
    self.base = db_connection

  def get_usuarios(self) -> dict:
    query = """
      SELECT * FROM "Users"
    """
    
    ret = self.base.select(query)
    
    return ret