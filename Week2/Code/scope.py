"""script demostrating variable scope"""
## Try this first

# set global variable
_a_global = 10

if _a_global >= 5:
    _b_global = _a_global +5


# 
def a_function():
    """ a function demonstrating variable scope, setting local variables """
    _a_global = 5

    if _a_global >= 5:
        _b_global = _a_global +5

    _a_local = 4

    print("Inside the function, the value of _a_global is ", _a_global)
    print("Inside the function, the value of _b_global is ", _b_global)
    print("Inside the function, the value of _a_local is ", _a_local)
    return None

a_function()

print("Outside the function, the value of _a_global is ", _a_global)
print("Outside the function, the value of _b_global is ", _b_global)




print('\n\n\n')

del(_a_global)
del(_b_global)
## Now try this

_a_global = 10

def a_function():
    """a function demonstrating variable scope, setting a local variable"""
    _a_local = 4
    print("Inside the function, the value of _a_local is ", _a_local)
    print("Inside the function, the value of _a_global is ", _a_global)
    return None

a_function()
print("Outside the function, the value of _a_global is", _a_global)

print('\n\n\n')

del(_a_global)

# Global keyword 

_a_global = 10

print("Outside the function, the value of _a_global is", _a_global)

def a_function():
    """a function demonstrating variable scope by declaring a local and a global variable"""

    global _a_global
    _a_global = 5
    _a_local = 4
    
    print("Inside the function, the value of _a_global is ", _a_global)
    print("Inside the function, the value _a_local is ", _a_local)
    
    return None

a_function()

print("Outside the function, the value of _a_global now is", _a_global)


print('\n\n\n')

del(_a_global)

# Nested functions and global keywords

def a_function():
    """a function demonstrating variable scope by setting a local variable and defining a nested function"""

    _a_global = 10

    def _a_function2():
        global _a_global
        _a_global = 20
    
    print("Before calling a_function2, value of _a_global is ", _a_global)

    _a_function2()
    
    print("After calling _a_function2, value of _a_global is ", _a_global)

a_function()

print("The value of a_global in main workspace / namespace is ", _a_global)


print('\n\n\n')

del(_a_global)


# Nested functions and global keywords


_a_global = 10

def a_function():
    """a function demonstrating variable scope by declaring a nested function"""

    def _a_function2():
        """a function demonstrating variable scope by setting a global variable"""
    
        global _a_global
        _a_global = 20
    
    print("Before calling a_function2, value of _a_global is ", _a_global)

    _a_function2()
    
    print("After calling _a_function2, value of _a_global is ", _a_global)

a_function()

print("The value of a_global in main workspace / namespace is ", _a_global)