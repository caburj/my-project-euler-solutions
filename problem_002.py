import core
import decorators

problem = """
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

"""


@decorators.timeit
def calculate(fib_func, nmax=4e6):
    """
    Calculates the problem, where fib_func is the fibonacci function and nmax
    is the maximum value of fib number - in the problem, nmax is 4000000.
    """
    n = 0
    container = []
    while True:
        fn = fib_func(n)
        if fn > nmax:
            break
        if core.is_even(fn):
            container.append(fn)
        n += 1
    return sum(container)


if __name__ == '__main__':
    print(problem)
    print("\nsolution is %s" % calculate(core.fib_cache, 4000000))
