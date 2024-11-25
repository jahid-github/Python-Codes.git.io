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
