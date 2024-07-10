def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_name(**name):
    print('My Last name is '+ name['lname'])

my_name1 = my_name(fname = 'Jacob',lname = 'Mathew')


def my_function(*, x):
  print(x)

my_function(x = 3)