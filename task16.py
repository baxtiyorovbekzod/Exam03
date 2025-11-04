
class Bird:
    def speak(self):
        print("Chirp chirp")

class Dog:
    def speak(self):
        print("Woof woof")


animals = [Bird(), Dog(), Bird(), Dog()]


for animal in animals:
    animal.speak()