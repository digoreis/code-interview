# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write 
# a function to check if they are one edit( or zero edits) away.

def oneWay(text1, text2):
    if len(text1) != len(text2):
        return (True, abs(len(text1) - len(text2)))

    count = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            count += 1

    return ((count >= 1), count)


print(oneWay("abc", "ab"))
print(oneWay("abc", "abcd"))
print(oneWay("abd", "abc"))
print(oneWay("abc", "abc"))