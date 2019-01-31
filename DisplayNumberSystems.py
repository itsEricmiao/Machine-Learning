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


def convertToTernary(decimal): # the function will take a decimal input as parameter and return the ternary number
    if decimal > 3:
        convertToTernary(decimal // 3)   # recursion if decimal is larger than 3
    print(decimal % 3, end = '') # Dividing the number successively by 3 and printing the remainder in reverse order.


def convertToQuaternary(decimal): # the function will take a decimal input as parameter and return the quaternary number
    if decimal > 4:
        convertToQuaternary(decimal // 4)   # recursion if decimal is larger than 4
    print(decimal % 4, end = '') # Dividing the number successively by 4 and printing the remainder in reverse order.


def convertToOctal(decimal): # the function will take a decimal input as parameter and return the octal number
    if decimal > 8:
        convertToOctal(decimal // 8)   # recursion if decimal is larger than 8
    print(decimal % 8, end = '') # Dividing the number successively by 8 and printing the remainder in reverse order.


def convertToHex(decimal): # the function will take a decimal input as parameter and return the hex number
    if decimal > 16:
        convertToHex(decimal // 16)   # recursion if decimal is larger than 16
    print(getHexNum(decimal % 16), end = '') # Dividing the number successively by 16 and printing the remainder in reverse order.

def convertToHex(binary): # convert from binary to hex


def getHexNum(digit): # this function serves for convertToHex function. It will change every digit from decimal expression to hex expression
    if digit < 10:
        return digit
    elif digit == 10:
        return 'A'
    elif digit == 11:
        return 'B'
    elif digit == 12:
        return 'C'
    elif digit == 13:
        return 'D'
    elif digit == 14:
        return 'E'
    elif digit == 15:
        return 'F'


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


def convertDectoOther(decimal):

    print("Binary: ", end = '')
    convertToBinary(decimal)
    print()
    print("Ternary: ", end='')
    convertToTernary(decimal)
    print()
    print("Quaternary: ", end='')
    convertToQuaternary(decimal)
    print()
    print("Octal: ", end='')
    convertToOctal(decimal)
    print()
    print("Hex: ", end='')
    convertToHex(decimal)
    print()


print("Welcome to Eric's number system converter")
print("Press 1 for converting decimal")
print("Press 2 for converting binary")
option = input()
if option == '1':
    print("You choose 1: Please enter your decimal number: ")
    decimal_number = input()
    try:
        val = int(decimal_number)
    except ValueError:
        print("That's not an int!")

    convertDectoOther(int(decimal_number))

elif option == '2':
    print("You choose 2: Please enter your binary number: ")

else:
    print("INVALID, please try again")

# find function overloading in python