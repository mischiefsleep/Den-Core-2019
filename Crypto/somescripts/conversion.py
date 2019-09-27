#!/usr/bin/python3

# william
# This program will convert a decimal number in a specific base. By default if no base is specified by default the base is 16
# If the base is greater than 16 or less than 2 then by default the base will be 16
# This program can only work with positive integers, otherwise an Invalid input message will be shown
# A typical execution would appear like follows
# What base do you want for conversion ? (by default the base is 16 and it should not exceed 16) 12
# What is the decimal to convert ? 134
# The result is B2  in base 12
# The time complexity of this program is O(log(number)/log(base))

def base():
    try:
        base=int(input("What base do you want for conversion ? (by default the base is 16 and it should not exceed 16) "))
        # The program verifies that the user input is an integer
        if(base<2 or base >16): # The program verifies that the user intput is within bounds
            print("Invalid input") # If the user input is not within bounds an error message is shown
            return(1)
    except:
        # If the base is not an integer then the program assumes that it is not a voluntary error from the user and base will default to 16
        base=16
    return(base)


def main():
    values="0123456789ABCDEF" # Store the digits up to 15 in hex
    conversion_base=base() # define the base in which the input will be converted, this function call will also verify that the user input satisfies the conditions of the program
    if conversion_base!=1: # If the base is valid then proceed to the rest of the program
        try:
            number=int(input("What is the decimal to convert ? ")) # Ask the user for the number to convert, if it is not an integer then the process will go to the exception handler
            result=""
            while(number>conversion_base): # The program computes the remainders as long as needed and prints it in the correct form
                result=values[number%conversion_base]+result
                number=number//conversion_base
            print("The result is", values[number]+result, " in base", conversion_base)
            return(0)
        except: # If the user input is not a decimal number exit the program with exit code 1
            print("Invalid input")
            return(1)
    else: # If the base definition process has failed, exit the program with exit code 1
        print("Invalid input")
        return(1)


if __name__ == '__main__':
    main()
