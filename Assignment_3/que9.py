##  Input 5 subject marks from user and display grade(eg.First class,Second class ..) 
Marathi = int(input('Enter the marks of Marathi: '))
Hindi = int(input('Enter the marks of Hindi: '))
English = int(input('Enter the marks of English: '))
Science = int(input('Enter the marks of Science: '))
Geography = int(input('Enter the marks of Geography: '))

total_marks = Marathi+Hindi+English+Science+Geography
percentage = (total_marks/500)*100

if(percentage>=65 and percentage<100):
    print('Student passed with First Class.')
elif(percentage>=55 and percentage<65):
    print('Student passed with Second Class.')
elif(percentage>=45 and percentage<55):
    print('Student is passed with Third Class.')
elif(percentage>=35 and percentage<45):
    print('Student passed with average.')
else:
    print('Student is fail.')