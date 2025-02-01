from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    SECRETKEY: str
    ALGORITHM: str
    EXP: int
    REFRESH_EXP: int

    DB_HOST: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    @property
    def DB_URL(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}/{self.DB_NAME}'


settings = Settings()
