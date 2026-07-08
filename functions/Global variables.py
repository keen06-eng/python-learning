msg="I love anime!!"

def announce():
    print("Inside function:",msg)

announce()
print("Outside function",msg)

#modifying global variable

def addon():
    global msg
    msg+=" A lot"
    print(msg)

addon()