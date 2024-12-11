if __name__ == '__main__':
    x = int(input())  # Read x dimension
    y = int(input())  # Read y dimension
    z = int(input())  # Read z dimension
    n = int(input())  # Read the restriction sum value

    # List comprehension to generate coordinates
    result = [[i, j, k] for i in range(x + 1) #All permutations of [i, j, k]:
                       for j in range(y + 1) 
                       for k in range(z + 1) 
                       if i + j + k != n] #if i + j + k != n ensures that only those combinations where the sum is not equal to n are included.
    print(result)  # The valid combinations of [i, j, k] are stored in the list result.


"""
#without n restrictions code
if __name__ == '__main__':
    x = int(input())  # Read x dimension
    y = int(input())  # Read y dimension
    z = int(input())  # Read z dimension

    # List comprehension to generate all possible coordinates
    result = [[i, j, k] for i in range(x + 1) 
                       for j in range(y + 1) 
                       for k in range(z + 1)]

    print(result)  # Print the resulting list
"""
