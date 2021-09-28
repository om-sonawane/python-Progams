# n!= 1 X 2 X 3 X....X n
# 5! = 1 X 2 X 3 X 4 X 5 X

num = int(input("Enter the number:"))
factorial= 1
for i in range (1,num+1):
    factorial= factorial* i
print(f"the factorial of{num}is{factorial}")    
    