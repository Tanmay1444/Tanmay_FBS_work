## Write a program to check if the given number is positive or negative.
num = int(input('Enter the number:'))

if(num==0):
    print('Number is a neutral.')
elif(num>0):
    print(f'{num} is a positive number.')
else:
    print(f'{num} is a negative number.')