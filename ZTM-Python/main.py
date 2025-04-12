print("Ryan Woods")

name = input("What is your name?")
print(' hellllloooooo ' + name)









#Fundamental Data Types
int 2+4
float
bool
str
list 
tuple
set
dict

#Classes -> custom types

#Specialized Data Types

None


############ NUMBERS ############
#print(type(6))
#print(type(2-4))
#print(type(2*4))
#print(type(2/4))
#print(type(5.000001))
#print(type(0))
print(type(9.9+1.1))

print(2 ** 3)
print(5//4)
print(5%4)


############ MATH FUNCTIONS ############
print(round(3.1))
print(round(3.9))

print(abs(-99))


############ OPERATOR PRECEDENCE ############
# ()
# **
# * /
# + -
print(20-3*4)
print((20-3)+ 2 ** 2)

# EXERCISE
print((5 + 4) * 10 / 2)
#45
print(((5 + 4) * 10) / 2)
#45
print((5 + 4) * (10 / 2))
#45
print(5 + (4 * 10) / 2)
#25
print(5 + 4 * 10 // 2)
#25




############ VARIABLES ############
iq = 190
print(iq)





############ EXPRESSIONS VS STATEMENTS ############
iq = 100
user_ago = iq/5
#expression
iq/5
#statement
user_ago = iq/5
iq = 100




############ AUGMENTED ASSIGNMENT OPERATOR ############
some_value = 5
some_value += 2 #7
print(some_value)
some_value -= 2 #5
print(some_value)
some_value *= 2 #10
print(some_value)




############ STRINGS ############
type("Hello there!")

username = "Ryan W"
password = "secret"

long_string = '''
WOW
0 0
---
'''

print(long_string)

first_name = "Ryan"
last_name = "Woods"
full_name = first_name +  ' ' + last_name
print(full_name)




############ STRINGS CONCATENATION ############
print('Hello' + 'Ryan')




############ TYPE CONVERSION ############
print(str(100))
print(type(str(100)))
print(type(int(str(100))))


a = 100
b = int(a)
c = type(b)
print(c)





############ ESCAPE SEQUENCES ############
weather = "It's sunny"
weather = "It's \"kind of\" sunny"




############ FORMATTED STRINGS ############
'asdfasf'

name = 'Ryan'
age = 35

print('hi ' + name)
print('Hi ' + name + '. You are ' + str(age) + ' years old!')
# f at the beginning for a formatted string
print(f'Hi {name}. You are {age} years old!') #reccomended
print('Hi {}. You are {} years old!'.format('Annie', 31))
print('Hi {1}. You are {0} years old!'.format(name, age))
print('Hi {new_name}. You are {new_age} years old!'.format(new_name="Annie", new_age=31))





############ STRING INDEXES ############
selfish ='01234567'
         #01234567
print(selfish[0])
print(selfish[7])
# [start:stop]
print(selfish[0:2])
print(selfish[0:7])
# [start:stop:stepover]
print(selfish[0:8:1])







############ IMMUTABILITY ############
selfish ='01234567'
         #01234567
#selfish[start:stop:stepover]
selfish = selfish + 8
print(selfish)




############ BUILT IN FUNCTIONS AND METHODS ############
str()
int()
float()
type()
print()
greet = 'helloooooo'
print(greet[0:len(greet)])

quote = 'to be or not to be'
quote2 = quote.replace('be', 'me')
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be','me'))
print(quote)
print(quote2)










