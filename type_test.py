from typing import TypedDict


class Movie (TypedDict):
    title: str
    year: int


def add_movie(movie: Movie) -> None:
    pass


add_movie({'title': 'Blade Runner', 'year': 1982})


def dec(fun: str):
    pass


@dec
def func(num) -> int:
    return num


value = func(4)







# from typing import final, Callable
#
# @final
# class A:
#     def method(self):
#         pass
#
#
# class B(A):
#     def method(self):
#         pass
#
#
# a: Callable[int, str]


def foo(d: dict, k: str) -> str:
    if k in d.keys():
        print(f"'bar' is {d['bar']}")
    else:
        raise KeyError(f"'bar' not found!")





