#!/usr/bin/python3

allowed="azertyuiopqsdfghjklmwxcvbn"
not_allowed="@#&é\"'(§è!çà)°-_^¨$*€ù%`£,?;.:/=+<>¿·\\±"

def white_list():
    '''
    This function will ask the user for a password and check if the letters are all in a white list.
    '''
    word=input("Type in the password you want: ")
    ok=True # by default consider the password valid
    for letter in word:
        if letter not in allowed:
            ok = False # if a letter outside the white list is found then the password becomes invalid
            break
    if ok:
        print("Your password is allowed")
    else:
        print("Your password is not allowed")

def black_list():
    '''
    This function will ask the user for a password and check none of the characters are in a black list.
    '''
    word=input("Type in the password you want: ")
    ok=True # by default the password is valid
    for letter in word:
        if letter in not_allowed:
            ok=False # if one letter in found in the black list then the password becomes invalid
            break
    if ok:
        print("Your password is allowed")
    else:
        print(word)

if __name__=="__main__":
    white_list()
#    black_list()
