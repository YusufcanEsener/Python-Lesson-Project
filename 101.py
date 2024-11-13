class Bird:
    def __init__(self):
        print("bird class init")
    def fly(self):
        print("bird is flying")
    def eat(self):
        print("bird is eating")
    def walk(self):
        print("bird is walking")
class Parrot(Bird):#inheritiance kalıtım
    def __init__(self):
        print("parrot class init")#base ==super pythonda
        super().__init__()
    def speak(self):
        print("parrot is speaking")
obj=Parrot()
object=Bird()
obj.speak()
object.eat()
