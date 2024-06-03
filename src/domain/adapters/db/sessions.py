from typing import Callable


def iget_async_session(url: str) -> Callable:  # noqa
    raise NotImplementedError


def iget_sync_session(url: str):  # noqa
    raise NotImplementedError
