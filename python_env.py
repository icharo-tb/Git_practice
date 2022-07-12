from unittest import result

from numpy import average


width = 15
height = 12.0
print(height/3)

x = 1 + (2 ** 3 / 4) * 5
print(x)

text = 'hello ' +  'there'
print(text)

t2 = 'hello ' + 'there'
num = 1

conv = str(num)

print(t2, num)
print('text type is:', type(t2))
print('num type is:', type(num))

t3 = 'Hello ' + 'World'
num2 = 2022

print(f'{t3} {(23 + (num2 ** 3) / 5 * 30)}') # f-strings

num3 = 83
print(f'¿Es par? {True if num3%2==0 else False}') # {True if num3%2==0 else False} operaciones booleanas

author = 'william shakespeare'
print(f'Macbeth was written by {author.title()}.')


def option(o):
    if o%2==0:
        return 'Learn Python'
    else:
        return 'Learn JavaScript'

# o = input()

print(f'¿What should I learn, Python?. {option(34)}')

# Write a program to prompt the user for hours and rate per hour using input to compute the gross pay
# Use 35h and a rate of 2.75 per hour to test the program (result = 96.25)
# Use input() to read a string and float() to convert the string to a number

hrs = input('Enter hours: ')
rate = input('Enter your rate: ')
res = float(hrs) * float(rate)

print(f'Your total hours are {hrs} and your gross pay rate is {res}.')

# try conditional structure
# used to surround dangerous sections of code without risking the rest
# try + except

name = 'Bob McCartney'
try:
    namestr = int(name)
except:
    namestr = 'Error'
print('First: ', namestr)

# if the program fails, which is what happends here since we cannot convert a name into an integer, the program will drop directly to the except clause


num4 = '123'
try:
    nstr = int(num4)
except:
    nstr = 'Error'
print('Second: ', nstr)

# on the other hand, if the program is able to complete the task it will run the try result
# try clauses are similar to if else but it wont put our program on the risk of being stopped by an error

astr = 'Michael'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = 'Error'
print('Done: ', istr)

astr = 'Michael'
try:
    print('Hello')
    print('There')
    istr = int(astr)
except:
    istr = 'Error'
print('Done: ', istr)

# a try clause can also have multiple variables and operations inside

rawstr = input('Enter your number:')
try:
    turn = int(rawstr)
except:
    turn = 'Error'

if turn > 0:
    print('Nice work!')
else:
    print('Not a number')

# =================================================================================================

temp = "5 degrees"
cel = 0
try:
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    fahr = 'Error'
    print('Error')

# =================================================================================================

hrs = input('Enter hours: ')
rate = input('Enter your rate: ')
try:
    fhrs = float(hrs)
    frate = float(rate)
    if(fhrs > 40):
        #print('Overtime')
        reg = fhrs * frate
        otp = (fhrs - 40.0) * (frate * 0.5)
        res = reg + otp
    else:
        #print('Regular')
        res = fhrs * frate
    
    print(f'Your total hours are {hrs} and your gross pay rate is {res}.')
except:
    print('Error, enter numeric input.')

def greeting_recognize(name):
    name.split()
    if name.isdigit():
        return 'Type a name'
    elif name.isalpha():
        return 'Hello ' + name + '!'
    
name = 'Bob Sinclair'
greet = greeting_recognize(name)

def greeting(name):
    return 'Hello ' + name + '!'

name = input()
greet = greeting(name)
print(greet)

# def function_name(argument): argument will help us define what the fucntion has to look forward to work 
# in this case, the def is searching for our name input, so everytime you set a name as an input
# the fucntion will apply the fucntion 'greeting' to it

# =================================================================================================

def payment(hours, rate):
    try:
        fhrs = float(hours)
        frte = float(rate)
        if fhrs > 40:
            reg = fhrs * frte
            otp = (fhrs - 40.0) * (frte * 0.5)
            pay = reg + otp
        else:
            pay = fhrs * frte
    except:
        return 'Error'
    return pay

