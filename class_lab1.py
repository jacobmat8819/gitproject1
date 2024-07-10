class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


#-------------------


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}{self.age}"

p1 = Person("John", 36)

print(p1)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()



class family:
    def __init__(self,father,mother):
        self.father = father
        self.mother = mother

    def myfunc(self):
        print(f"The Father of the House is {self.father} \nThe Mother of the House is {self.mother}")

inst1 = family('Jacob','Shalini')
inst1.myfunc()


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


class family:
    def __init__(who,father,mother):
        who.father = father
        who.mother = mother
    
    def my_family(abc):
        print(f"Fathers Name is {abc.father} \nMothers Name is {abc.mother}")
    

inst2 = family('Jacob','Shalini')
inst2.my_family()