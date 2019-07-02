# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def is_unique(text):
    if text == "":
        return True

    map = dict({})
    for c in text:
        if map.get(c) is None:
            map[c] = 1
        else:
            return False
    return True

print(is_unique("aba"))
print(is_unique("abc"))
print(is_unique("aaaaabbbbbccccccddddddd"))
print(is_unique("aqwetdvfghnjuyri"))
print(is_unique(""))