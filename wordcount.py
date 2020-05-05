import sys
import string 


def dicts_word_count(test_file):

    word_count = open(test_file)

    word_count_dict = {}

    for line in word_count:
        words = line.strip().split(" ")
        
        for word in words:
            word = word.strip(string.punctuation) 
            word_count_dict[word] = word_count_dict.get(word, 0) + 1


    for key, value in word_count_dict.items():

        print(f"{key} {value}")
            
dicts_word_count(sys.argv[0])



#close file 
