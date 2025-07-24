class Animal:
    def sound(self):
        print("Animal makes sound")
class Pets(Animal):
    def character(self):
        print("Pets are amazing")
class Dog(Pets):
    def bark(self):
        print("Dog is barking")
a=Dog()
a.sound()
a.bark()