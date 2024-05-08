from pydantic.v1 import BaseSettings
from dotenv import load_dotenv, dotenv_values

config = dotenv_values()


class Settings(BaseSettings):
    # db_name: str = config["POLYC_DB_NAME"]
    # db_user: str
    # db_password: str
    # db_host: str
    # db_port: int

    class Config:
        env_prefix = "POLYC"
        env_file = ".env"

    # @property
    # def db_url(self) -> str:
    #     return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def db_url(self) -> str:
        return "sqlite:///test.db"


settings = Settings()
