from fastapi import HTTPException

from src.utils.utils import *
from src.dependencies.conexao import ConexaoPostgres


class UsuarioRepository:
  def __init__(self, db_connection: ConexaoPostgres):
    self.base = db_connection

  def get_usuarios(self, user: dict) -> dict:
    params = {}
    
    query = """
      SELECT 
        codigo,
        to_char(created_at, 'DD/MM/YYYY HH24:MI:SS') AS created_at,
        user_name,
        email  
      FROM "Users" where 0 = 0
    """   

    if 'user_name' in user and user['user_name']:
      query += " AND user_name = :user_name"
      params['user_name'] = user['user_name']
      
    if 'email' in user and user['email']:
      query += " AND email = :email"
      params['email'] = user['email']  
    
    query += f""" ORDER BY user_name ASC"""
               
    return self.base.select(query, params)
  
  def registrar_user(self, info: dict) -> dict:
    user = self.get_usuarios({'email': info['email']})

    if user and len(user) > 0:
      raise HTTPException(
        status_code=400, 
        detail=f"E-mail '{info['email']}' já cadastradp  para o usuário '{user[0]['user_name']}'."
      )  
      
    query = """
      INSERT INTO "Users" (user_name, email, password)
      VALUES (:user_name, :email, :password)
    """  
    
    ret = self.base.insert(query, info)
    
    return {
      'codigo': 1 if ret.get('success') else 99,
      'message':"Usuário cadastrado com sucesso" if ret.get('success') else "Erro ao cadastrar usuário"
    }
