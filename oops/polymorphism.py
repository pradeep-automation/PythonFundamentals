class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Duck(Animal):
    def speak(self):
        return "Quack!"


# Function that uses polymorphism
def animal_sound(animal):
    return animal.speak()

# Create instances of different animal classes
dog = Dog()
cat = Cat()
duck = Duck()

# Call the function with different animal instances
print(animal_sound(dog))   # Output: Woof!
print(animal_sound(cat))   # Output: Meow!
print(animal_sound(duck))  # Output: Quack!
