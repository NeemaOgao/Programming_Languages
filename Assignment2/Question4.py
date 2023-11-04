#NEEMA OGAO SCT211-0086/2022
print("HELLO!")

#Prompt the user to enter a year
Year=input("Please enter the year: ")
Year=int(Year)

#Determine if the year entered is a leap year or not.
if (Year%4==0)and(Year%100!=0):
    print(str(Year)+" is a leap Year")
elif(Year%400==0):
    print("Leap Year")
else: print(str(Year)+" is not a leap year")
