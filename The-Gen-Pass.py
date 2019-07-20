#Random password generating program named the Gen-Pass 

#import libraries first
#password meter will allow us to test the strenghth of the password
#We will use the passwordmeter test function to check strength as wella s tak advantage of it's advice
import passwordmeter
from passwordmeter import test
#This downloads thousands of words we can use in the generation of our passwords
import random
from random import choice,randint

chars = 'abcdefghigklomnopqrstuvwxyz'
#Add as many special characters as you want
special_chars=['!','?','$','#','&']

#Password generator function

#In the first for loop we are iterating for as many characters as we want defaulting to a value we input, convert it to lower case
#and capitalize the first letter
#In the second for loop we will iterate for as many numbers as we want, randomly selecting from 0-9
#In the thrid loop we wil iterate for as many special characters as we want defaulting to just one of our options
def create_password(num_chars=5,num_numbers=4,num_special=3):
    pass_str=''
    
    for _ in range(num_chars):
        pass_str+=random.choice(chars).lower().capitalize()
    for _ in range(num_numbers):
        pass_str+=str(randint(0,9))
    for _ in range(num_special):
        pass_str+=choice(special_chars)
        return pass_str


#Password Strength 
def main():
    pass_str=create_password()
    strength,_=test(pass_str)

    print("\nPassword: %s"%pass_str)
    print("Strenth: %0.5f"%strength)

if __name__=='__main__':
    main()

