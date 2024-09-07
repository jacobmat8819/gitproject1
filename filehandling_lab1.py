f = open("demofile.txt")

f = open("demofile.txt", "rt")

f = open("demofile.txt", "r")
print(f.read())


f = open("demofile.txt", "r")
print(f.read(5))

f = open("demofile.txt", "r")
print(f.readline())

f = open("demofile.txt", "r")
for x in f:
  print(x)

f = open("demofile.txt", "r")
print(f.readline())
f.close()


f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile.txt", "r")
print(f.read())


f = open("myfile.txt", "w")
f.write("Just writing one line")

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")