import functools as ft
import time


def timeit(func):
    def timed(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print("--- %s seconds ---" % (time.time() - start_time))
        return result
    return timed


def cache(init_storage):
    """init_storage can be list or dict depending on needs."""
    def wrap(func):
        return ft.partial(func, storage=init_storage)
    return wrap


def profile(f, currently_evaluating=set()):
    # `currently_evaluating` will persist across all decorated functions, due
    # to "mutable default argument" behavior.
    # see also
    # http://stackoverflow.com/questions/1132941/least-astonishment-in-python-the-mutable-default-argument
    def g(*args, **kwargs):
        # don't bother timing it if we're already doing so
        if f in currently_evaluating:
            return f(*args, **kwargs)
        else:
            start_time = time.clock()
            currently_evaluating.add(f)
            try:
                value = f(*args, **kwargs)
            finally:
                currently_evaluating.remove(f)
            end_time = time.clock()
            print('time taken: {time}'.format(time=end_time - start_time))
            return value
    return g
