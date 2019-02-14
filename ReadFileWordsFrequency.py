# CSE-3342 Spring 2019
# # PA03: Read File Words Frequency
# # Instructor: Nasser Jan
# # Name: Eric Miao


import re
def readfile(path):
    days_file = open(path, 'r')  # input the file
    mystr = days_file.read()
    wordList = re.sub("[^\w]", " ", mystr).split()
    return wordList

def word_freq(list):
    counts = dict()
    for i in list:
        counts[i] = counts.get(i, 0) + 1
    return counts # The word_freq() returns a dictionary of word counts to the main method.


#main function starts from here:
path = '/Users/ericmiao/Desktop/Programming/Python/smu.txt' # getting the path to the smu.txt file
a = readfile(path)
b = word_freq(a)
print(b)

