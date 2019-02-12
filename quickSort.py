# CSE-3353 Spring 2019
# PA01: Quick Sort
# Instructor: Dan Lorts
# Name: Eric Miao


import random
import time

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


# main function starts from here:
x = int(input("Please type in the number of elements you want in an unsorted list: "))
alist = []

for i in range(x):
    random_num = random.randint(1, 400)
    alist.append(random_num)
print("Unsorted list: ", alist)
start = time.time()
quickSort(alist)
print("Sorted list: ", alist)
end = time.time()
total_time = end - start
print("The number of elements = ", x)
print("Total sorting time = : ", total_time)