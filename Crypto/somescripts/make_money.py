#!/usr/bin/python3

def wanna_earn(wallet):
    return(wallet+10)

def main():
    wallet=0
    user_input=input("Wanna earn 10$ ? ")
    while user_input=='yes':
        wallet=wanna_earn(wallet)
        print("Congrats you have earned 10$")
        print("You now have", wallet,"$")
        user_input=input("Wanna earn 10$ ? ") 
    print("You should have said 'yes'")
    return(0)

if __name__=="__main__":
    main()
