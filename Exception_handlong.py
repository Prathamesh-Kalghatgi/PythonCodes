try:
    width = 0
    length/width
except NameError:
    print("Variable has to be used before defining it ")
except ZeroDivisionError:
    print("Division by zero is invalid! Kindly change your input")
except Exception:
    print("Have caught a new error")
finally:
    print("Finally blocked execution")