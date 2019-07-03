# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is 
# a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of 
# letters. The palidrome does need to be limited to just dictionary words.

def palindromePermutation(text):
    counter = dict()
    
    for c in text:
        counter[c] = ((counter.get(c) + 1) % 2) if counter.get(c) else 1
    
    sumValues = 0

    for value in counter.values():
        sumValues += value
    
    return sumValues <= 1

print(palindromePermutation("aabbccdd"))
print(palindromePermutation("aabbzccdd"))
print(palindromePermutation("adbcyWzcybda"))