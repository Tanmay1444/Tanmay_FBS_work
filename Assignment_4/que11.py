##  WAP to check if given number Strong Number.  

num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    fact = 1
    i = 1
    
    while i <= digit:
        fact = fact * i
        i += 1
        
    sum = sum + fact
    temp = temp // 10

if sum == num:
    print("Strong Number")
else:
    print("Not a Strong Number")