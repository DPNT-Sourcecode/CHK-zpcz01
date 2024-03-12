# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if (0 <= x <= 100) and (0 <= y <= 100) and isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        return -1


