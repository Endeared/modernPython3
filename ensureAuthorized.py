from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if 'role' in kwargs:
            kwarg = kwargs.get('role')
            if kwarg == 'admin':
                return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper