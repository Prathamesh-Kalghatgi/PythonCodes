# Method overloading
# It has understood languages like C, C++ refers to the ability to define multiply methods
# with the same name but different parameters within a class. However, Python does not
# support method overloading in the same way that java or C++ does

# In Python , you can only have ob=ne method with a given name in a class. If ypo define
# methods with the same name, the last method definition will override the previous ones.
# Therefore, method overloading, as commonly understood does not exist in Python.

class mathoperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


math_ops = mathoperations()

result1 = math_ops.add(2, 3, 4)
print("Result1:", result1)

result2 = math_ops.add(2, 3)