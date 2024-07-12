def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()


x = 300

def myfunc():
  x = 150
  print(x)

myfunc()

print(x)

#------------------

def myname():
    name = 'Jacob'
    return name
x = myname()
print(x)

def func():
    i = 500
    def innerfunc():
        print(i)
    innerfunc()
func()


k = 600

def func1():
    k = 200
    print(k)

print(k)
func1()


def myfunc():
  global x

  x = 39.84

myfunc()

print(x)


x = 300

def myfunc():
  global x
  x = 200
  print(x)

myfunc()
print(x)


def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

