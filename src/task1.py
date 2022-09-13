import contextlib
import time
import io


def decorator_1(base):
    """prints function execution time and the number of times it was called"""
    
    no_of_calls = 0
    def f(*args, **kwargs):
        nonlocal no_of_calls
        st = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as _:
            base(*args, **kwargs)
        exec_time = time.time() - st
        no_of_calls += 1
        print(f"func {base.__name__} {no_of_calls} executed in {round(exec_time, 4)} sec")    
    return f
