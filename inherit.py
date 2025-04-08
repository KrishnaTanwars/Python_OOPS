# SIMPLE INHERITANCE


# # Base Class

# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # Derived Class

# class Dog(Animal):
#     def __init__(self):
#         self.behaviour = "friendly"
#     def speak(self):
#         print(f"{self.name} barks and he is very {self.behaviour}")

# # animal = Animal("Genric animal")
# # animal.speak()

# dog = Dog()
# dog.speak()



# SUPER 

class animal:
    def __init__(self):
        self.name = "Buddy"
    def speak(self):
        print(f"{self.name} makes a sound")

class dog(animal):
    def __init__(self,breed):
        self.breed =  breed
        super().__init__()
    def speak(self):
        super().speak()
        print(f"{self.name} barks. It is {self.breed}")

dog = dog("golden")
dog.speak()