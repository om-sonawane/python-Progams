num = int(input("Enter the number: "))
prime = True
for i in range (2,num):
    if (num%i == 0 and num!=2):
         prime= False
         break
if prime:
    print("this number is prime")
else:
     print("this number is not prime")      
