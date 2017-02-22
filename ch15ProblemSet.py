'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (7pts) Write code which finds and prints the longest word in the provided dictionary.
# If there are more than one longest word, print them all.
# Make a list and add words to them based on length
print("Problem #1")
import re
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

dictionary_list = []
file = open("dictionary.txt", "r")
for line in file:
    words = split_line(line)
    for word in words:
        dictionary_list.append(word)

long_words = []
longest_words = []
file_length = (len(dictionary_list))
file_length = int(file_length)

dictionary_file = open("dictionary.txt")
number = 0
long_word = ""
for word in dictionary_file:
     if len(word) > number:
         number = len(word)
         long_word = word

print("The length of the longest word is" , number , "letters.")
print("The longest word is:", long_word)
file.close()

#2.  (10pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"
print("Problem #2")

file = open("AliceInWonderland.txt", "r")
alice = []
for line in file:
    words = split_line(line)
    for word in words:
        alice.append(word.lower())
print("There are", (len(alice)), "words in 'Alice In Wonderland'.")

# make an algorithm to find the average length
tracking = 0
for item in range(len(alice)):
    tracking += len(alice[item])

average = tracking / len(alice)
average = round(average, 2)
print("The average number of letters in the words in 'Alice In Wonderland' is", average ,"letters.")
file.close()


##### CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS #####
print("\nCHOOSE")
#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?
# use .upper and .lower



for items in alice:
    number = 0
    for words in range(len(alice)):
        if alice[words].lower() == str("Cheshire").upper():
            number += 1
print(number)


### OR ###


#3  (13pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"
print("\nProblem #3")
'''
seven_let_list = []

for item in word_number:
    individual = (len(item))
    if individual == 7:
        individual = item
        seven_let_list.append(individual)
print(seven_let_list)


for item in word_number:
    individual = (len(item))
    if len(item) == 7:
        for i in len(seven_let_list):
            if item == seven_let_list[item][0]:
                seven_let_list[i][1] += 1
        else:
            seven_let_list.append([item, 1])
print(seven_let_list)


sevens = []
for word in word_number:
    if len(word) == 7:
        for i in len(int(sevens)):
            if word == sevens[i][0]:
                sevens[i][1] += 1
        else:
            sevens.append([word, 1])
    print(sevens)

frequent = []
for item in seven_let_list:
    wordy = split_line(item)
    for word in wordy:
        frequent.append(word)
print(frequent)
'''
# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".
# Make a list.  You can substitute this for any of the above problems.
