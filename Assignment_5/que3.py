## Accept no. of passengers from user and per ticket cost. 
# Then accept age of each passenger and then calculate total amount to ticket to 
# travel for all of them based on following condition :
#  a. Children below 12 = 30% discount 
# b. Senior citizen (above 59) = 50% discount
#  c. Others need to pay full.


# Accept number of passengers
n = int(input("Enter number of passengers: "))

# Accept per ticket cost
ticket_cost = float(input("Enter cost per ticket: "))

total_amount = 0

for i in range(1, n + 1):
    age = int(input("Enter age of passenger {}: ".format(i)))
    
    if age < 12:
        amount = ticket_cost * 0.70   # 30% discount
    elif age > 59:
        amount = ticket_cost * 0.50   # 50% discount
    else:
        amount = ticket_cost          # Full payment
    
    total_amount += amount

print("Total amount to be paid =", total_amount)
