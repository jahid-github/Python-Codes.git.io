"""Write a program to select paper bill denominations in an ATM.

The input is the value requested by the customer. Check if the value is a multiple of 5 (smallest available bill). Break down the value into bills of 100, 50, 10 and 5, using the largest possible bills.

Examples:
Withdrawing $375:
3 bills of $100
1 bill of $50
2 bills of $10
1 bill of $5
Withdrawing $57:
Sorry, amount must be a multiple of 5
"""
a=int(input("Withdrawing: "))
if a%5==0:
   b=a//100
   c=a%100
   print(b,"bills of 100")
   d=c//50
   e=a%50
   print(d,"bills of 50")
   f=e//10
   g=a%10
   print(f,"bills of 10")
   h=g//5
   print(h,"bills of 5")
else:
   print("Sorry, amount must be a multiple of 5")
