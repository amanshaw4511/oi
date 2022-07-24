from typing import TypeVar, Callable, Iterable, Optional

T = TypeVar("T")

def find_any(fn: Callable[[T], bool] , iter: Iterable[T]) -> Optional[T]:
    return next(filter(fn, iter), None)
