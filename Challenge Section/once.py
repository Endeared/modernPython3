def once(func):

    func.do = False

    def inner(*args):
        if not(func.do):
            func.do = True
            return func(*args)
            
    return inner