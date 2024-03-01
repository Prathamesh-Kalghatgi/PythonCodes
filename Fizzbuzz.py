num = 1
for num in range(1, 101):
    x = num % 3
    y = num % 5
    if (x==0 and y==0):
        print("Fizzbuzz")
    elif x==0:
        print("Fizz")
    elif y==0:
        print("Buzz")
    else:
        print(num)

