from pydantic import BaseSettings


class Settings(BaseSettings):
    # APPLICATION SETTING
    APP_NAME: str = "Awesome Base Architecture"
    API_PREFIX: str = "/api/v1"

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
