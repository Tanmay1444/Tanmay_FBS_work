### Write a program to reverse three-digit number. 

num = int(input("Enter the three digit number:"))

reversed_num = int(str(num)[::-1])
print(f'Reversed number is: {reversed_num}')