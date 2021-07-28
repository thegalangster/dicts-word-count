# put your code here.
import string
import sys
import pprint

def count_words(file_name = "test.txt"):
    open_file = open(file_name,"r")
    word_count = {}
    for line in open_file:
        line = line.rstrip()
        for character in string.punctuation:
            line = line.replace(character,"")
        line = line.lower()
        words = line.split(" ")
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count
        
output = count_words(sys.argv[1])
pprint.pp(output)