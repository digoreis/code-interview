# Given two strings, write a method do decide if one is a permutation of the other

def permutation(textA, textB):
    
    counter = dict({})

    if len(textA) != len(textB):
        return False

    for i in range(len(textA)):

        cA = textA[i]
        cB = textB[i]

        if counter.get(cA) is None:
            counter[cA] = 1
        else :
            counter[cA] += 1

        if counter.get(cB) is None:
            counter[cB] = -1
        else :
            counter[cB] -= 1

    for  key,value in counter.items():
        if value != 0:
            return False

    return True

print(permutation("abcd", "dcab"))