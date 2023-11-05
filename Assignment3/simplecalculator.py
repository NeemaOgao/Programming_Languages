#NEEMA OGAO SCT211-0086/2022
#Ask for the user's name and display it
username=input("Enter your name: ")
print("Hello "+username+"!")

class Calculator():
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def sum(self):
        return print(number1,"+",number2,"= ",(self.number1+self.number2))
    def difference(self):
        return print(number1,"-",number2,"= ",(self.number1-self.number2))
    def product(self):
        return print(number1,"x",number2,"= ",self.number1*self.number2)
    def division(self):
        return print(number1,"÷",number2,"= ",(self.number1/self.number2))

#Input two numbers from the user and calculate the sum and the difference
number1=float (input("Enter the first number : "))
number2=float (input("Enter the second number: "))
numbers= Calculator(number1,number2)

#Display the results
print("Sum:")
numbers.sum()
print("\nDifference:")
numbers.difference()
print("\nProduct:")
numbers.product()
print("\nDivision:")
numbers.division()