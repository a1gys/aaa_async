from asyncio import Task
from typing import Callable, Coroutine, Any


async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    # На вход приходит одна из стадий жизненного цикла корутины, необходимо
    # вернуть результат её выполнения.

    if isinstance(f, Callable):
        coroutine = f()
    elif isinstance(f, Task):
        coroutine = f.get_coro()
    elif isinstance(f, Coroutine):
        coroutine = f
    else:
        raise ValueError('invalid argument')

    result = await coroutine
    return result
