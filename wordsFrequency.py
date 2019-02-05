# CSE-3342 Spring 2019
# PA02: Words Frequency
# Instructor: Nasser Jan
# Name: Eric Miao

items = ["Liam", "Mason", "William", "Noah", "William", "James", "Sophia", "Logan", "Benjamin", "Mason", "Elijah",
         "Oliver", "Jacob", "Emma", "Olivia", "Ava", "William", "Isabella", "Oliver", "Sophia", "Mia", "Charlotte",
         "Amelia", "William", "Evelyn", "Abigail", "Olivia", "Ava", "Mason", "Isabella", "Noah", "William", "James",
         "Olivia", "Amelia", "Oliver", "William"]

newList = []
for i in range(len(items)-1):
    j = i + 1
    for j in range(len(items)):
        if(items[i] == items[j]):
            if items[i] in newList:
                pass # do nothing
            else:
                newList.append(items[i])
print(newList)

