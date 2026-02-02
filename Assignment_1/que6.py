#### Write a Program to input two angles from user and find third angle of the 
#triangle. 

a1 = int(input("Enter the value of fisrt angle:"))
a2 = int(input("Enter the value of second angle:"))

third_angle = 180 - (a1 + a2)
print(f'Third angle is: {third_angle}')