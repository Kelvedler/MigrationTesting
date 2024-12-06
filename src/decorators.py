from __future__ import annotations
from typing import Any, Callable, Type
from time import sleep
from loggers import log_controller

logger = log_controller.get_app()


def retry_on_exception(
    *exc: Type[Exception], retries: int = 2, interval_seconds: int = 5
) -> Callable:
    if not exc:
        exc = (Exception,)

    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            i = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except exc as e:
                    if i < retries:
                        logger.warning(e)
                        sleep(interval_seconds)
                        i += 1
                    else:
                        raise

        return wrapper

    return decorator
