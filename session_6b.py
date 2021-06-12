# Fibonacci sequence part
from os import spawnl
import math

fibolist = [0, 1, 1]
while fibolist[-1] <= 10000:
    fibolist.append(fibolist[-1] + fibolist[-2])

checkfibonumber = lambda checklist: list(filter(lambda x: x in fibolist, checklist))
print("fibo number checker - ",checkfibonumber(
    [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Prints all the numbers which are a fibonacci number , should be 1,2,3,5,8

# Second part , odd even number addition, strip vowel from word , sigmoid function , encryption algorithm

# odd even number addition
final_result = lambda mylist1, mylist2: sum(list(filter((lambda x: x % 2 == 0), mylist1))) + sum(
    list(filter((lambda y: y % 2 == 1), mylist2)))
print("add even and odd numbers filtered - ",final_result([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8]))  # Should be 36 since 9 shouldn't be counted

# strip vowel from word
vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowel_conversion_function = lambda mystring: "".join(filter(lambda x: x not in vowel_list, list(mystring)))
print("Vowel removal - ",vowel_conversion_function("tsaiTSAI"))

# sigmoid function (I haven't learnt this in school so I'll just try to do what I can)
sigmoid_apply_to_list = lambda myintegerlist: list(map(lambda x: 1 / (1 + math.exp(-x)), myintegerlist))
print("sigmoid apply to list - ",sigmoid_apply_to_list([1, 2, 3, 4, 5]))

# Encryption algorithm

shifted_text_function = lambda mystring: "".join(
    map(lambda x: chr(ord(x) + 5) if ord(x) + 5 <= ord('z') else chr(ord('a') + 4 - (ord('z') - ord(x))),
        list(mystring)))
print("beta encryption - ",shifted_text_function(
    "abcdefghjiklmnopqrstuvwxyz"))  # Should return a nice string starting from f and ending with e

# Third part , profanity checking

with open("list.txt", "r") as f:  # Opens the list of bad word file
    bad_words = f.read().split()  # Stores it as a list for better comparison

# Callable which checks if certain banned words are present
check_paragraph_for_bad_words = lambda mypara: "Profanity words present" if list(
    filter((lambda x: x in bad_words), mypara.split())) else "Not present"
print("Bad words filter - ",check_paragraph_for_bad_words(
    "Oh shit this is a phrase"))  # Should print the True part since there is a word present

# Fourth part , reduce functions for adding even numbers,biggest character , adds every 3rd number in a list

#Add even numbers from a list
from functools import reduce

add_even_numbers_only=lambda my_even_number_addition_list: reduce(lambda x,y:x+y,filter(lambda z:z%2==0,my_even_number_addition_list))
print("add even numbers only - ",add_even_numbers_only([1,2,3,4,5,6])) #Output should be 12

#Biggest character

biggest_character_from_string=lambda my_character_string:reduce(lambda x,y:x if ord(x)>ord(y) else y,my_character_string)
print("biggest character from string - ",biggest_character_from_string("zabcgheriofjoasdo"))#Should return z as it is the largest unicode alphabet

#3rd number of list

third_number_from_list_addition=lambda list_of_numbers:reduce(lambda x,y:x+y,list_of_numbers[2::3])
print("Third number list addition - ",third_number_from_list_addition([1,2,3,4,5,6]))#Should return 9


# Random number plate generator
random_number_plates=[]
from string import ascii_uppercase
from functools import partial
import random
random_number_plates=[("KA"+("0"+str(random.randint(1,99)))[-2:]+random.choice(ascii_uppercase)+random.choice(ascii_uppercase)+str(random.randint(1000,9999))) for _ in range(15)]
#generator(random_number_plates)
print("Random KA number plates - ",random_number_plates)

#second part with partial
generator_improved=lambda number_plate_list,state,upper_limit_number:number_plate_list.append(("DL" if state=="DL" else "KA") + ("0" + str(random.randint(1, 99)))[-2:] + random.choice(ascii_uppercase) + random.choice(ascii_uppercase) + str(random.randint(1000, upper_limit_number)))
random_number_plates_improved=[]
generator_improved_partially=partial(generator_improved,random_number_plates_improved,"DL",9999)
generator_improved_partially()
print("Partial number plates - ",random_number_plates_improved)
