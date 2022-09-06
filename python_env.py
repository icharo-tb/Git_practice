from msilib.schema import RemoveRegistry
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

#--------------------------------------------------------------------------------------------------
# PYTHON RECURSIVE ALGORITHM
# Recursion is basicly calling the fuction inside the function
# Easy example would be factorial numbers:
    # This is a factorial: 4!, where exclamation means factorial of the number 4
        # This can be transalated to: 4 * 3 * 2 * 1 which is equal to 24
        # Also, this problem can be seen as 4 * 3!, and 3 can be seen as 3 * 2! and on and on
        # Important: factrorial for 1 and 0 are the following (ALWAYS!!)
            # 1! = 1
            # 0! = 1

# In the iterative function code what we want to do is an iterative loop that does the following:

        # def factorial(4):
            # factorial = 1
            # for x = 1 to 4:
                # factorial = factorial * x
    
    # So our code sets a factorial to 1, and its going to loop and multiply x by our number

    # Whereas on using recursion, our code will complete factorial of 1! until the number we asked for
        # So the code is basicly reading and returning until it completes the loop
    # So, for a recursive algorithm it would look like this:

        # def factorial(n):
            # if n < 2:
                # return 1
            # else:
                # return n * factorial(n - 1)
    
    # The first condition is our debugging line, in case n is less than 2 just return 1 cause that is the result of factorial for 1 and 0
    # Otherwise, return n and multiply it by (n - 1) times
        # This works by the logic that, if n = 5 we are gonna multiply it by 4 as 5! is the same as 5 * 4!
            # And here is where the loop starts as it will do:
                # 5 * 4!
                    # 4 * 3!
                        # 3 * 2!
                            # 2 * 1!
                                # 1 * 0!
                                    # And then it will return the result (120 in this case)

def recursive_factorial(n):
    if n < 2:
        return 1
    elif n < 0:
        return -1
    else:
        return n * recursive_factorial(n-1)
pass

def iterative_factorial(n):
    if n < 0:
        return -1
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        return factorial
pass    

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

#--------------------------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------------------------

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

# =================================================================================================
# STRING OPS

def split(fruit):
    return[letter for letter in fruit]

fruit = 'banana'
for word in fruit.upper():
    words = split(fruit)
    count = words
    print(word)
print('Total of characters:', len(fruit))

up = fruit.upper()
index = 0
while index < len(up):
    letter = up[index]
    print(index, letter)
    index = index + 1

for n in 'banana':
    print(n)

count = 0
for letter in up:
    if letter == 'A':
        count = count + 1
print(count)

# =================================================================================================
# INTERMEDIATE STRING OPS

s = 'Monty Python'
print('String lenght:', len(s))
print(s[0:4])
print(s[3:6])
print(s[5:13])
# We can slice string by defining from which position we want to start and which one we want to end at

bob = 'Hello Bob'
zap = bob.lower()
print(zap)
try:
    print(bob.lower())
except:
    print('Error')
print('Hello'.lower())

lat = 'Lorem Ipsum Dolor'
print(lat.center(35))
print(lat.center(35).casefold())
print(lat.isalpha())
print(lat.isascii())
print(type(lat))
print(dir(lat)) # this will show every possible operation over the object/string

# str.capitalize(), str.center(width[, fillchar]), str.endswith(suffix[, start[, end]])
# str.find(sub[, start[, end]]), str.lstrip([chars]), str.replace(old, new[, count])
# str.lower(), str.rstrip([chars]), str.strip([chars]), str.upper()

st2 = 'Hello World'
rep = st2.replace('Hello', 'Hi')
print(rep)

st3 = 'banana'
pos = st3.find('na')
print(pos)
print(st3.find('z'))


st4 = '  Bob  '
l = st4.lstrip()
r = st4.rstrip()
strip = st4.strip()
print(st4)
print(l)
print(r)
print(strip)
# lstrip, rstrip and strip are string commands that help us drop spaces
# lstrip will drop left spaces, rstrip will drop rspaces and strip will drop both sides spaces

