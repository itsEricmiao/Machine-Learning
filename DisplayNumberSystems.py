# CSE-3342 Spring 2019
# PA01: DisplayNumberSystems
# Instructor: Nasser Jan
# Name: Eric Miao

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



def get_digit(num): # this is a function that can get each digit of the number from right to left
    if num < 10: # if the digit is less than 10, we just return the number since it is only 1 digit
        return num
    else:
        get_digit(num // 10)
        return num % 10


def convertDecToOther(decimal):
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


# Step 2: Converting binary to other number systems
def convertBinaryToDec(binary): #Binary to decimal converter
    binary = str(binary)
    b = list(binary) # create a list from the number
    n = len(list(binary)) # getting legth of the list
    decimal = 0
    hold = 0
    i = 0
    exp = n - 1
    while (i < n): #loop through the list and getting the x*2**exp for each decimal numbers
        x = int(b[i])
        quot = 2 ** exp
        hold = x * quot
        i += 1
        exp -= 1
        decimal = decimal + hold  #adding each number togther and we will get the final decimal number
    return decimal

# We convert binary to decimal and we use the funcions above to convert decimal to other number systems
def convertBinaryToTernary(binary):
    decimal = convertBinaryToDec(binary)
    convertToTernary(decimal)

def convertBinaryToQuaternary(binary):
    decimal = convertBinaryToDec(binary)
    convertToQuaternary(decimal)


def convertBinaryToOctal(binary):
    decimal = convertBinaryToDec(binary)
    convertToOctal(decimal)


def convertBinaryToHex(binary):
    decimal = convertBinaryToDec(binary)
    convertToHex(decimal)


def convertBinaryToOther(binary):
    #print("Decimal: ", end='')
    print("Decimal: ", convertBinaryToDec(binary), end = '')
    print()
    print("Ternary: ", end='')
    convertBinaryToTernary(binary)
    print()
    print("Quaternary: ", end='')
    convertBinaryToQuaternary(binary)
    print()
    print("Octal: ", end='')
    convertBinaryToOctal(binary)
    print()
    print("Hex: ", end='')
    convertBinaryToHex(binary)
    print()
def ifBinary(number):
    binary = str(number)
    a = list(binary)  # create a list from the number
    for i in range (len(a)):
        x = int(a[i])
        if (x > 1):
            return False
    return True

# the main function starts here:
print("Welcome to Eric's number system converter")
print("Press 1 for converting decimal")
print("Press 2 for converting binary")
option = input()
if option == '1':
    print("You choose 1: Please enter your decimal number: ")
    decimal_number = input()
    try:
        val = int(decimal_number) # using try...except to make sure the input is number only
        convertDecToOther(int(decimal_number))
    except ValueError:
        print("That's not an int!")


elif option == '2':
    print("You choose 2: Please enter your binary number: ")
    bin = input()
    try:
        val = int(bin)  # using try...except to make sure the input is number only
        if (ifBinary(val) == True):
            convertBinaryToOther(int(bin))
        else:
            print("That's not an int!")
            exit()
    except ValueError:
        print("That's not an int!")

elif option == '3': # this is a testing funtion
    bin = input()
    if(ifBinary(bin) == True):
        print("It is binary")
    elif(ifBinary(bin) == False):
        print("It is NOT binary")

else:
    print("INVALID, please try again")





