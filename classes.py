'''class person:
   def __init__(self, name, age):
      self.name = name
      self.age = age
p1 = person("yogi",23)
p1.age = 24
print(p1.name)
print(p1.age)'''

class calculator:
    def add(self, a , b):
        return a+b 
    def multiply(self, a, b):
        return a*b
r = calculator()
print(r.add(2,4))
print(r.multiply(34,5))

