from typing import Literal
from pydantic import BaseModel, Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class LogLevelSettings(BaseModel):
    default: str = Field(default="INFO")
    sqlalchemy: str = Field(default="WARN")


class LogNameSettings(BaseModel):
    app: Literal["migration-testing"] = "migration-testing"
    alembic: Literal["alembic"] = "alembic"
    sqlalchemy: Literal["sqlalchemy"] = "sqlalchemy"
    uvicorn: Literal["uvicorn"] = "uvicorn"


class LogSettings(BaseModel):
    formatter: Literal["[{}] - %(levelname)s - %(message)s"] = (
        "[{}] - %(levelname)s - %(message)s"
    )
    level: LogLevelSettings = LogLevelSettings()
    name: LogNameSettings = LogNameSettings()


class DbSettings(BaseModel):
    user: str = Field(default="")
    password: str = Field(default="")
    host: str = Field(default="")
    port: int = Field(default=0)
    name: str = Field(default="")

    @computed_field  # type: ignore[misc]
    @property
    def url(self) -> str:
        return "mysql+pymysql://{}:{}@{}:{}/{}".format(
            self.user, self.password, self.host, self.port, self.name
        )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_file=".env",
        nested_model_default_partial_update=True,
    )

    db: DbSettings = DbSettings()
    log: LogSettings = LogSettings()


settings = Settings()
