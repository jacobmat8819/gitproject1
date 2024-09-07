x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


x = abs(-7.25)

print(x)

x = pow(4, 3)

print(x)

x = abs(-45.45)
print(x)

x = pow(5,2)
print(x)


import math

x = math.sqrt(64)

print(x)

y = math.sqrt(81)
print(y)

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1


i = math.ceil(777.77)
j = math.floor(777.47)
print(i,'\n',j)

x = math.pi

print(x)

import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
