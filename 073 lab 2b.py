def rev(s):
    li=[]
    li=s.split(" ")
    print(li)
    li.reverse()
    print(li)
    print('-'.join(li))
def revs(s):
    l2=s.split(" ")
    l3=" "
    for i in l2 :
        l3+=i[::-1]
        l3+=" "
    print(l3)
s=input("Enter the string")
rev(s)
revs(s)
