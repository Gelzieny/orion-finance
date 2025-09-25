from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl


class Settings(BaseSettings):
  VERSION: str = "1.0.0"
  POSTGRES_PRODUCAO_DB: str
  POSTGRES_PRODUCAO_HOST: str
  POSTGRES_PRODUCAO_PASSWORD: str
  POSTGRES_PRODUCAO_PORT: int
  POSTGRES_PRODUCAO_USER: str
  
  model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
  
  
settings = Settings()  