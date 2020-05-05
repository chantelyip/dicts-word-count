import sys
import string 

def dicts_word_count(file):

    word_count = open(file)

    word_count_dict = {}

    for line in word_count:
        words = line.strip().split(" ")
        
        for word in words:
            word = word.strip(string.punctuation).lower() 
            word_count_dict[word] = word_count_dict.get(word, 0) + 1


    for key, value in sorted(word_count_dict.items()):

        print(f"{key} {value}")
            
dicts_word_count(sys.argv[1])

print ('Number of arguments:', len(sys.argv), 'arguments.')




#close file 
