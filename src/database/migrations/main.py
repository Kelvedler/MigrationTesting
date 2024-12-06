from alembic.config import Config, command
from decorators import retry_on_exception
from sqlalchemy.exc import OperationalError


@retry_on_exception(OperationalError)
def run_migrations() -> None:
    config = Config()
    config.set_main_option("script_location", "database:migrations")
    command.upgrade(config, "head")
