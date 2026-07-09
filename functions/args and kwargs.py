#Functions  that calculates the product of all numbers entered
def multiply(*args):
    result=1
    for arg in args:
        result*=arg
    
    return result

#print(multiply(2,3,5,6,8))

#Function that allows you to enter people's totems
def totem(**kwargs):
    for k,v in kwargs.items():
        print(k+"'s totem is",v)
    

print(totem(ashley="Nhari",valery="Chihera"))

