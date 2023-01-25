from functools import wraps

def show_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return func(*args, **kwargs)
    return wrapper