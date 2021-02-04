def calculator_add(a, b):
    if (type(a) != float or type(b) != float):
        return None
    else:
        return a + b

def calculator_sub(a, b):
    if (type(a) != float or type(b) != float):
        return None
    else:
        return a - b

def calculator_mul(a, b):
    if (type(a) != float or type(b) != float):
        return None
    else:
        return a * b

def calculator_div(a, b):
    if (type(a) != float or type(b) != float):
        return None
    elif b == 0:
        return None
    else:
        return a / b