def calculate(**kwargs):

    if kwargs['operation'] == 'add' and kwargs['make_float'] == False:
        try:
            return(kwargs['message'] + " " + str(int(kwargs['first'] + kwargs['second'])))
        except KeyError:
            return('The result is ' + str(int(kwargs['first'] + kwargs['second'])))
    elif kwargs['operation'] == 'add' and kwargs['make_float'] == True:
        try:
            return(kwargs['message'] + " " + str(kwargs['first'] + kwargs['second']))
        except KeyError:
            return('The result is ' + str(kwargs['first'] + kwargs['second']))

    if kwargs['operation'] == 'subtract' and kwargs['make_float'] == False:
        try:
            return(kwargs['message'] + " " + str(int(kwargs['first'] - kwargs['second'])))
        except KeyError:
            return('The result is ' + str(int(kwargs['first'] - kwargs['second'])))
    elif kwargs['operation'] == 'subtract' and kwargs['make_float'] == True:
        try:
            return(kwargs['message'] + " " + str(kwargs['first'] - kwargs['second']))
        except KeyError:
            return('The result is ' + str(kwargs['first'] - kwargs['second']))

    if kwargs['operation'] == 'multiply' and kwargs['make_float'] == False:
        try:
            return(kwargs['message'] + " " + str(int(kwargs['first'] * kwargs['second'])))
        except KeyError:
            return('The result is ' + str(int(kwargs['first'] * kwargs['second'])))
    elif kwargs['operation'] == 'multiply' and kwargs['make_float'] == True:
        try:
            return(kwargs['message'] + " " + str(kwargs['first'] * kwargs['second']))
        except KeyError:
            return('The result is ' + str(kwargs['first'] * kwargs['second']))
    
    if kwargs['operation'] == 'divide' and kwargs['make_float'] == False:
        try:
            return(kwargs['message'] + " " + str(int(kwargs['first'] / kwargs['second'])))
        except KeyError:
            return('The result is ' + str(int(kwargs['first'] / kwargs['second'])))
    elif kwargs['operation'] == 'divide' and kwargs['make_float'] == True:
        try:
            return(kwargs['message'] + " " + str(kwargs['first'] / kwargs['second']))
        except KeyError:
            return('The result is ' + str(kwargs['first'] / kwargs['second']))

print(calculate(make_float=True, operation='subtract', first=2.5, second=4))