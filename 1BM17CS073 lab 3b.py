import string
import random
n=int(input("Enter the size of the password required"))
str1=string.printable
for i in range(n):
    print(str1[random.randint(0,100)],end="")
