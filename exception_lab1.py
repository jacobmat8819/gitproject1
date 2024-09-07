try:
  print(x)
except:
  print("An exception occurred")


try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")



try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")       




price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)





