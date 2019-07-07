# Implement a method to perform basic string compression using the counts of repeated characters. For example, 
# the string aabccccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the 
# original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters(a-z).

def compress(text):
    compressedString = ""
    lastChar = ""
    charCount = 0
    for c in text:
        if c == lastChar:
            charCount += 1
        else:
            if lastChar != "":
                compressedString += lastChar + str(charCount)
            lastChar = c
            charCount = 1

    compressedString += lastChar + str(charCount)
    return compressedString

print(compress("aabcccccaaa"))