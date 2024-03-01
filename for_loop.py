favfruits = ["Apple", "Mango", "Berry", "Orange"]
print(favfruits)
for demo in favfruits:
    print(demo)

#range()
for number in range(1, 10):
    print(number)

temp = 77
while temp >= 68 and temp <= 77:
    print("Room temp is maintained at {} deg F".format(temp))
    temp = temp-1

#Matrix 3*3
n = 1
for row in range(1, 4):
    for column in range(1, 4):
        print(n, end =' ')
        n = n + 1
    print()



#Continue
for n in range(1, 11):
    if n == 5:
        continue
    else:
        print(n)

else:
    print("All the numbers are printed withput breakin")

 #Break
for n in range(1, 11):
    if n == 5:
        break
    else:
        print(n)
else:
    print("All the numbers are printed without breaking")