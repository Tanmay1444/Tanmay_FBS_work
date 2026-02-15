##  Write a program to solve the following series :

#a. 1! + 2! + 3! + 4! + .....n!
#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
#e. x - x2/3 + x3/5 - x4/7 + .... to n terms

# 1! + 2! + 3! + ... + n!
n = int(input("Enter value of n: "))

i = 1
sum = 0

while i <= n:
    fact = 1
    j = 1
    
    while j <= i:
        fact *= j
        j += 1
    
    sum += fact
    i += 1

print("Sum of factorial series =", sum)



#N + N² + N³ + ... + Nᴺ
n = int(input("Enter value of N: "))

i = 1
sum = 0

while i <= n:
    sum += n ** i
    i += 1

print("Sum =", sum)


#n = int(input("Enter number of terms: "))

i = 0
sum = 0

while i < n:
    sum += 2 ** i
    i += 1

print("Sum of geometric series =", sum)



#S = a + a*2/2 + a*3/3 + ... + a*10/10
a = int(input("Enter value of a: "))

i = 1
sum = 0

while i <= 10:
    sum += (a ** i) / i
    i += 1

print("Sum =", sum)


#x - x²/3 + x³/5 - x⁴/7 + ... upto n terms
x = int(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

i = 1
sum = 0
sign = 1
den = 1

while i <= n:
    sum += sign * (x ** i) / den
    sign *= -1
    den += 2
    i += 1

print("Sum =", sum)