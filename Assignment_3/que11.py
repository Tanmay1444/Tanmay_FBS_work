## Accept age of five people and also per person ticket amount and then calculate total 
#amount to ticket to travel for all of them based on following condition : 
#a. Children below 12 = 30% discount 
#b. Senior citizen (above 59) = 50% discount 
#c. Others need to pay full.

p1 = int(input('Enter age of first person:'))
p2 = int(input('Enter age of second person:'))
p3 = int(input('Enter age of third person:'))
p4 = int(input('Enter age of fourth person:'))
p5 = int(input('Enter age of fifth person:'))

ticket_amt = 1000

if(p1>0 and p1<12):
    disc = ticket_amt*0.3
    amt1 = ticket_amt - disc
elif(p1>59):
    disc = ticket_amt*0.5
    amt1 = ticket_amt-disc
else:
    amt1 = ticket_amt

if(p2>0 and p2<12):
    disc = ticket_amt*0.3
    amt2 = ticket_amt - disc
elif(p2>59):
    disc = ticket_amt*0.5
    amt2 = ticket_amt-disc
else:
    amt2 = ticket_amt

if(p3>0 and p3<12):
    disc = ticket_amt*0.3
    amt3 = ticket_amt - disc
elif(p3>59):
    disc = ticket_amt*0.5
    amt3 = ticket_amt-disc
else:
    amt3 = ticket_amt

if(p4>0 and p4<12):
    disc = ticket_amt*0.3
    amt4 = ticket_amt - disc
elif(p4>59):
    disc = ticket_amt*0.5
    amt4 = ticket_amt-disc
else:
    amt4 = ticket_amt

if(p5>0 and p5<12):
    disc = ticket_amt*0.3
    amt5 = ticket_amt - disc
elif(p5>59):
    disc = ticket_amt*0.5
    amt5 = ticket_amt-disc
else:
    amt5 = ticket_amt

total_travel_amt = amt1+amt2+amt3+amt4+amt5

print(f'Total amount of ticket to travel is {total_travel_amt}rs.')