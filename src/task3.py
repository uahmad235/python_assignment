import time
import inspect
import contextlib


metrics = {}   # store function execution metrics
OUT_FILE = 'logs.txt'  # path where decorator logs will be dumped


def plot_table():
    """Plot metrics table by rank"""
    sorted_metrics = sorted(metrics.items(), key=lambda item: item[1])
    print('{: <17} | {: ^13} | {: ^15}'.format("PROGRAM", "RANK", "TIME"))
    for rank, fn_exec_time in enumerate(sorted_metrics):
        fn, exec_time = fn_exec_time
        print('{: <17}  {: ^15}  {: ^17}'.format(fn, str(rank + 1), exec_time))


def Decorator(ff):
    def wrapper(*args):
        fdesc = open(OUT_FILE, "a")
        with contextlib.redirect_stdout(fdesc) as k:
            return ff(*args)
    return wrapper


class SpecsMetrics:
    """Prints function execution time and the number of times it was called"""
    def __init__(self, function):
        self.function = function
        self.counter = 0

    @Decorator
    def myfun(self, *args):
        st = time.time()
        global OUT_FILE

        self.function(*args)
        
        self.counter += 1
        exec_time = time.time() - st
        fname = self.function.__name__

        metrics[fname] = exec_time
        print(f"func {fname} {self.counter} executed in {exec_time} sec")    

    @Decorator
    def myfun2(self, *args, **kwargs):
        print("Name:\t", self.function.__name__)
        print("Type:\t", type(self.function))
        print("Doc:\t", '\n\t '.join(self.function.__doc__.split('\n')))
        print("Sign:\t", str(inspect.signature(self.function)))
        print("Source: ", end=' ')
        print('\n\t '.join(inspect.getsource(self.function).split('\n')))
        print("Output:\t ", end='')
        self.function(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        
        self.myfun(*args)
        self.myfun2(*args, **kwargs)
