# CSE-3353 Spring 2019
# PA01: Quick Sort
# Instructor: Dan Lorts
# Name: Eric Miao


import random
import time

def quickSort(myList):
    quickSortHelper(myList, 0, len(myList) - 1)


def quickSortHelper(myList, first, last):
    if first < last:
        split = partition(myList, first, last)

        quickSortHelper(myList, first, split - 1)
        quickSortHelper(myList, split + 1, last)


def partition(myList, first, last):
    pivot = myList[first]

    left = first + 1
    right = last

    done = False
    while not done:

        while left <= right and myList[left] <= pivot:
            left = left + 1

        while myList[right] >= pivot and right >= left:
            right = right - 1

        if right < left:
            done = True
        else:
            temp = myList[left]
            myList[left] = myList[right]
            myList[right] = temp

    temp = myList[first]
    myList[first] = myList[right]
    myList[right] = temp

    return right


def createRandomElements(n):
    myList = []
    for i in range(n):
        random_num = random.randint(0, 400)  # the generated element is in range between 0-400
        myList.append(random_num)
    return myList


# main function starts from here:
x = int(input("Please type in the number of elements you want in an unsorted list: "))  # User can input the number of random number that the program gonna generate
sample_list = createRandomElements(x)
print("Unsorted list: ", sample_list)
start = time.time()  # start time records the time that sorting starts
quickSort(sample_list)
print("Sorted list: ", sample_list)
end = time.time()  # end time records the time that sorting ejd
total_time = end - start
print("The number of elements = ", x)
print("Total sorting time = : ", total_time)