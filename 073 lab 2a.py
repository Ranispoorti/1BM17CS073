def search(l1,k):
 if k in l1 :
    return True
 return False
l1=list(map(int,input().split()))
k=int(input("enter the key to be searched"))
print(search(l1,k))
