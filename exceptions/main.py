#Exceptions
try:
    number = int(input("enter a number:"))

    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers")
except Exception:
    print("Something went wrong")
finally:
    print("Do some cleanup here")
