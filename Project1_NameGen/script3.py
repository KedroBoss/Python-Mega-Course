import string, random

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letters = string.ascii_lowercase

letter_in2 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants 'l' for any letters: ")
letter_in1 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants 'l' for any letters: ")
letter_in3 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants 'l' for any letters: ")



def generator():
    if letter_in1=='v':
        letter1 = random.choice(vowels)
    elif letter_in1 =='c':
        letter1 = random.choice(consonants)
    elif letter_in1 == 'l':
        letter1 = random.choice(letters)
    else:
        letter1=letter_in1

    if letter_in2=='v':
        letter2 = random.choice(vowels)
    elif letter_in2 =='c':
        letter2 = random.choice(consonants)
    elif letter_in2 == 'l':
        letter2 = random.choice(letters)
    else:
        letter2=letter_in2

    if letter_in3=='v':
        letter3 = random.choice(vowels)
    elif letter_in3 =='c':
        letter3 = random.choice(consonants)
    elif letter_in3 == 'l':
        letter3 = random.choice(letters)
    else:
        letter3=letter_in3
    name = letter1+letter2+letter3
    return name

for i in range(11):
    print(generator())
