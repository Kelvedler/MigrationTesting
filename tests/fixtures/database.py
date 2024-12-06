import contextlib
from typing import Any, Generator, Iterator
from typing_extensions import Self
from sqlalchemy.orm import Session, sessionmaker
from testcontainers.mysql import MySqlContainer  # type: ignore[import]
from sqlalchemy import create_engine
from pytest import fixture


class MysqlSessionManager:
    def __new__(cls) -> Self:
        if not hasattr(cls, "__instance"):
            cls.__instance = super(MysqlSessionManager, cls).__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        self._container = MySqlContainer("mysql:8.0.35")
        self._container.start()
        self.connection_url = self._container.get_connection_url()
        self._engine = create_engine(self.connection_url)
        self._sessionmaker = sessionmaker(self._engine, expire_on_commit=False)

    @contextlib.contextmanager
    def session(self) -> Iterator[Session]:
        session = self._sessionmaker()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


@fixture
def mysql_session_manager() -> MysqlSessionManager:
    return MysqlSessionManager()


@fixture
def mysql_session() -> Generator[Session, Any, Any]:
    session_manager = MysqlSessionManager()
    with session_manager.session() as session:
        yield session
