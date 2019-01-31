# CSE-3342 Spring 2019
# PA01: DisplayNumberSystems (with a simpler design)
# Instructor: Nasser Jan
# Name: Eric Miao


def convertToOtherSystem(decimal, num): # the function will take a decimal input as parameter and return the binary number
    if decimal > num:
        convertToOtherSystem(decimal // num)   # recursion if decimal is larger than 1
    print(decimal % num) # Dividing the number successively by 2 and printing the remainder in reverse order.

convertToOtherSystem(350, 2)
