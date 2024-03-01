class A:
    def method(self):
        print("Method of class A")

class B(A):
    def method(self):
        print("Method of class B")

class C(A):
    def method(self):
        print("Method of class C")

class D(B, C):
    pass

d = D()
d.method()

# Return is used inside a function to exit the
# function and return a value back to the caller.
# It os typically the last statement in the function.
# Although we can have multiple return statements in different parts of the function

# Pass is a null operation python. It is used as a placeholder when a statement
# is syntactically required, but you don't want to execute the code. It is typically used in [laces
# where the syntax requires a statement, but we don't need any action to be taken.

# Polymorphism in python refers to the ability of different objects to respond to the same method
# of function call in different ways. It allows objects of different classes to be treated as a common superclass

# Duck typing is a concept in python where the type of class of an object is less important
# the method it defines.



class mathoperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

math_ops = mathoperations()

result1 = math_ops.add(2,3,4)
print("Result1:",result1)

result2 = math_ops.add(2,3)
