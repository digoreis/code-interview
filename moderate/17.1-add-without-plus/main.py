#Write a function that adds two numbers. You should not use `+` or any arithmetic operators.

def newPlus(numberA, numberB):
    while numberB:
        numberA, numberB = (numberA ^ numberB), (numberA & numberB) << 1
    return numberA

print(newPlus(17,6))