num1 = float(input("please enter first value : "))
num2 = float(input("please enter second value : "))
while(num2 !=0):
    temp = num2
    num2 = num1%num2
    num1 = temp
hcf = temp
print("HCF of N1 and N2 is :",hcf)