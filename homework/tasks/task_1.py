from asyncio import Task
from typing import Callable, Coroutine, Any


async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    # На вход приходит одна из стадий жизненного цикла корутины, необходимо вернуть результат
    # её выполнения.

    if isinstance(f, Callable):
        pass
    elif isinstance(f, Task):
        pass
    elif isinstance(f, Coroutine):
        pass
    else:
        raise ValueError('invalid argument')
