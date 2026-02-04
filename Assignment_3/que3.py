#Write a program to input angles of a triangle and check whether triangle is valid or not.

ang1= int(input('Enter the first angle:'))
ang2 = int(input('Enter the second angle:'))
ang3 = int(input('Enter the third angle:'))

sum = ang1+ang2+ang3

if(sum == 180):
    print('This is valid triangle.')
else:
    print('This is not valid traingle.')