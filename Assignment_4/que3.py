## WAP to print sum of even series upto n.  
n = int(input('Enter number to take sum of series:'))
i = 2
sum = 0

while(i<=n):
    sum = sum + i
    i+=2

print(f'The sum of the even series is {sum}.')

