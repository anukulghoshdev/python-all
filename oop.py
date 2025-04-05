class Person:   #create class
    pass

person1 = Person()  # create object
print(person1)

class Animal:
    pass

dog = Animal()
print(dog)


# __init__(), self
class Animal:
    def __init__(self, name, species): #__init__() -> constructor — object বানানোর সময় যেটা অটোমেটিক কল হয়।
        self.nam = name #attribute -> self.nam, self.species
        self.species = species

    def make_sound(self):
        print(f"{self.nam} is making sound")

    def intruduce(self):
        print(f"আমি একটি {self.species} এবং আমার নাম {self.nam}")

dog = Animal("Tony", "dog") #create object
cat = Animal("Kitty", "cat")

print(dog.nam)
print(dog.species)
dog.make_sound()

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

my_stack = Stack()

my_stack.push(523)
my_stack.push(334)
my_stack.push(431)
print(my_stack.items)
