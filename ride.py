#over_riding
class Employee:
    def setnumofworkinghrs(self):
        self.numofworkinghrs = 40

    def displaythenumofworkinghrs(self):
        print(self.numofworkinghrs)

class Trainee(Employee):
    def setnumofworkinghrs(self):
        self.numofworkinghrs = 45

# super concept is used to reset the value which was set initially
    def resetnumofworkinghrs(self):
        super().setnumofworkinghrs()

# Employee func displaying
emp = Employee()
emp.setnumofworkinghrs()
print("Number of working hours of employees:",end = " ")
emp.displaythenumofworkinghrs()

# Trainee func displaying
trainee = Trainee()
trainee.setnumofworkinghrs()
print("Number of working hours of a Trainee:", end = " ")
trainee.displaythenumofworkinghrs()

# Reset func displaying
trainee.resetnumofworkinghrs()
print("Number of working hours have been reset:", end = " ")
trainee.displaythenumofworkinghrs()

# Method overriding refers to the ability of a subclass to provide a
# specific implementation of a method that is defined in its superclass
# When a method in a subclass has the same name , parameters and return type
# # as method in its superclass. The method in the subclass overrides
# the method in the superclass
