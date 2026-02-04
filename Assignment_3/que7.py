# Write a program to check if user has entered correct userid and password. 
user_id = input('Enter user id:')
password = input('Enter password: ')

if((user_id == 'Tanmay_1444') and (password=='146244')):
    print('This is genuine user.')
else:
    print('This is invalid user.')