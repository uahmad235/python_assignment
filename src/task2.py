import contextlib
import inspect
import io


def decorator_2(fn):
    """Print the inspect elements information of a decorated function"""
    
    def function_inspector(*args, **kwargs):
        print("Name:\t", fn.__name__)
        print("Type:\t", type(fn))
        print("Sign:\t", str(inspect.signature(fn)))
        print("Args:\t positional:", args)
        print("\t key=worded:", kwargs)
        print("Doc:\t", '\n\t '.join(fn.__doc__.split('\n')))
        print("Source: ", end=' ')
        print('\n\t '.join(inspect.getsource(fn).split('\n')))
        print("Output:", end='')

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            fn(*args, **kwargs)
        s = f.getvalue()
        for line in s.splitlines():
            print('\t', line)
        
    return function_inspector
