#include<stdio.h>

// Guilhem Mizrahi 10/2019

int main(){  
    
    printf("########### basic pointers #############\n");

    int a=1; 
// Create a variable storing an integer

    int* pointer_to_a=&a; 
// The & sign means "return the address of the variable"
// So &a holds the memory addres to a, which is a pointer

    int back_to_a=*pointer_to_a;
// To dereference a pointer (ie. get the value stored at the address 
// the pointer points to) we use the * in front of the pointer

    printf("a=%i\np_a=%p\na=%i\n", a, pointer_to_a, back_to_a);
// The print statement takes a string as input, but each %something in 
// the string creates a "hole" in the string that you have to fill with
// a parameter that has the type specified by the %something.
// example : %i creates a "hole" that you have to fill with an integer
// So you have to provide a integer parameter after the string in the printf.
// In the printf line 16 we have 3 holes:
//              one for an int
//              one for an address (pointer)
//              one for an int again
// So we give 3 arguments, an int, a pointer and an int again respectively.
    
// We can also manipulate pointers, do arithmetics, or nest them.
// for example:

    printf("\n########### list of characters aka strings #############\n");

// We create a "string" that we denote by a pointer to a character.
    char* string="abc";
    printf("string=%s at address %p\n", string, string);

// In reality what C does is it points to the first memory address of the string.
// So if we look at the value held at the memory address of the string

    char first_char=*string;
    printf("first letter=%c\n", first_char);

// We get the first character

// If we create a pointer to the same string, we can increment the pointer to reach 
// the memory addresses that come after the first address of the original pointer.
// Run this program and see how the addresses do up by one for each letter.
// This is because a char is 1byte long. If we have a pointer of integers (4bytes long)
// the addresses would increment by 4.

    for (char* pt=string; *pt!='\0'; pt++){
        printf("letter=%c at address %p\n", *pt, pt);
    }

// let's try with a list of integers.

    printf("\n########### list of integers #############\n");

    int list_of_int[3]={1, 2, 3};

// This creates a list of integers [1, 2, 3]. This list is actually exactly
// like a pointer but if we try to define it with int* then it expects just
// one int in the declaration (it's a compiler thing)
// we could initialise using a for loop as well but this is easier (in my opinion)

    int* p_int=list_of_int;

// But we can create a pointer and initialize it with the list so it's all good.
    
    for (int i=0; i<3; i++){
// We want to look at the 3 integers in the list.
// Because we don't have a stopping condition like we had for strings
// that end with '\0' we are forced to count the number of steps using a counter
// here the counter is i
        printf("number=%i at address %p\n", *p_int, p_int);
        p_int++;
// Run the program and pay attention to the value of the increment of the address
    }

    printf("\n########### over reading a list of integers #############\n");
// Now this also means that we can over read the memory (ie. read outside of the array in memory)
// by simply incrementing the pointer

    p_int=list_of_int;

// We reset the value of the pointer to start at the beginning of the array again

    for (int j=0; j<4; j++){
// This time instead of reading only the 3 values of the array we read 4 addresses in memory
// Look at the result of the program to see what happens
        printf("number=%i at address %p\n", *p_int, p_int);
        p_int++;
    }

    printf("\n########### nested pointers #############\n");

// We can nest pointers (ie. create pointers to pointers)

    char* nested[3] = {"abc", "defg", "hi"};
    char** p_nested=nested;

// p_nested is a pointer of pointers (hence the **)

    for (int k=0; k<3; k++){
        printf("The value at rank %i is %s at address %p\n", k, *p_nested, p_nested);
        p_nested++;
    }

// If you look at the addresses in the result, it is a bit difficult to make sense of the increments.
// My guess is that the compiler chooses a static value for he increment so that it is sure not to create conflicts.

    return(0);
}
