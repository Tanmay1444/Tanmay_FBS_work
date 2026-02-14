##  Write a program to check if given number is Armstrong number or not.  
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +  
#4*4*4*4)

# WAP to check Armstrong Number

num = int(input("Enter a number: "))
temp = num
count = 0
sum = 0

# Count number of digits
while temp > 0:
    count += 1
    temp = temp // 10

temp = num

# Calculate sum of digits raised to power count
while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** count)
    temp = temp // 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
