def sums(number):
    return sum(int(digit) for digit in str(number))

number = int(input("Enter an integer:"))
print("Sum of the digits entered :", sums(number))