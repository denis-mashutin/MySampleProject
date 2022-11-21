def int_to_str(fun):
    return str(fun())


@int_to_str
def func():
    return 2


value = func + 2


