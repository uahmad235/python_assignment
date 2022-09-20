import contextlib
import time
import io


def decorator_1(fn):
    """Prints function execution time and the number of times
        it was called for the decorated function"""
    
    no_of_calls = 0
    def fn_call_tracker(*args, **kwargs):
        nonlocal no_of_calls
        st = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as _:
            fn(*args, **kwargs)
        exec_time = time.time() - st
        no_of_calls += 1
        print(f"func {fn.__name__} {no_of_calls} executed in {exec_time} sec")    
    return fn_call_tracker
