#NEEMA OGAO SCT211-0086/2022
#Find the current date
import datetime
currentDate=datetime.datetime.now()

#Prompt the user to enter their date of birth
YearOfBirth=int(input("Hello!\nPlease enter your year of birth: "))

#Check if the year entered isn't greater than the current one and if it is, prompt the user to enter a valid one
while(YearOfBirth>currentDate.year):
    print("Enter a valid option!")
    YearOfBirth=int(input("Please enter your year of birth: "))

#Prompt the user to enter a valid month of birth
MonthOfBirth=int(input("Please enter your month of birth: "))
while(MonthOfBirth<0)or(MonthOfBirth>12):
    print("Enter a valid option!")
    MonthOfBirth=int(input("Please enter your month of birth: "))

#Prompt the user to enter a valid day of birth (Assuming a month has 31 days)
DayOfBirth=int(input("Please enter your day of birth: "))
while(DayOfBirth<0)or(DayOfBirth>31):
    print("Enter a valid option!")
    DayOfBirth=int(input("Please enter your day of birth: "))

#Compute the age in months
if currentDate.month >= MonthOfBirth:
    AgeInMonths = currentDate.month - MonthOfBirth
else:
    AgeInMonths = 12 - (MonthOfBirth - currentDate.month)

#Compute the age in days
if currentDate.day >= MonthOfBirth:
    AgeInDays = currentDate.day - MonthOfBirth
else:
#Find the number of days in the previous month
    FormerMonth = currentDate.month - 1 if currentDate.month > 1 else 12
    DaysInFormerMonth = (currentDate.replace(month=FormerMonth).date() - datetime.date(currentDate.year, FormerMonth, DayOfBirth)).days
    AgeInMonths -= 1
    AgeInDays = DaysInFormerMonth + currentDate.day - DayOfBirth

#Calculate the age in years
AgeInYears=currentDate.year-YearOfBirth

#Display the age in years, months, and days.
print("Your age is: "+str(AgeInYears)+"years, "+str(AgeInMonths)+" months, and "+str(AgeInDays)+" days.")
