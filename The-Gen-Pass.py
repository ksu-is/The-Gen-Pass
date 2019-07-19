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
special_chars=['!','?']

#Password Strength 
def main():
    pass_str=create_password()
    strength,_=test(pass_str)
    print('\nPassword: %s'%pass_str)
    print('Strenth: %0.5'%strength)

if _name_=='_main_':
    main()

#Password generator function