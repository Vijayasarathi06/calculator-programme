##Calculator
def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def multi(a,b):
    return (a*b)
def devide(a,b):
    if a==0 or b==0:
        print("please enter the crt value")
    else:
        print(a/b)
a=int(input("enter the value"))
b=int(input("enter the value"))
c=str(input("select the option add,sub,multi,devide"))
if(c =="add"):
    print(add(a,b))
elif(c =="sub"):
    print(sub(a,b))
elif(c =="multi"):
    print(multi(a,b))
elif(c =="devide"):
    (devide(a,b))
else:
    print("invalid no")
    



















