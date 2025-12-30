print("enter marks of following subjects:")
alg = int(input("Marks of Algebra out of 100: "))
chem = int(input("Marks of Chemistry out of 100: "))
his = int(input("Marks of History out of 100: "))
lang =  int(input("Marks of Language out of 100: "))
lit = int(input("Marks of Litreture out of 100 : "))

sum = (alg+chem+his+lang+lit)
print("sum of subjects : ", sum )
perc = (sum/500)*100
print("percentage of all subjects is : ", perc )