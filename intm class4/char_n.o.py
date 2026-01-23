string = str(input("Please enter a word : "))
char = str(input("Please enter a charecter : "))
i = 0
count = 0
while (i<len(string)):
    if (string[i] == char):
        count = count + 1
    i = i + 1
print("the total amount of times",char,"has occured : ",count)
