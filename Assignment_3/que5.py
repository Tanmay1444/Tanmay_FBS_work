#Write a program to check whether the triangle is equilateral, isosceles or scalene 
#triangle. 
a = int(input('Enter the first side:'))
b = int(input('Enter the second side:'))
c = int(input('Enter the third side:'))

if(a==b==c):
    print('This is an equilateral triangle.')
elif(a==b or b==c or a==c):
    print('This is an isosceles triangle.')
elif(a!=b!=c):
    print('This is an scalene triangle.')
else:
    print('This is invalid triangle')

