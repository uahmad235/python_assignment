import time
import inspect
import contextlib
from task4 import ErrorLogsDecorator


rank_metrics = {}   # store function execution metrics
OUT_FILE = 'logs.txt'  # path where decorator logs will be dumped


def plot_rank_table():
    """Plot metrics table sorted by execution time"""
    sorted_metrics = sorted(rank_metrics.items(), key=lambda item: item[1])
    print('{: <17} | {: ^13} | {: ^15}'.format("PROGRAM", "RANK", "TIME"))
    for rank, fn_exec_time in enumerate(sorted_metrics):
        fn, exec_time = fn_exec_time
        print('{: <17}  {: ^15}  {: ^17}'.format(fn, str(rank + 1), exec_time))


def DecLogsHandler(fn):
    """Dumps logs of decorated function(s) in a txt file"""

    @ErrorLogsDecorator
    def wrapper(*args):
        fdesc = open(OUT_FILE, "a")
        with contextlib.redirect_stdout(fdesc) as _:
            return fn(*args)
    return wrapper


class decorator_3:
    """Prints function execution time and the number of times it was called"""
    def __init__(self, function):
        self.function = function
        self.counter = 0

    @DecLogsHandler
    def compute_execution_time(self, *args, **kwargs):
        st = time.time()
        global OUT_FILE

        self.function(*args, **kwargs)
        
        self.counter += 1
        exec_time = time.time() - st
        fname = self.function.__name__

        rank_metrics[fname] = exec_time
        print(f"func {fname} {self.counter} executed in {exec_time} sec")    

    @DecLogsHandler
    def inspect_object(self, *args, **kwargs):
        print("Name:\t", self.function.__name__)
        print("Type:\t", type(self.function))
        print("Doc:\t", '\n\t '.join(self.function.__doc__.split('\n')))
        print("Sign:\t", str(inspect.signature(self.function)))
        print("Source: ", end=' ')
        print('\n\t '.join(inspect.getsource(self.function).split('\n')))
        print("Output:\t", end='')
        # Uncomment this line to test exception handling functionality for decorator_4
        # raise ValueError("Some Value Error")
        self.function(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        
        self.compute_execution_time(*args)
        self.inspect_object(*args, **kwargs)
