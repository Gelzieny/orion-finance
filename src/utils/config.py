from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl


class Settings(BaseSettings):
  VERSION: str = "1.0.0"
  model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
  
  
settings = Settings()  