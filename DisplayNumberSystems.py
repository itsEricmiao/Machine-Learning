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
    power = 0;
    while binary > 1:
        x = get_digit(binary)
        binary = int(binary / 10)
        print('The result is: ', + x*(2**power), ' Binary = ', binary)
        power = power + 1



def get_digit(num):
    if num < 10:
        return num
    else:
        get_digit(num // 10)
        return (num % 10)

x = 1100
convertToDec(x)



