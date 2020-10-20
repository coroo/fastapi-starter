from pydantic import BaseSettings


class Settings(BaseSettings):
    # APPLICATION SETTING
    APP_NAME: str = "Awesome Base Architecture"
    APP_DESCRIPTION: str = "Base App for next project"
    API_PREFIX: str = "/api/v1"
    APP_VERSION: str = "v1.0"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    APP_MODE: str = "development"
    # available in ['development','production']
    LOG_LEVEL: str = "info"
    # available in ['critical', 'error', 'warning', 'info', 'debug', 'trace']
    SECRET_KEY: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # DB CONNECTION
    DB_CONNECTION: str = "mysql"
    DB_PORT: int = 3306
    DB_HOST: str = "localhost"
    DB_DATABASE: str = "db-name"
    DB_USERNAME: str = "root"
    DB_PASSWORD: str = "root_pass"

    # ALLOWED ORIGINS
    ALLOWED_ORIGINS: str = "http://localhost:8080,http://127.0.0.1:8080"

    class Config:
        env_file = ".env"


settings = Settings()
