from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "DataLens AI"
    DATABASE_URL: str = "sqlite:///./datalens.db"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
