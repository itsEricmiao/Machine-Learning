# CSE-3342 Spring 2019
# PA01: DisplayNumberSystems
# Instructor: Nasser Jan
# Name: Eric Miao


# convertToBinary
# convertToTernary
# convertToQuaternary
# convertToOctal
# convertToHex
# convertToDec


def convertToBinary(decimal): # the function will take a decimal input as parameter and return the binary number
    if decimal > 1:
        convertToBinary(decimal // 2)   # recursion if decimal is larger than 1
    print(decimal % 2, end = '') # Dividing the number successively by 2 and printing the remainder in reverse order.

def convertToDec(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    print(decimal)

x = 1010
convertToDec(x)
