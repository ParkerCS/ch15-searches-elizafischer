'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''

# BINARY SEARCH HAS TO BE ALPHEBETIZED
import re
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open("dictionary.txt")
dictionary_list = []
for line in file:
    line = line.strip()
    dictionary_list.append(line)
file.close()

print("**--- Linear Search ---**")
file = open("AliceInWonderLand200.txt")
spellmisline = 0

for line in file:
    words = split_line(line)
    spellmisline += 1
    for word in words:
        key = word
        for item in range(len(dictionary_list)):
            if key.upper() == dictionary_list[item]:
                break
        else:
            print("Check:", key ,"'s spelling at line", spellmisline)

file.close()
'''
file = open("AliceInWonderLand200.txt", "r")
for line in file:
    words = split_line(line)
    for word in words:
        key = word
key = ""

i = 0
while i < len(name_list) and name_list[i] != key:
    i += 1

if i < len(name_list):
    print("The name is at position", i)
else:
    print("The name was not in the list.")
'''

print("**--- Binary Search ---**")
# LOOK AT FEB 7 AND 10

line_num = 0