from typing import Optional
from pydantic import BaseModel, Field

class Usuario(BaseModel): 
  nome_usuario:  str = Field()
  senha_usuario:  str = Field()
  email: str = Field()