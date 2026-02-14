##WAP to print Fibonacci series upto n

n = int(input('Enter number of times:'))
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))

for i in range(n):
    c = a + b
    print(c)
    a = b
    b = c