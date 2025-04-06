#Initiate a class
class employee:
    # Special method/ magic method/ dunder method - constructor
    def __init__(self):
        print("started excecuting attribiutes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "MLE"
        print("attributes/data have been initiated")
    
    def travel(self,destination):
        print("This travel method was called manually")
        print(f"Emploeyee is now travelling to {destination}")

# Create an instance/object of the class
sam = employee()

# Printing an attribute
# print(sam.salary)

# Calling a method
sam.travel("Delhi")

print(type(sam))