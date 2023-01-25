def make_song(count=99, beverage="soda"):
    
    while count > -1:
        if count == 0:
            yield "No more " + beverage + "!"
        elif count == 1:
            yield "Only " + str(count) + " bottle of " + beverage + " left!"
        else:
            yield str(count) + " bottles of " + beverage + " on the wall."
        count -= 1
    raise StopIteration