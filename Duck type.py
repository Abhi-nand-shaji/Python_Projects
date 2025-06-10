class Duck:
    def walk(self):
        print("This duck is walking")

    def quack(self):
        print("Tis duck is quacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def quack(self):
        print("This chicken is quacking")

class Person:
    def catch(self, duck):
        duck.walk()
        duck.quack()
        print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
