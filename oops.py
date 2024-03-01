class Calculator:
    num = 100

    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b
        print("I am called automatically when object is created")

    def getdata(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num

obj = Calculator(20,20)
obj.getdata()
print(obj.num)
print(obj.summation())





