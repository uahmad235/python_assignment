import time
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

class ComputeMetrics:
    """Prints function execution time and the number of times it was called"""
    def __init__(self, function):
        self.function = function
        self.counter = 0
     
    def __call__(self, *args):
 
        st = time.time()
        global OUT_FILE

        fdesc = open(OUT_FILE, "a")
        with contextlib.redirect_stdout(fdesc) as k:
            self.function(*args)
        
        self.counter += 1
        exec_time = time.time() - st
        fname = self.function.__name__

        metrics[fname] = exec_time
        print(f"func {fname} {self.counter} executed in {exec_time} sec")    
