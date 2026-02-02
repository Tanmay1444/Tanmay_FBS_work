### Write a program to enter P, T, R and calculate Compound Interest. 

P = int(input("Enter the principal amount:"))
R = int(input("Enter the Interest rate:"))
T = int(input("Enter the time:"))

Compound_int = (P*(1+R/100)**T)-P
print(f'Compound interest is: {Compound_int}')