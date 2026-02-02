### Convert the time entered in hh,min and sec into seconds. 

hours = int(input("Enter the time in hh:"))
minutes = int(input("Enter the time in min:"))

total_sec = (hours*3600) + (minutes*60)
print(f'After converting time in seconds is:{total_sec}')