##. WAP to print factorial of a number .

n = int(input('Enter number:'))
i = 1
fact = 1
while(i<=n):
    fact = fact*i
    i = i+1
print(f'Factorial of the {n} is {fact}.')


