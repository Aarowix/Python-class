unit = (int(input("Please enter the units you have consumed : ")))
if unit <= 50:
    amount = unit*2.60
    surcharge = 25
elif unit <= 100:
    amount = 130+((unit-50)*3.25)
    surcharge = 35
elif unit <= 200:
    amount = 130+162.50+((unit-100)*5.25)
    surcharge = 45
else:
    amount = 130+162.50+526+((unit-200)*8.25)
    surcharge = 75
print("\nElectricity Bill is : ", amount+surcharge)