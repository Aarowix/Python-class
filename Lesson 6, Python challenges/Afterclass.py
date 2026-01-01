import time
a = 12
b = 120
c = 10
print("Numbers are",a,b,c)
print(a*b==c)
print("System error, numbers assigned wrong, rewriting...")
time.sleep(3)
a,b,c = b,c,a
print(b*c==a)