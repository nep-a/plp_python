try:
    divide = 2 / 0
    print(divide)
except ZeroDivisionError:
    print("Cannot divide by zero.")