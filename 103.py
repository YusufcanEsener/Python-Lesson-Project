class Cat:
    def speak(self):
        print("meow ->_<-")
    def eat(self):
        print("cat is eating")
class Dog:
    def speak(self):
        print("hav")
    def eat(self):
        print("dog is eating")
def eat_test(mammal):
    mammal.eat()
obj1=Cat()
obj2=Dog()
print("Testing cat's eat method:")
eat_test(obj1)
print("Testing dog's eat method:")
eat_test(obj2)
