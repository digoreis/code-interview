#Write a function to swap a number in place( that is, without temporary variables)
#Hint 491: Try picturing the two numbers, a and b, on a number 
#Hint 715: Lef diff be the difference betweeen a and b. Can you use diff some way? Then can you get rid of this temporary variable.
#Hint 736: You could also try to using XOR

def swap(numberA, numberB):
    numberA = numberA ^ numberB
    numberB =  numberA ^ numberB
    numberA = numberA ^ numberB
    
    return (numberA, numberB)

print(swap(20,10))

#Solution: Swipe using XOR, first using the variable A for to save the XOR of A = A ^ B. Second step is apply the XOR again but save 
# in B = A ^ B (that's moment move A to B). Now , apply XOR of B in A to recovery B in A= A ^ B. 