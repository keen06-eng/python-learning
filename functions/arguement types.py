#default arguements
def myFun(x,y=10):
    print("x:",x)
    print("y:",y)

myFun(5) #y=10 because no value was passed to y 

#keyword arguements
def nameAge(fname,lname):
    print(fname,lname)

nameAge(fname="Ashley",lname="Gatsi")
nameAge(lname="Gatsi",fname="Ashley")#prints the same as above statement because order doesnt matter

#positional arguements
#values are assigned to parameters in the order they are passed

def demo(name,age):
    print("Hi my name is ",name)
    print("I am ",age," years old")

demo('Ashley',20)
demo(20,'Ashley')

#Arbitrary arguements (*args and **kwargs)
def func(*args,**kwargs):
    print("Non-keyword arguements")
    for arg in args:
        print(arg)
    
    print("Keyword arguements")
    for key,value in kwargs.items():
        print(f"{key}=={value}")
    
func('hie','welcome',first='ashley',last='gatsi')
