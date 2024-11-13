class Parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return "{} is singing {}".format(self.name,song)
    def dance(self):
        return "{} is now dancing".format(self.name)
blu=Parrot("blu",10)
woo=Parrot("woo",13)
print(f"{blu.name} is {blu.age} years old.")
print(f"{woo.name} is {woo.age} years old.")
print("blu is {}".format(blu.__class__.species))
ahmet=Parrot("ahmet","kaya")
print(ahmet.sing("November Rain"))#fixlencek