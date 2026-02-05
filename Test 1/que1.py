## 
l = int(input('Enter the length:'))
b = int(input('Enter the breadth:'))
r = int(input('Enter the radius:'))

# area 
area_rect = (l*b)
area_circle = (3.14*r)**2/2
area_of_shape = (area_rect + area_circle)

# perimeter 
peri_rect = 2*(l+b)
peri_cir = (2*3.14*r)/2
perimeter_of_shape = (peri_rect+peri_cir)

print(f'Area of the shape is {area_of_shape}, and Perimeter of the shape is {perimeter_of_shape}')

