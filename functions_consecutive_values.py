if __name__ == '__main__':
  n= int(input()) #read input as an integer
  result = "" # initialize the empty string to hold the result
  for i in range(1, n+1): #loop from 1 to n (inclusive)
    result += str(i) #convert the number to a string with increamnet by 1
  print(result)
#sample input 3
#sample output 123
