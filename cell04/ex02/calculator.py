try: 
    num1 = int(input("Give me the first number: "))
    num2 = int(input("Give me the second number: "))

    print("Thank you!")

    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} / {num2} = {num1 // num2}")
    print(f"{num1} * {num2} = {num1 * num2}")

except ValueError:
    print("Please enter the valid number only!")
except ZeroDivisionError:
    print("Cannot devide by zero!")