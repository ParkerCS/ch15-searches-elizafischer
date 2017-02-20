'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (7pts) Write code which finds and prints the longest word in the provided dictionary.
# If there are more than one longest word, print them all.
# Make a list and add words to them based on length
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





#2.  (10pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"


# make an algorithm to find the average length




## CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS ##

#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?
# use .upper and .lower

#### OR #####

#3  (13pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"
# for word in range(len(signahy))


# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.



