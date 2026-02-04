#Write a program to input any alphabet and check whether it is vowel or consonant.

alphabet = input('Enter alphabet:')

if(alphabet in ['a','A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']):
    print(f'{alphabet} is a vowel')
else:
    print('It is a consonant')