from logging import Logger, getLogger
from typing import Any, Dict
from logging.config import dictConfig

from settings import settings
from uvicorn.config import LOGGING_CONFIG

from utils import Singleton


class LogController(metaclass=Singleton):

    def __init__(self) -> None:
        conf_dict: Dict[str, Any] = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "app": {"format": settings.log.formatter.format(settings.log.name.app)},
                "alembic": {
                    "format": settings.log.formatter.format(settings.log.name.alembic)
                },
                "sqlalchemy": {
                    "format": settings.log.formatter.format(
                        settings.log.name.sqlalchemy
                    )
                },
            },
            "handlers": {
                "app": {
                    "formatter": "app",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                },
                "alembic": {
                    "formatter": "alembic",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                },
                "sqlalchemy": {
                    "formatter": "sqlalchemy",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                },
            },
            "loggers": {
                "app": {
                    "handlers": ["app"],
                    "level": settings.log.level.default,
                    "propagate": False,
                },
                "sqlalchemy": {
                    "handlers": ["sqlalchemy"],
                    "level": settings.log.level.sqlalchemy,
                    "propagate": False,
                },
                "alembic": {
                    "handlers": ["alembic"],
                    "level": settings.log.level.default,
                    "propagate": False,
                },
            },
        }
        dictConfig(conf_dict)

    def get_uvicorn_config(self) -> Dict[str, Any]:
        config = LOGGING_CONFIG
        for k in config["formatters"]:
            config["formatters"][k] = {
                "format": settings.log.formatter.format(settings.log.name.uvicorn)
            }
        handlers = ["default"]
        for k in config["loggers"]:
            config["loggers"][k] = {
                "level": settings.log.level.default,
                "handlers": handlers,
                "propagate": False,
            }
        return config

    def get_app(self) -> Logger:
        return getLogger("app")


log_controller = LogController()
