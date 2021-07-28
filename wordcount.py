# put your code here.
import string
import sys
import pprint
import collections
import operator


def count_words(file_name = "test.txt"):

#    open_file = open(file_name,"r")

    with open(file_name) as file_object:
        entire_file = file_object.read()
    entire_file = entire_file.strip().lower()
    for character in string.punctuation:
        entire_file = entire_file.replace(character,"")
    words = entire_file.split()
    word_count = collections.Counter(words)

#    word_count = {}
#    for line in open_file:
#        line = line.rstrip()
#        for character in string.punctuation:
#            line = line.replace(character,"")
#        line = line.lower()
#        words = line.split(" ")
#        for word in words:
#            word_count[word] = word_count.get(word, 0) + 1

    return word_count


        
output_dict = count_words(sys.argv[1])

word_items = output_dict.items()
sorted_word_items = sorted(word_items, key = operator.itemgetter(1,0))
sorted_word_items.reverse()
for item in sorted_word_items:
    print(f"{item[0]} {item[1]}")