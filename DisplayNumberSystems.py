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

# Step 1: Converting decimal to other number systems
def convertToBinary(decimal): # the function will take a decimal input as parameter and return the binary number
    if decimal > 1:
        convertToBinary(decimal // 2)   # recursion if decimal is larger than 1
    print(decimal % 2, end = '') # Dividing the number successively by 2 and printing the remainder in reverse order.


def convertToTernary(decimal): # the function will take a decimal input as parameter and return the binary number
    if decimal > 3:
        convertToTernary(decimal // 3)   # recursion if decimal is larger than 1
    print(decimal % 3, end = '') # Dividing the number successively by 2 and printing the remainder in reverse order.


def convertToQuaternary(decimal): # the function will take a decimal input as parameter and return the binary number
    if decimal > 4:
        convertToQuaternary(decimal // 4)   # recursion if decimal is larger than 1
    print(decimal % 4, end = '') # Dividing the number successively by 2 and printing the remainder in reverse order.


def convertToOctal(decimal): # the function will take a decimal input as parameter and return the binary number
    if decimal > 8:
        convertToOctal(decimal // 8)   # recursion if decimal is larger than 1
    print(decimal % 8, end = '') # Dividing the number successively by 2 and printing the remainder in reverse order.



# Step 2: Converting binary to other number systems
def convertToDec(binary):
    power = 0;
    while binary > 1:
        x = get_digit(binary)
        binary = int(binary / 10)
        print('The result is: ', + x*(2**power), ' Binary = ', binary)
        power = power + 1


def get_digit(num): # this is a function that can get each digit of the number from right to left
    if num < 10: # if the digit is less than 10, we just return the number since it is only 1 digit
        return num
    else:
        get_digit(num // 10)
        return num % 10


x = 1100

convertToQuaternary(350)

