#NEEMA OGAO SCT211-0086/2022
#Prompt to input the total bill, tip, and the number of people
BillAmount=input("Please enter the total bill: $")
TipInput=input("What percentage tip would you like to give?(10,12,or15): ")
NumberOfPeople=input("Enter the number of people splitting the bill: ")

BillAmount=float(BillAmount)
TipInput=int(TipInput)
NumberOfPeople=int(NumberOfPeople)

#Calculate the tip, final bill, and the amount to be paid by each person
TipAmount=float(BillAmount)*float(TipInput/100)
TotalBill=BillAmount+TipAmount
AmountToPay=TotalBill/NumberOfPeople
FinalAmount=round(AmountToPay,2)

#Display the amount to be paid by each person
print("\nEach person will pay: "+str(FinalAmount))
