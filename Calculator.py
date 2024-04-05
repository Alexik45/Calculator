def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."

while True:
    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. End")

    choice = input("Enter operation number (1/2/3/4/5): ")

    if choice == '5':
        print("End of the program.")
        break

    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        continue

    if choice == '1':
        result = addition(number1, number2)
    elif choice == '2':
        result = subtraction(number1, number2)
    elif choice == '3':
        result = multiplication(number1, number2)
    elif choice == '4':
        result = division(number1, number2)
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
        continue

    print("Result: {}".format(result))
