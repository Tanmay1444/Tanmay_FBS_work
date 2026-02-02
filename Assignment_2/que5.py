### WAP to calculate selling price of book based on cost price and discount.

cost = int(input("Enter the cost of the book:"))
discount = int(input("Enter the discount percentage:"))

disc_amt = (discount/100)*cost

selling_price = cost - disc_amt

print(f'Selling price of book is:{selling_price}rs.')
