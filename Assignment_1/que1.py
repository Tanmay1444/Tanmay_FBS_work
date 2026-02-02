####Write a program to calculate the percentage of student based on marks of any 5 
####subjects.

sub1 = int(input('Enter the Marks of English:'))
sub2 = int(input('Enter the Marks of Marathi:'))
sub3 = int(input('Enter the Marks of Mathematics:'))
sub4 = int(input('Enter the Marks of Hindi:'))
sub5 = int(input('Enter the Marks of Geography:'))

calc_percentage = (sub1 + sub2 + sub3 + sub4 + sub5)/(500)*100
print(f'Percentage of the student is {calc_percentage}.')