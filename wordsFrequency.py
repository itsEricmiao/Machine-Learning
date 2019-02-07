# CSE-3342 Spring 2019
# PA02: Words Frequency
# Instructor: Nasser Jan
# Name: Eric Miao

items = ["Liam", "Mason", "William", "Noah", "William", "James", "Sophia", "Logan", "Benjamin", "Mason", "Elijah",
         "Oliver", "Jacob", "Emma", "Olivia", "Ava", "William", "Isabella", "Oliver", "Sophia", "Mia", "Charlotte",
         "Amelia", "William", "Evelyn", "Abigail", "Olivia", "Ava", "Mason", "Isabella", "Noah", "William", "James",
         "Olivia", "Amelia", "Oliver", "William"]


def word_freq(list):

    counts = dict()
    for i in list:
        counts[i] = counts.get(i, 0) + 1
    print(counts)

word_freq(items)
# ascending
