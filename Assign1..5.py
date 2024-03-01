Age = int(input("Enter an integer: "))
if Age<13:
    print("Your a child")
elif Age<20 and Age>12:
    print('Your a teen')
elif Age>19 and Age<60:
    print("Your an adult")
else:
    print("Your a senior citizen")
