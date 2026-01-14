import time
a = 1
b = 3
c = 2
print(a, b, c, "go!")

print("System error, numbers countdown wrong, rewriting...")
time.sleep(3)
a,b,c = b,a,c
print(a, c, b, "go!" )