#####Write a program to enter P, T, R and calculate simple Interest. 

P = int(input("Enter the principal:"))
R = int(input("Enter the interest rate:"))
T = int(input("Enter the time(years):"))

simple_int = (P * R * T)/100
print(f'Simple interest is:{simple_int}')


