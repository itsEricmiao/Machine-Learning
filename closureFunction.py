# CSE-3342 Spring 2019
# PA04: Closure Function
# Instructor: Nasser Jan
# Name: Eric Miao

def outerFunc(input): #outer function
    msg = input
    print(input, "is a cool place")

    def innerFunc(): #inner function
        print(msg, "is an amazing place")

    return innerFunc #return innerFunc without executing it

#main function starts here:
a = outerFunc('Dallas') # assign inner function to a and b
b = outerFunc('Austin')
del outerFunc # even if we delete the outer function, the closure function still can remember the value
a() # a and b remember the value outside of the scope
b()