import re 

with open ('dracula.txt', 'r') as document_read:
    with open ('dracula_copy.txt', 'w') as document_write:
        for line in document_read:
            document_write.write(line)

with open('dracula.txt', 'r', encoding='utf-8') as file:
    text = file.read()


# make all words lowercase 
text = text.lower()
# splits all the word
words = text.split()
# stripped puncuations 
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
print(stripped[:200])







