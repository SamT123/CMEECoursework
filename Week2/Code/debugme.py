import ipdb; ipdb.set_trace()

def createabug(x):
    """function with divide by zero error"""
    y = x**4

    z = 0
    
    y = y/z
    return y

createabug(25)