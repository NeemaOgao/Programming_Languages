#NEEMA OGAO SCT211-0086/2022

def Sum(Number1,Number2):
    sum =Number1+Number2
    return sum
def Difference(Number1,Number2):
    return Number1-Number2
def Product(Number1,Number2):
    return Number1*Number2
def Division(Number1,Number2):
    try:
        return Number1/Number2
    except ZeroDivisionError:
        print("Division of any number by zero is undefined!")

def Calculator():
    #Ask for the user's name and display it
    username=input("Enter your name: ")
    print("Hello "+username+"!")

    try:
        #Input two valid numbers from the user
        Number1=float(input("Enter the first number : "))
        Number2=float(input("Enter the second number: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    #Display the results obtained
    print("\n\nResults:\n")
    print(Number1,"+",Number2,"= ",Sum(Number1,Number2))
    print(Number1,"-",Number2,"= ",Difference(Number1,Number2))
    print(Number1,"x",Number2,"= ",Product(Number1, Number2))
    print(Number1,"÷",Number2,"= ",round(Division(Number1,Number2),4))

Calculator()