#Local Scope
 
def myfunc():
    x = 300
    print(x)
myfunc()

# Function inside Function

def myfunc1():
    x = 3000
    def myinnerfunc():
        x = 2000
        print(x)
    myinnerfunc()
    print(x)
myfunc1()


# Global Scope

x = 300
def myfunc2():
    x = 200
    print(x)
myfunc2()
print(x)

# Global Keyword

def myfunc3():
    global x
    x = 300
    print(x)
myfunc3()
print(x)

# Nonlocal Keyword

def myfunc4():
    x = 'Jacob'
    def myfunc5():
        nonlocal x
        x = 'Hello'
    myfunc5()
    return x
print(myfunc4())