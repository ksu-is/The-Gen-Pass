#Random password generating program named the Gen-Pass 

#import libraries first
#password meter will allow us to test the strenghth of the password
#We will use the passwordmeter test function to check strength as wella s tak advantage of it's advice
import passwordmeter
from passwordmeter import test
#This downloads thousands of words we can use in the generation of our passwords
from urllib.request import urlopen
from os.path import isfile
from random import choice, randint

if not isfile('words.txt'):
    print ('Downloading words.txt')
    url='https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
    with open('words.txt','w') as f:
        f.write(urlopen(url).read())

words=open('words.txt','r').read().split('\n')
#Add as many special characters as you want
special_chars=['!','?','$','#','&']

#Password generator function

#In the first for loop we are iterating for as many words as we want defaulting to a value of two, convert it to lower case
#and capitalize the first letter
#In the second for loop we will iterate for as many numbers as we want, randomly selecting from 0-9
#In the thrid loop we wil iterate for as many special characters as we want defaulting to just one of our options
def create_password(num_words=2,num_numbers=5,num_special=2):
    pass_str=''
    for _ in xrange(num_words):
        pass_str+=choice(words).lower().capitalize()
    for _ in xrange(num_numbers):
        pass_str+=str(randint(0,9))
    for _ in xrange(num_special):
        pass_str+=choice(special_chars)
        return pass_str


#Password Strength 
def main():
    pass_str=create_password()
    strength,_=test(pass_str)
    print('\nPassword: %s'%pass_str)
    print('Strenth: %0.5'%strength)

if __name__=='__main__':
    main()

