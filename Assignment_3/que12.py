##Write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter the three digit number:'))
temp = num

d1 = temp % 10
temp = temp //10

d2 = temp % 10
temp = temp // 10

d3 = temp % 10
temp = temp // 10

rev_num = (d1*100) + (d2*10)+ d3

if(rev_num == num):
    print('It is an palindrome number. ')
else:
    print('It is not a palindrome number.')


