## Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

correct_user_id = "TANMAY"
correct_pass = "1444"

for attempts in range(1, 4):
    user_id = input('Enter user id:')
    user_pass = input('Enter the password:')

    if(user_id==correct_user_id and user_pass==correct_pass):
        print('Login Successfull.')
        break
    else:
        print('Incorrect user id or password.')

        if(attempts<3):
            print('Try again/.')
        else:
            print('To many failed attempts, program terminated.')

    
