#Design a method to find the frequency of occurrences of any given word in a book. What if we were running this algorithm multiple times?
#Hint 488: Think about what the best conceivable runtime is for this problem. If your solution matches the best 
# conceivable runtime, then you probablycan't do any better.
#Hint 535: Can use a Hash Table to optimize the repeated case?
def wordCount(text, word):
    counter = dict({})
    for w in text.split():
        if counter.get(w) is None:
            counter[w] = 0
        counter[w] += 1
    
    if counter[word] is None:
        return 0
    return counter[word]

text = """Design a method to find the frequency of occurrences of any given word in a book. What if we were running this algorithm multiple times?
Hint 488: Think about what the best conceivable runtime is for this problem. If your solution matches the best 
conceivable runtime, then you probablycan't do any better.
Hint 535: Can use a Hash Table to optimize the repeated case?"""

print(wordCount(text, "to"))