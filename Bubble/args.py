#*args - Variable number of arguments passed
# **kwargs - Key value pair


def add(*args):
    tot=0
    for i in args:
        tot=tot+i 
    print("total  = " , tot)
add(2,3)    
add(3,4,5,6)
add(2,3,4)

def add(**kwargs):
    return sum(kwargs.values())
a= add(a = 10,b=20,c=33)
print (a)