st5 = 'Please, give me water'
print(st5.startswith('Please'))
print(st5.startswith('P'))
print(st5.startswith('p'))

data = 'From stephen.marquard@utc.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos + 1 : sppos]
print(host)

word = "bananana"
i = word.find("na")
print(i)

# =================================================================================================
# FILE READING WITH PYTHON

text = open('file1.txt', 'r')
print(text)

hw = 'Hello\nWorld!'
print(hw)
# \n means newline, anytime we use this sytax it will display things on a new line 
# in this particular example it shows Hello on a line and World! on another line
# \n will also count on the variable content as an element 
print(len(hw))

def newline(text):
    for line in text:
        line = text.split()

text = open('file1.txt', 'r')
count = 0
for line in text:
    count = count + 1
    print(line, 'Line count:' , count)

text = open('file1.txt', 'r')
inp = text.read()
print(len(inp))

text = open('file1.txt', 'r')
for line in text:
    line = line.splitlines()
    print(line)

text = open('file1.txt', 'r')
for line in text:
    print(line)

text = open('file1.txt', 'r')
for line in text:
    rline = line.rstrip()
    if rline.startswith('One'):
        print(rline)
    
text = open('file1.txt', 'r')
for line in text:
    rline = line.rstrip()
    if not rline.startswith('One'):
        continue
    print(rline)
# we can use loops to iterate over the text to find the information we need

def text_gen(your_text):
    try:
        text.open(your_text)
    except:
        print('File not found', your_text)
        quit()
    for line in your_text:
        print(your_text)

your_text = input('Enter your file name:')
res = text_gen(your_text)
print(res)

# Exercise 1: Write a program to read through a file and print the contents of the file 
# (line by line) all in upper case. (mbox file)

text = open('mbox-short.txt', 'r')
for line in text:
    line = line.rstrip()
    up = line.upper()
    print(up)

#--------------------------------------------------------------------------------------------------
# EXTRA STUFF

def coco(coquito = []):
    coquito.append(['Coconut'])
    return coquito

coco_loco = coco()
print(coco_loco)
# this will append a new memory space everytime we execute it

def coco_noice(coconutito = 0):
    coconutito += 1
    return coconutito

print(coco_noice())

#--------------------------------------------------------------------------------------------------
# PYTHON LISTS

fruit = 'BANANA'
low = fruit.lower()
print(low)

num = [1, 4, 45, 67, 23]
print(num)
num[2] = 32
print(num)
# while numbers are able to change easily, strings are all inmutable, which means that they cannot be changed

friends = ['Joseph', 'Glenn', 'Michael', 'Ana']

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year', friend + '!')

stuff = list()
stuff.append('Red')
stuff.append('Blue')
stuff.append(99)
print(stuff)
stuff.remove(99)
print(stuff)
stuff.sort()
print(stuff)

nums = [1, 2, 45, 56, 34, 21, 12, 67]
print(nums)
print('Lenght:', len(nums))
print('Max:', max(nums))
print('Min:', min(nums))
print('Sum:', sum(nums))
print('Operation:', sum(nums) / len(nums))

numlist = list()
while True:
    inp = input('Enter a number to add to the list:')
    if inp == 'done':
        break
    finp = float(inp)
    numlist.append(finp)
aver = sum(numlist) / len(numlist)
print(numlist)
print('Average:', aver)

total = 0
count = 0
while True:
    inp = input('Enter a number to add to the list:')
    if inp == 'done':
        break
    finp = float(inp)
    total = total + finp
    count = count + 1
op = total / count
print(total)
print('Average:', op)

# =================================================================================================
# STRINGS AND LISTS

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
mailsp = pieces[1].split('-')
m = mailsp[1]
parts = pieces[3].split('-')
n = parts[1]
print(pieces)
print(mailsp)
print(m)
print(parts)
print(n)
# split let us separate a word either on list elements or use to substract a character
# in this case, - is being substituted by an space

