import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


mytext = 'My Name is Jacob Mathew and I am from Bhilai'
y = re.search("^My.*Bhilai$",mytext)

if y:
    print("You are Lucky")
else:
    print("Sorry your Unlucky")


import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)