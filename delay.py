from functools import wraps
from time import sleep

def delay(time):
    def innerFunc(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print("Waiting " + str(time) + "s before running " + fn.__name__)
            sleep(time)
            return fn(*args, **kwargs)
        return wrapper
    return innerFunc