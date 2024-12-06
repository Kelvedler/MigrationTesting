from click import command, option
import uvicorn

from database.migrations import run_migrations as run_migrations_
from loggers import log_controller


@command(help="Starts Uvicorn server based on provided arguments.")
@option(
    "--host",
    default="127.0.0.1",
    help="Bind socket to this host. [default:127.0.0.1]",
)
@option("--port", default=8000, help="Bind socket to this port. [default: 8000]")
@option("--reload", default=False, is_flag=True, help="Enable auto-reload.")
@option(
    "--run-migrations",
    default=False,
    is_flag=True,
    help="Run database migrations to the latest version.",
)
def run(host: str, port: int, reload: bool, run_migrations: bool) -> None:
    if run_migrations:
        run_migrations_()
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=reload,
        log_config=log_controller.get_uvicorn_config(),
    )


run()
