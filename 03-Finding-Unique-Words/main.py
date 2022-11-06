import re

# SCRIPT TO FETCH UNIQUE SORTED WORDS FROM A TEXT FILE.
list_of_words = []

filename = 'text.txt'  # INSERT YOUR FILE PATH HERE

with open(filename, 'r') as f:
    for line in f:
        # MAKE SURE CASE IS IGNORED
        list_of_words.extend(re.findall(r'[\w]+', line.lower()))

# CREATE UNIQUE DICTIONARY TO STORE THE NUMBER OF OCCURENCE OF A WORD
unique = {}

for each in list_of_words:
    if each not in unique:
        unique[each] = 0
    unique[each] += 1

# CREATE A LIST TO SORT THE FINAL UNIQUE WORDS
s = []

# IF OCURRENCE OF A WORD IS 1, THEN IT'S UNIQUE
for key, val in unique.items():
    if val == 1:
        s.append(key)

print('total of unique words: ', len(s), '\nunique words: ', sorted(s))