colon = 'Hey;,;how;are;you;doing;?'
sep = colon.split(';')
print(sep)

fhand = open('mbox-short.txt', 'r')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1:
        continue
    # guradian code line
    elif words[0] != 'From':
        continue
    print(words[2])

#--------------------------------------------------------------------------------------------------
# BONUS: FIBONACCI SEQUENCE
# The Fibonacci sequence is based on the add of a num by its previous. Therefore, 1+1 = 2, 2+1 = 3...

num = int(input('Term lenght:'))

n1, n2 = 0, 1
count = 0

if num <= 0:
    print('Enter a positive integer')
elif num == 1:
    print(f'Fibonacci sequence upto {num} term:')
    print(n1)
else:
    print('Fibonacci sequence:')
    try:
        while count < num:
            print(n1)
            res = n1 + n2
            n1 = n2
            n2 = res
            count += 1
    except:
        print('Error')

# BONUS 2: 1-LINE FIBONACCI SEQUENCE CODE (Lambda ops)

fibonacci = lambda x: x if x <= 1 else fibonacci(x-1) + fibonacci(x-2)
# lambda can take an argument, called 'x' in this case

print([fibonacci(i) for i in range(5)])

# Fibonacci Formula:
    # Fn = (Fn-1) + (Fn-2)

def fibonacci_seq(n):
    if n < 0:
        return f'Error'
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_seq(n-1) + fibonacci_seq(n-2)
pass

print(fibonacci_seq(5))


# check later how to construct this function

#--------------------------------------------------------------------------------------------------
# PYTHON DICTIONARIES

bag = dict()
bag['Towel'] = 1
bag['Pencil'] = 3
print(bag)
bag['Candy'] = 3
bag['Candy'] = bag['Candy'] + 2
print(bag['Candy'])
print(bag)

purse = {'money': 12, 'lipstick': 3, 'cologne': 32}
print(purse)
# dictionaries work with a primary key and then a value (key: value)
# this let us call an element easily inside the dictionary

new_dict = []
x = str(input())

for thing in new_dict:
    new_dict.append(new_dict[x])
print(new_dict) 
# doesn't work with input as expected

# =================================================================================================
# COMMON DICTIONARIES APPLICATIONS

# COUNTING
my_dict = {'allen': 3, 'joshua': 2, 'benjamin': 5, 'charles': 1}
print(my_dict.get('allen', 5))

# HISTOGRAM
myDict = dict()
names = ['allen', 'barry', 'barry', 'josh', 'allen',  'ken', 'william', 'allen', 'daniel']
for name in names:
    if name not in myDict:
        myDict[name] = 1
    else:
        myDict[name] = myDict[name] + 1
print(myDict)

# .GET METHOD
myDict = dict()
names = ['allen', 'barry', 'barry', 'josh', 'allen',  'ken', 'william', 'allen', 'daniel']
for name in names:
    myDict[name] = myDict.get(name, 0) + 1
    # 0 will be pur default value
print(myDict)

# =================================================================================================
# DICTIONARIES AND LOOPS

# KEY COUNT
counts = {'allen': 1, 'joshua': 42, 'benjamin': 6, 'charles': 120}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
# Prints out keys (K/V)
print(counts.keys())
# Prints out values
print(counts.values())
# Prints out all items in the dictionary
print(counts.items())
# Prints out data type in case it exists
print(counts.type())

# WORDS COUNT
text = dict()
inp = input('Enter your text:')

words_sp = inp.split()
print('Words', words_sp)

for word in words_sp:
    text[word] = text.get(word, 0) + 1
    total = len(words_sp) 
    # use len() to get the total of words
    # otherwise, use count() specifying a key to count the amount of that element

print('Count', text)
print('Total', total)

# --BONUS-- TWO ITERATION VARIABLES
counts = {'allen': 1, 'joshua': 42, 'benjamin': 6, 'charles': 120}
for a,b in counts.items():
    print(a,b)

# EXAMPLE:
inp = input('Enter text file:')

