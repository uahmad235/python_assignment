import random
from task1 import decorator_1
from task2 import decorator_2
from task3 import ComputeMetrics, PrintSpecs, plot_table


@decorator_2
def pascal_triangle(n):
    """Calculates and returns pascal triangle"""
    results = [] # a container to collect the rows
    for _ in range(n): 
        row = [1] # a starter 1 in the row
        if results: # then we're in the second row or beyond
            last_row = results[-1] # reference the previous row
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            # finally append the final 1 to the outside
            row.append(1)
        results.append(row) # add the row to the results.

    return results

# @decorator_1
# def quadratic_solver(a, b, c):
#     """Solve Quadratic Equation"""
#     partial_num = (b ** 2 - 4 * a * c) ** (1/2)
#     denominator = 2 * a
#     first_root = ((-1 * b) + partial_num) / denominator
#     second_root = ((-1 * b) - partial_num) / denominator
#     return first_root, second_root


@ComputeMetrics
def quadratic_solver(a, b, c):
    """Solves Quadratic Equation"""
    quadratic = lambda a, b, c: ((((-1 * b) + ((b ** 2 - 4 * a * c) ** (1/2))) / 2 * a),\
                                    (((-1 * b) - ((b ** 2 - 4 * a * c) ** (1/2))) / 2 * a))
    return quadratic(a, b, c)

@decorator_2
def func():
    """Func2 does something great!"""
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)
        
@PrintSpecs
def funx(n=2, m=5):
    """funx does something excellent!"""
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i
    
if __name__ == "__main__": 
    func()
    funx()
    func()
    funx()
    func()
    pascal_triangle(3)
    pascal_triangle(190)
    quadratic_solver(4434525435343243, 4434525435343243, 4434525435343243)
    quadratic_solver(32, 43, 23)    
    plot_table()


# @decorator_1
# @decorator_2
# def funh(bar1, bar2=""):
#     """This function does something useful 
#     :param bar1: description
#     :param bar2: description
#     """ 
#     print("some\n\t multiline\n\t output")


# if __name__ == "__main__": 
#     funh(None, bar2="")
