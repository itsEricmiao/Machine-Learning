# CSE-3342 Spring 2019
# PA02: Words Frequency
# Instructor: Nasser Jan
# Name: Eric Miao
import operator
items = ["Liam", "Mason", "William", "Noah", "William", "James", "Sophia", "Logan", "Benjamin", "Mason", "Elijah",
         "Oliver", "Jacob", "Emma", "Olivia", "Ava", "William", "Isabella", "Oliver", "Sophia", "Mia", "Charlotte",
         "Amelia", "William", "Evelyn", "Abigail", "Olivia", "Ava", "Mason", "Isabella", "Noah", "William", "James",
         "Olivia", "Amelia", "Oliver", "William"]


def word_freq(list):
    counts = dict()
    for i in list:
        counts[i] = counts.get(i, 0) + 1
    return counts # The word_freq() returns a dictionary of word counts to the main method.


def asc_word_freq(dict): # accepts dictionary of words’ counts
    sorted_d = sorted(dict.items(), key=operator.itemgetter(0))
    return sorted_d

def desc_word_freq(dict):  # accepts dictionary of words’ counts
    sorted_d = sorted(dict.items(), key=operator.itemgetter(0), reverse=True)
    return sorted_d
    # returns a dictionary of word counts in ascending order to the main method.

def size_dict(d, n):
    temp = dict()
    size = len(d)
    print(size)
    if( n > size):
        return d
    elif(n < 0):
        return temp
    else:
        



# main function starts here
print(word_freq(items))
print(asc_word_freq(word_freq(items)))
print(desc_word_freq(word_freq(items)))
print(size_dict(word_freq(items), 5))