try:
    handle = open(inp, 'r')
except Exception as e:
    print('Error' + str(e))

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

bigCount = None
bigWord = None
for word,count in counts.items():
    if bigCount is None or count > bigCount:
        bigCount = count
        bigWord = word
print(bigCount)
print(bigWord)

#--------------------------------------------------------------------------------------------------
# BONUS: JACCARD SIMILARITY
# It is mainly used to compare betwwen two sets and calculate it's similarity ratio

def jaccard_similarity(A, B):
    # This will find the common elements, that is, the intersection between the sets
    nominator = A.intersection(B)

    # We will find the union between the sets
    denominator = A.union(B)

    # Now for the ratio
    similarity_ratio = len(nominator)/len(denominator)
    return similarity_ratio

A = {1,2,3,5,7}
B = {1,2,4,8,9}

print(jaccard_similarity(A, B))

# =================================================================================================
# BONUS: 2nd GRADE EQUATION

# (-b+-((b**2) - (4 * a) * c)**2) / 2 * a | It will need some formula changes
# x**2 - 5x + 6 = 0

a = 1
b = -5
c = 6

# It can have int or work as a float
secGrade_eq_pos = int((-b + ((b**2) - (4 * a) * c)**2) / 2 * a)
secGrade_eq_neg = int((-b - ((b**2) - (4 * a) * c)**2) / 2 * a)

print(f'The first result is {secGrade_eq_pos} and the second result is {secGrade_eq_neg}')

# DISCRIMINANT aka DELTA
# print('\u0394') DISCRIMINANT / DELTA unicode

# When using discriminant:
    # If DISC > 0 --> 2 different real solutions
    # If DISC = 0 --> 2 equal real solutions
    # If DISC < 0 --> 2 no real solutions, just 2 complex solutions

# 3x**2 - 5x + 1 = 0

a = 3
b = -5
c = 1

discGrade_eq = int((b**2) - (4 * a) * c)

print(f'DISCRIMINANT \u0394 is equal to {discGrade_eq}')

if discGrade_eq > 0:
    print('Equation has 2 different real solutions')
elif discGrade_eq == 0:
    print('Equation has 2 equal real solutions')
elif discGrade_eq < 0:
    print('Equation has no real solutions, it has 2 complex solutions')

#--------------------------------------------------------------------------------------------------
# TUPLE COLLECTIONS

# Tuples are similar to lists, but, they are inmutable
x = (1,2,9)
x[2] = 6 # this will blow up cause a tuple cannot be modified
print(x)

x = tuple()
print(dir(x))

(x, y) = (5, 'fred')
print(y)

tdict = {'allen': 1, 'joshua': 42, 'benjamin': 6, 'charles': 120}
for (x, y) in tdict.items():
    print(x, y)
# We use .items() in order to get our dictionary turned into a tuple 

tup = tdict.items()
print('\n', tup)

#--------------------------------------------------------------------------------------------------
# COMPARING AND SORTING TUPLES

tdict = {'allen': 1, 'joshua': 42, 'benjamin': 6, 'charles': 120}
#tup = tdict.items()
#print(sorted(tup))

temp = list()
for k, v in tdict.items():
    temp.append((v, k))
print(temp)

temp = sorted(temp, reverse = True)
print(temp)

# Word counting applying tuples

f = open('mbox-short.txt')
counts = dict()
for line in f:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for k, v in counts.items():
    tup = (k, v)
    lst.append(tup)

lst = sorted(lst, reverse = True)

for k, v in lst[:10]:
    print(k, v)

tdict = {'allen': 1, 'joshua': 42, 'benjamin': 6, 'charles': 120}
print(sorted([(v, k) for k, v in tdict.items()], reverse = True))
# Important to remember that the order of k,v variables changes the displayed order

#--------------------------------------------------------------------------------------------------
# PYTHON REGULAR EXPRESSIONS

# Regular expressions are a kind of language itself, its really powerful
# to use the we will import re


