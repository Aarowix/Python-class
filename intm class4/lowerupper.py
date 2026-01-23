lower = int(input("Please enter Lower Range : "))
upper = int(input("Please enter Upper Range : "))
print("The prime numbers between",lower,"and",upper,"is:")
for num in range(lower,upper+1):
    if num>0:
        for i in range(2,num):
            if(num%i) == 0:
                    break
        else:
             print(num)
