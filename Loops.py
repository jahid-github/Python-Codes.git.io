if __name__ == '__main__': #without this line code will be executed but it is the common construct for building variable (__name__) and set the string (__main__)
#Executes only when the script is run directly (not imported as a module).
    n = int(input("Enter The Input Number: ")) #user for input, expecting an integer
    #Prompts the user for an integer input and stores it in the variable n.
    for i in range(0, n): #Initializes a for loop where the variable i starts at 0 and increments by 1 on each iteration until it reaches (but does not include) n. range(0, n) 
    #generates a sequence of numbers starting at 0 and ending at n-1.
        result = i**2 #Calculates the square of the current value of i using the ** (exponentiation) operator
        #Assigns the result of i * i to the variable result.
        i=i+1 #Increments i by 1. However, this line has no effect on the loop variable i because i is reset to the next value from range() in each iteration of the loop.
        print(result) #Prints the value of result (the square of the current i) to the console.
