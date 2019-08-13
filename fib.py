n=int(input())
fib=[]
a,b=0,1
c=0
for i in range(0,n) :
 fib.append(a)
 c=a
 a=b
 b=b+c
print(fib)