mail_t = 'His e-mail is q-lar@freecodecamp.org'
mail_ts = mail_t.rstrip()
if mail_ts.find('@'):
    print('Its a mail')

# We can do the exact same operation using re.search() instead

import re

mail_t = 'His e-mail is q-lar@freecodecamp.org'
mail_ts = mail_t.rstrip()
if re.search('@', mail_ts):
    print('Its a mail')

# re.search() can also substitute .startswith()

#--------------------------------------------------------------------------------------------------
# PYTHON REGULAR EXPRESSIONS: MATCHING AND EXTRACTING DATA

import re

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x) # [0-9] means one single digit from 0 to 9, when we use the + we are
# indicating to find one or more digit strings
print(y)
y = re.findall('[a-u]+', x) # works the same with letters
print(y)

# GREEDY MATCHING
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x) 
# ^F indicates that starts with F
# .+ indicates that it has one or more characters (this is GREEDY)
# : indicates the last character in the match
print(y)

# NON-GREEDY MATCHING
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x) 
# ^F indicates that starts with F
# .+? indicates that it has one or more characters but not greedy (? similar to !=)
# : indicates the last character in the match
print(y)

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
# \S+ means: at least one non-whitespace character
# \\S+@\\S+ means: at least 2 non-whitespaces before, followed by an @ 
    # and ending with at least 2 non-whitespaces
print(lst)

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('^A(\\S+@\\S+)', s)
print(lst)

#--------------------------------------------------------------------------------------------------
# PYTHON REGULAR EXPRESSION: PRACTICAL APLICATIONS

mail_str = 'From stephen.marques@gmail.com Sat Jan  5 09:15:45 2022'
words = mail_str.split()
email_ = words[1]
lst = email_.split('@')
print(lst[1])

import re
mail_str = 'From stephen.marques@gmail.com  and john.skittle@gmail.com Sat Jan  5 09:15:45 2022'
y = re.findall('@([^ ]*)', mail_str)
# [^ ] will match non-blank character
# * matches many of them 
print(y)

import re
mail_str = 'From stephen.marques@gmail.com  and john.skittle@gmail.com Sat Jan  5 09:15:45 2022'
y = re.findall('[^ ]*@', mail_str)
print(y)

import re
mail_str = 'From stephen.marques@gmail.com  and john.skittle@gmail.com Sat Jan  5 09:15:45 2022'
y = re.findall('^From.*@([^ ]*)', mail_str)
print(y)

import re
with open(r'C:\Users\DANIEL\workspace\gitwork\mbox-short.txt', 'r') as file:
    for line in file:
        print(line)
        numlist = list()
        line = line.rstrip()
        stuff = re.findall('^X-DSPAM-Confidence:([0-9.]+)', line)
        if len(stuff) !=1:
            continue
        num = float(stuff[1])
        numlist.append(num)
    print(stuff)

import re
x = 'We just received $10.00'
y = re.findall('\$[0-9.]+', x)
# \$ matches a real dollar sign
print(y)

#--------------------------------------------------------------------------------------------------
# PYTHON NETWORKING

# TCP Architecture: Transport Control Protocol works by connecting P2P your pc with a server sending packages back and forth
    # In programming those connection points are called Sockets
    # We will make use of Ports: which are endpoints for the software connection
        # Common TCP Ports:
            # HTTPS(443) - Secure
            # HTTP(80)
            # SSH(22) - Secure Login
            # DNS(53) - Domain Name

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET will create a socket connection to internet ports
mysock.connect(('freecodecamp.org', 80))

# A URL have three main elemnts:
    # EX: https://www.dr-chuck.com/page.htm
        # Protocol: https://
        # Host: www.dr-chuck.com
        # Document: page.htm

# WEB BROWSER

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# \r its a 'carriage return' while \n its a 'line break'
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()
# This will help us decode the information we are getting from the web so Python can understand it
# The process here is a give and receive:
    # First of all we are sending the information based on Unicode (due to Python 3)
    # We encode() into UTF-8 and send() it to the socket connected to the network
    # Then we recover with recv() all the info in UTF-8
    # Finally we decode() the information back to Unicode so Python 3 can understand it
        # Extra code stuff:
            # cmd are basicly the bytes we are sending

