from alembic.config import Config, command


def test_run_migrations(mysql_session_manager):
    config = Config()
    config.set_main_option("sqlalchemy.url", mysql_session_manager.connection_url)
    config.set_main_option("script_location", "src.database:migrations")
    command.upgrade(config, "head")
    command.downgrade(config, "base")
