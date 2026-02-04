## Write a program to calculate profit or loss. 
cost = int(input('Enter the cost:'))
selling_price= int(input('Enter the selling price:'))

if(selling_price>cost):
    print('Profit')
elif(selling_price<cost):
    print('Loss')
else:
    print('No profit No loss.')