# TEXT PROCESSING
# ASCII: American Standard Code for Information Interchange
    # Unicode: billions of characters
        # UTF = Unicode Transformation Format
            # UTF-8: 1-4 bytes
            # UTF-16: 2 bytes
            # UTF-32: 4 bytes

# In python, the function ord() will return the ASCII value of a character
print(ord('A'))

# We can retrieve information from a url using urllib within a few lines of code
# We can do almost every kind of operation just by requesting the url information we want
import urllib.request, urllib.parse, urllib.error

linkLine = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in linkLine:
    print(line.decode().rstrip())

count = {}

for line in linkLine:
    words = line.decode().rstrip()
    print(words)
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)

# PYTHON WEB SCRAPER
# What is web scraping?
    # Web scraping is when a program or script pretends to be a browser and retrieves web pages
        # It can retrieve any kind of information and when it finishes it looks for more web pages
    # Other methods are the called Web Crawlers, where we use trackers or spiders to search information

# Why Scrape?
    # Pull Data
    # Get your own data from any source that has no native export capability
    # Monitor sites for new info
    # Spider/Track the web in order to make a database for a search engine

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Lets ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://dr-chuck.com/page1.htm'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a') # a = anchor tags
for tag in tags:
    print(tag.get('href', None))

import requests

URL = 'http://dr-chuck.com/page1.htm'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
# User-Agent headers can be found here: https://deviceatlas.com/blog/list-of-user-agent-strings
req = requests.get(url=URL, headers=headers)
print(req.content)

# WEB SERVICES
# Most common data sending formats: XML and JSON
    # XML:
        # XML = eXtensible Markup Language
            # XML Terminology: Tags, Attributes, Serialize/De-serialize
        # Basic XML structure:
            # <person> -> Starter tag
            #   <name>Chuck</name>
            #   <phone type="intl">+1 734 303 4456</phone> -> Normal tag with an attribute type
            #   <email hide="yes"/> -> Self closing tag with an attribute hide
            # </person>
        # XML Schema:
            # They are several guidelines that sets a XML as a complete readable format
            # XSD(WS3 Schema specifications for XML files):
                # xs:Type
                # xs:element
                # xs:sequence
                # When using time data types, XML Schema will store it as Universal time:
                    # 2022-05-03T09:37:24Z :
                        # 2022-05-03 is the year-month-day
                        # 09:37:24 is the time of the day
                        # Z corresponds to the time zone(where Z is for local)
                            # Usually we see UTC or GMT
import xml.etree.ElementTree as ET

data =  '''<person> 
    <name>Chuck</name>
    <phone type="intl">+1 734 303 4456</phone> 
    <email hide="yes"/> 
</person>'''

tree = ET.fromstring(data)
print(f'Name: {tree.find("name").text}')
print(f"Phone Number: {tree.find('phone').text}")
print(f'Attr: {tree.find("email").get("hide")}')

import xml.etree.ElementTree as ET

data2 = '''<data>
    <users>
        <user x="2">
            <id>001a</id>
            <name>Josh</name>
        </user>
         <user x="7">
            <id>002a</id>
            <name>Carl</name>
        </user>
    </users>
</data>'''

stuff = ET.fromstring(data2)
lst = stuff.findall('users/user')
print(f'User count: {len(lst)}\n\nUsers:')

for i in lst:
    print('-'*10)
    print(f"ID: {i.find('id').text}")
    print(f"Name: {i.find('name').text}")
    print(f"Attr: {i.get('x')}")
    print('-'*10)

    # JSON:
        # JSON: JavaScript Object Notation
            # It comes from JS syntax
            # Data is represented as nested lists and dictionaries

import json

