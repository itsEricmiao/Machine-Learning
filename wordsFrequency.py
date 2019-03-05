# CSE-3342 Spring 2019
# PA02: Words Frequency
# Instructor: Nasser Jan
# Name: Eric Miao
import operator

def word_freq(list):
    counts = dict()
    for i in list:
        counts[i] = counts.get(i, 0) + 1
    return counts # The word_freq() returns a dictionary of word counts to the main method.


def asc_word_freq(dict): # accepts dictionary of words’ counts
    sorted_d = sorted(dict.items(), key=operator.itemgetter(1))
    # NOTE: if we want to sort the dict by key, we simply change the val from 1 to 0
    return sorted_d

def desc_word_freq(dict):  # accepts dictionary of words’ counts
    #sorted_d = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_d = sorted(dict.items(), key=lambda t: t[1], reverse=True)
    return (sorted_d)
    # returns a dictionary of word counts in ascending order to the main method.

def size_dict(d, n):
    temp = dict()
    size = len(d)
    if(n > size): # if the n is out of range, we return the whole dict
        return d
    elif(n < 0): # if the n is out of range, we return an empty dict
        return temp
    else: # normal case: 0 < n < size
        new_d = desc_word_freq(d)
        target = new_d[:n]
        return target


items = ["Liam", "Mason", "William", "Noah", "William", "James", "Sophia", "Logan", "Benjamin", "Mason", "Elijah",
         "Oliver", "Jacob", "Emma", "Olivia", "Ava", "William", "Isabella", "Oliver", "Sophia", "Mia", "Charlotte",
         "Amelia", "William", "Evelyn", "Abigail", "Olivia", "Ava", "Mason", "Isabella", "Noah", "William", "James",
         "Olivia", "Amelia", "Oliver", "William"]

# main function starts here
print("1. Name Frequency: ")
print(word_freq(items))
print('')

print("2. Ascending Order Based On Keys")
print(asc_word_freq(word_freq(items)))
print('')

print("3. Descending Order Based On Keys")
print(desc_word_freq(word_freq(items)))
print('')

print("4. Returns a subset of dictionary with n most frequent words. ")
print(size_dict(word_freq(items), 3))
print('')
