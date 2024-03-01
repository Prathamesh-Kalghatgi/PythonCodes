Add = lambda x, y: x + y
result = Add(20, 35)
print(result)


# Note lambda functions are best used where you need a small one-off func for a short
# period of time especially when you don't want to define a full-fledged func using def func
# one of the scenarios passing funcs as arguments, simple transformation, anonymous func
# and call back func.
# Lambda func are not suitable for complex logic or large block of code

# Example
def classroom(n):
    square = lambda x: x + n
    return square


demo = classroom(20)
print(demo(30))


# Example2
def multiplier(n):
    multiplier_by = lambda x: x * n
    return multiplier_by


multiplier_by_5 = multiplier(5)
print(multiplier_by_5(10))
print(multiplier_by_5(7))
