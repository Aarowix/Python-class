med_reason = (input("Did you have any Medical Cause, Y or N: "))
attend = (int(input("please enter your attendence : ")))
if med_reason == "Y" :
   print("you are allowed")
if attend >= 75:
    print("You are allowed for the exam")
else:
    print("you are not allowed for the exam")
