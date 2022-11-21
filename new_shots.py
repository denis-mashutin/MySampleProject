
a = 1  # type: int


def bar(param):
    # type: (object) -> object
    return param


def foo(param):
    b = bar(param)
    return b

class C:
    foo = None  # type: object

    def __init__(self, p):
        self.foo = p


c = C('bar').foo






def bar2(param: int) -> None:
    # type: (int) -> None
    pass


def b(p1, p2):
    # type: (int) -> None
    pass


def bar3(param: int):
    pass

l = [1,3,4]

bar3(l)

