from dotenv import find_dotenv, dotenv_values


env_path = find_dotenv()


config = dotenv_values(env_path)


class Settings:
    DB_HOST: str = config["DB_HOST"]
    DB_PORT: int = config["DB_PORT"]
    DB_NAME: str = config["DB_NAME"]
    DB_USER: str = config["DB_USER"]
    DB_PASSWORD: str = config["DB_PASSWORD"]
    SECRET_KEY: str = config["SECRET_KEY"]
    ALGORITHM: str = config["ALGORITHM"]
    VK_APP_ID: int = config["VK_APP_ID"]
    VK_APP_SECRET: str = config["VK_APP_SECRET"]
    VK_REDIRECT_URI: str = config["VK_REDIRECT_URI"]
    VK_AUTH_URL: str = config["VK_AUTH_URL"]
    VK_TOKEN_URL: str = config["VK_TOKEN_URL"]
    VK_API_URL: str = config["VK_API_URL"]
    CODE_VERIFIER: str = config["CODE_VERIFIER"]
    CODE_CHALLENGE: str = config["CODE_CHALLENGE"]
    STATE: str = config["STATE"]
    CLIENT_SECRET: str = config["CLIENT_SECRET"]


settings = Settings()


def get_db_url():
    return (
        f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@"
        f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    )
