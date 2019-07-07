# Assume you have a method isSubstring which checks if one word is a substring of another. given two strings,  s1 and s2, 
# write code to check if s2 is a rotation of s1 using only one call to isSubstring(e.g. "waterbottle" is a rotation of "erbottlewat")

def isSubtring(original,substring):
    return substring in original

def isRotation(text1, text2):

    return isSubtring(text1+text1, text2)

print(isRotation("waterbottle", "erbottlewat"))