hours = input('Enter hours: ')
rate = input('Enter your rate: ')

res = payment(hours, rate)

print(f'Your hours are {hours}, your rate is {rate} and your payment is {res}.')

# =================================================================================================
# Number guesser with WHILE LOOP

import random
import math
from random import randint

num_low = int(input('Enter lowest number: '))
num_high = int(input('Enter highest numer: '))


ran_num = random.randint(num_low, num_high)
print('\n\tYou have only', round(math.log(num_high - num_low + 1, 2)), ' chances to guess the number!\n')

count = 0

while count < math.log(num_high - num_low + 1, 2):
    count += 1
    guess = int(input('Make your guess: '))

    if ran_num == guess:
        print('Congratulations! You did it in ', count, ' tries')
        break
    elif ran_num < guess:
        print('Too high!')
    elif ran_num > guess:
        print('Too small')
    else:
        print('Error')

if count >= math.log(num_high - num_low + 1, 2):
    print('\nThe number is %d' % ran_num)
    print('\tBetter luck next time!')

# =================================================================================================

n = 0

while True:
    if n == 3:
        break
    print(n)
    n = n + 1

# =================================================================================================
# WHILE LOOPS

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done')

# continue statement will execute the next condition once the first one is done
import numpy
from numpy import average

user_num = 0
count = 0
total = 0.0

while True:
    sel = input('Enter a number or done: ')
    if sel == 'done':
        break
    try:
        fsel = float(sel)
        user_num = user_num + 1
        total = total + fsel
        count += 1
        print('Your number: ', fsel)
    except:
        print('Invalid data')
        continue

print('Count:', count, '||', 'Last number added:', fsel, '||', 'Total average:', total)
print('LOOP COMPLETED')


# =================================================================================================

import sys

if sys.version_info.major == 2:
    user = print('Hey') # raw_input('Username: ')
elif sys.version_info.major == 3:
    user = input('Username')

# =================================================================================================
# FOR LOOPS

friends = ['Joseph', 'Charles', 'Rita']
for friend in friends:
    print('Happy New Year', friend + '!')
print('Done')

for i in [2,1,5]:
    print(i)

# =================================================================================================

smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15, 0]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

# if we use break on this loop it will cause a fail since it will only read the first
# number as the smallest one

# =================================================================================================
# LOOP COUNTING AND OTHER OPS

val = 0
print('Before', val)
for i in [3, 5, 89, 32, 24, 78]:
    val = val + 1 
    print(val, i)
print('After', val)
# normal adding to val variable

val = 0
print('Before', val)
for i in [3, 5, 89, 32, 24, 78]:
    val = val + i 
    print(val, i)
print('After', val)
# adding the i value to val variable

for value in [3, 5, 89, 32, 24, 78]:
    if value > 20:
        print('Large number')
# we set a condition that once is done it will print x-result

val = 0
print('Before', val)
for i in [3, 5, 89, 32, 24, 78]:
    val = val - i 
    print(val, i)
print('After', val)
# same as adding but with a substract

found = False
print('Before', found)
for value in [34, 67, 2, 90, 3, 73, 82]:
    if value == 3:
        found = True
        break
    print(found, value)
print('After', found)
# Boolean ops works a bit different, first of all we are indicating that our found variable is False
# then we set our condition on the loop, and is that, when the value on our list matches 3, then found will turn True
# they way the boolean works is that every print will be false until the condition is met and the boolean variable turns to True
# that is why our result will be printed as False until it finds a 3 and afterwards it starts printing true values

largest = -1
print('Before', largest)
for num in [9, 34, 23, 65, 105, 1024, 92]:
    if num > largest:
        largest = num
    print(largest, num)
print('After', largest)

largest = None
print('Before', largest)
for num in [9, 34, 23, 65, 105, 1024, 92, 1, 0]:
    if largest is None or num < largest:
        largest = num
    print(largest, num)
print('After', largest)