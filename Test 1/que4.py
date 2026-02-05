area = int(input('Enter the area of the wall (sq/m):'))
cost1= int(input('Enter the cost of interior wall (per sq/m):'))
cost2= int(input('Enter the cost of exterior wall (per sq/m):'))

## there are total 8 interior and 7 exterior walls.
interior = (area) * (8) * (cost1)
exterior = (area) * (7) * (cost2)

total_cost = interior + exterior

print(f'Total cost for painting the buildings wall is {total_cost}.')