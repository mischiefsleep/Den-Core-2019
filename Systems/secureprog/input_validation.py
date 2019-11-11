#!/usr/bin/python3

# Guilhem Mizrahi 09/2019

def first():
    var1=input("Enter the first number: ")
    var2=input("Enter the second number: ")

    print(var1/var2)

def second():
    var1=int(input("Enter the first number: "))
    var2=int(input("Enter the second number: "))

    print(var1/var2)

def third():
    retvalue1=""
    while(not retvalue1.isnumeric()):
        retvalue1=input("Type in first a number: ") 
    retvalue2=""
    while(not retvalue2.isnumeric()):
        retvalue2=input("Type in a second number: ") 
    retvalue1=int(retvalue1)
    retvalue2=int(retvalue2)
    print(retvalue1/retvalue2)

def fourth():
    while True:
        try:
            val1 = int(input("Enter the first number: "))
            val2 = int(input("Enter the second number: "))
            break
        except:
            print("You did not enter a number")
            continue
    print(val1/val2)

def fith():
    mylist = ["obj1","obj2","obj3"]
    myvar1 = 32
    myvar2 = "Something else"
    print('{} {}'.format(myvar1,myvar2))
    print('{1} {0}'.format(myvar1,myvar2))
    print('{} {}'.format(mylist[1],mylist[2]))

def sixth():
    for i in range(1,13):
        print("{:3d} {:4d} {:5d}".format(i, i**2, i**3))

if __name__=="__main__":
#    first()
#    second()
#    third()
#    fourth()
#    fith()
    sixth()
