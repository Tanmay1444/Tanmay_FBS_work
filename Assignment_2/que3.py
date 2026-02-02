### Convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter distant in feet:"))
inches = int(input("Enter distant in inches:"))

meters = (feet*0.3048)+(inches*0.0254)
centimeters = (meters*100)

print(f'Distant in meter is:{meters}m, and Distant in centimeter is:{centimeters}cm.')