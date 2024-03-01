number= [1, 2, 3, 4]        #question 1
num = 5

number.append(num)

print(number)
# ------------------------------------------------------------------------

number = [1, 2, 3, 4, 5]  #question 2
remove = 3

number.remove(remove)

print(number)
# --------------------------------------------------------------------------

number = [3, 1, 4, 1, 5, 9, 2, 6, 5]  #question 3

number.sort()

print(number)
# ----------------------------------------------------------------------------

number = [3, 1, 4, 1, 5, 9, 2, 6, 5]  #question 4

number.reverse()
# ----------------------------------------------------------------------------

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2

print(list3)
# ----------------------------------------------------------------------------
# Tuple

cars = ("Toyota", "MG", "Kia")
# ----------------------------------------------------------------------------
# Dictionary
file1 = {'a': 1, 'b': 2}
file2 = {'c': 3, 'd': 4}

file1.update(file2)

print("Merged",file1)
# ----------------------------------------------------------------------------

try:
    width = 0
    width
except NameError:
    print("Variable has to be used before defining it ")
except ZeroDivisionError:
    print("Division by zero is invalid! Kindly change your input")
except Exception:
    print("Have caught a new error")
finally:
    print("Finally blocked execution")