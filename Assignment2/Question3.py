#NEEMA OGAO SCT211-0086/2022
print("Hello!")
#Prompt the user to enter their mass and height
UserMass=input("Please enter your mass in kilograms: ")
UserHeight=input("Please enter your height in meters: ")

UserMass=float(UserMass)
UserHeight=float(UserHeight)

#calculate the BMI
HeightSquared=UserHeight*UserHeight
BMI=UserMass/HeightSquared

#Display the outcome of the BMI
if (BMI<18.5):
    print("You are underweight")
elif (BMI>24.9):
    print("You are overweight")
else: print("You are normal weight")
