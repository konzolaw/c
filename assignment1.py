#name IRKE KONZOLO
#REGNO SCT211-0081/2022
#Course :BSC.computer science
# assignment one a simple calculator that performs addition subtraction multiplication and divison and also greets the user  by  name 


name = (input("ENTER YOU NAME PLEASE ")) #storing the name and prompting
#declaration of variable constants operators
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 'Syntax Error! Division by zero is prohibited'
    else:
        return a / b

while True:
    #user interface screen output prompts 
    print("choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Select a choice ((1)or(2)or(3)or(4)or(5)): ")
# using the loop to perfom the different function  operations
# 
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Input the first number: "))
        num2 = float(input("Input the second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            print("Another calculation?")

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            print("Another calculation?")

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            print("Another calculation?")

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            print("Another calculation?")

    elif choice == '5':
        print("CLOSING CALCULATOR.... ")
        print("GOODBYE " + name)
        break

    else:
        print("Invalid Input")