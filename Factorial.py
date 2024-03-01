num = int(input("Enter a integer:"))
def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * factorial(x - 1)

result = factorial(num)
print(f"The factorial of {num} is {result}.")