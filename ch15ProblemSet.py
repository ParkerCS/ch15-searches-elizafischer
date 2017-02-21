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
#print("Dictionary List:" , dictionary_list)

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
        #longest_words.append(word)
        #number = len(word)

print("The length of the longest word is" , number , "letters")
print("The longest word is: ", long_word)
file.close()
'''
import re
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

dictionary_list = []
file = open("dictionary.txt", "r")
for line in file:
    words = split_line(line)
    for word in words:
        #print(word)
        dictionary_list.append(word)
print("Dictionary List:" , dictionary_list)


long_words = []
longest_words = []
file_length = (len(dictionary_list))
file_length = int(file_length)


for word in range(file_length):
    if len(word) >= 10:
        long_words.append(word)
        print("Long Word List:", long_words)
file.close()
##################################
print("SPACE")
longest_len = 0
longest_word = ""
for word in dictionary_file:
    if len(word) > longest_len:
        longest_len = len(word)
        longest_word = word
print(longest_len, longest_word)

'''
#2.  (10pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"
print("Problem #2")
#alice_text = open("AliceInWonderland.txt")
#for word in alice_text:
    #print(word)

file = open("AliceInWonderland.txt", "r")
word_number = []
for line in file:
    words = split_line(line)
    for word in words:
        word_number.append(word.lower())
    #word_number.append(line)
#print(word_number)
print("There are", (len(word_number)), "words in Alice In Wonderland.")
    #line = line.lower()
    #words = split_line(line)
    #for word in words:
        #print(word)


# make an algorithm to find the average length
tracking = 0
for item in range(len(word_number)):
    tracking += len(word_number[item])

average = tracking / len(word_number)
average = round(average, 2)
print("The average number of letters in the words in Alice In Wonderland is", average ,"letters.")




##### CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS #####

#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?
# use .upper and .lower

### OR ###

#3  (13pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"

# for word in range(len(signahy))
seven_let = signahy
for word in range(len(seven_let)):


# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".
# Make a list.  You can substitute this for any of the above problems.