data = '''{
    "name": "Chuck",
    "phone": {
        "type": "intl",
        "number": "+1 456 783 9224"
    },
    "email": {
        "hide": "yes"
    }
}'''

info = json.loads(data)
print(f"Name: {info['name']}")
print(f"Hide: {info['email']['hide']}")
# This is a classic and easy JSON file, since everything is stored in dictionaries it makes searches easier

import json

data = '''[
    {
        "id": "002",
        "age": "31",
        "name": "Chuck",
        "email": {
            "hide": "yes"
        }
    },
    {
        "id": "013",
        "age": "25",
        "name": "Elysa",
        "email": {
            "hide": "no",
            "mail": "elysavangut@gmail.com"
        }
    }
]'''

info = json.loads(data)
print(f"User count: {len(info)}")
# Now, when JSON files are stored as lists, we need to iterate over every element to make efficient searches
for item in info:
    print('-'*10)
    print(f"ID: {item['id']}")
    print(f"Name: {item['name']}")
    print(f"Age: {item['age']}")
    print(f"Hide E-mail: {item['email']['hide']}")
    if 'mail' in item['email']: # Find an element "in" a list, so we search the term "mail" inside the "email" dict of item
        print(f"E-mail: {item['email']['mail']}")
    print('-'*10)

#---------------------------------------------------
# FIND MAX NUMBER IN SEQUENCE

# Find the max number on a sequence of 3 numbers that added consecutively results in x
    # x = 60
        # expected output: 19 + 20 + 21 = 60

# x = 60
# mid_seq = x//2 (3 number then // 3)
    # We use here int division //
# min_seq = mid_seq - 1
# max_seq = mid_seq + 1

def max_number_seq(x):
    nl = '\n'

    mid_seq = x//3
    min_seq = mid_seq - 1
    max_seq = mid_seq + 1

    return f"{min_seq} + {mid_seq} + {max_seq} = {x}{nl}The max number is: {max_seq}"
pass

print(max_number_seq(60))

#---------------------------------------------------
# SOA (Service Oriented Approach)
# It is a apporach to solve a complex application problem where data is not present in one computer system only
    # Data has spread out over the internet

# APIs
# API stands out for Application Program Interface
    # An API help us by specifying an interface and controling the behaviour of ebery object in that interface
    # Documentation is important to understand others APIs workflow

import requests
import json

# Needs API Key
url = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    par = {'address': address}
    response = requests.get(url, params=par)

    print(f'Retrieving {url}')
    data = response.text
    print(f'Retrieved {len(data)} characters')

    try:
        js = response.json()
        print(js)
    except:
        js = None

# response.content() -> Return the raw bytes of the data payload
# response.text() -> Return a string representation of the data payload
# response.json() -> This method is convenient when the API returns JSON

# Some APIs use an OAuth to make sure you have a valid key to make the proper connection with the API

#---------------------------------------------------
# PYTHON OBJECTS (CLASS)

#------------------------------------------------
# USUAL CLASS STATEMENT:
class Chalkboard:
    def __init__(self, lenght, height, name, color):
        self.lenght = lenght
        self.height = height
        self.name = name
        self.color = color

chalkb = Chalkboard(50,25,'chalky-2','white')
print(chalkb)

# DATACLASS STATEMENT(shorter):
from dataclasses import dataclass

@dataclass
class Chalkboard:
    lenght: int
    height: int
    name: str
    color: str

chalkb = Chalkboard(50,25,'chalky-3','black')
print(repr(chalkb))

# MULTIPLE CLASS:

# Some classes can be called multiple times, but you can always DRY(Don't Repeat Yourself) them:

class TestMath:
    def __init__(self):
        self.x = 10
        self.y = 20
        
    # From here we could make other fucntions to add, substract, etc. 
    # and call self.x = 10 everytime, but, we can also just call self.x

    def test_add(self):
        return self.x + self.y
    def test_sub(self):
        return self.x - self.y
    def test_div(self):
        return self.x // self.y
    def test_multiply(self):
        return self.x * self.y
#------------------------------------------------