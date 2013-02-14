my_variable = 1.0

def selfplus(i):
    global my_variable
    my_variable = my_variable + i
    return my_variable

def dispvar():
    global my_variable
    return my_variable
