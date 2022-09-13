import inspect


def decorator_2(ff):
    
    def f(*args, **kwargs):
        print("Name:\t", ff.__name__)
        print("Type:\t", type(ff))
        print("Doc:\t", '\n\t '.join(ff.__doc__.split('\n')))
        print("Sign:\t", str(inspect.signature(ff)))
        print("Source: ", end=' ')
        print('\n\t '.join(inspect.getsource(ff).split('\n')))
        print("Output:\t ", end='')
        ff(*args, **kwargs)
    return f
