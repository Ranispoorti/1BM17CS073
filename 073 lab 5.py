class callDetail:
    def __init__(self,a,b,c,d):
        self.called_from=a
        self.called_to=b
        self.duration=c
        self.type=d
    def printout(self):
        print("Details:")
        print("Called From:",self.called_from)
        print("Called To:",self.called_to)
        print("Call Duration:",self.duration)
        print("Call Type:",self.type)
        print()    
class Util:
    def __init__(self):
        self.list_of_call_objects=None
    def parse_customer(self,list_of_call_string):
        l=[]
        for i in range(len(list_of_call_string)):
            a=list_of_call_string[i].split(",")
            b=callDetail(a[0],a[1],a[2],a[3])
            l.append(b)
        for i in l:
            i.printout()
call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)
