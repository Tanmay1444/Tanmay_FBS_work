# WAP to check if a given number is prime number or not.
n = int(input('Enter number:'))
i = 2
while(i<n):
    if(n % i ==0):
        print('It is not a prime number.')
        break
    i=i+1
else:
    print('It is a prime number.')
