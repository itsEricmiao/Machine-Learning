# CSE-3342 Spring 2019
# # PA03: Read File Words Frequency
# # Instructor: Nasser Jan
# # Name: Eric Miao
import re
def readfile(path):
    days_file = open(path, 'r')  # Input the file
    mystr = days_file.read() # Read in the file
    wordList = re.sub("[^\w]", " ", mystr).split() # Split string to the words
    return wordList

def word_freq(list):
    counts = dict() # Initilize a dictionary
    for i in list: # Loop through the list and add instances if found in the dictionary
        counts[i] = counts.get(i, 0) + 1
    return counts # The word_freq() returns a dictionary of word counts to the main method.

def word_no_duplicate (items):
    return  set(sorted(set(items)))# return a sorted list with non-duplicates

def dic_no_duplicate (dict):
    return  set(sorted(set(dict)))

#main function starts from here:
path = '/Users/ericmiao/Desktop/Programming/Python/smu.txt' # getting the path to the smu.txt file
wordList = readfile(path)
dict = word_freq(wordList)
print("1. Dictionary is: ")
print(dict)
print()

print("2. Input list and return set that contains non-duplicates only: ")
print(word_no_duplicate(wordList))
print()

print("3. Input dictionary and return set that contains non-duplicates only: ")
print(dic_no_duplicate(dict))