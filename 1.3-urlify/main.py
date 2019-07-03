# Write a method to replace all spaces in a string with %20. You may assume that the string has 
# sufficient space at the end to hold the addictional characters, and that you are given the `true` 
# length of the string.( Note: if implementing in Java, please use a character array so that you 
# can perfom this operation in place)

def urlify(url):
    newText = ""
    for c in url:
        newText += c if c != " " else "%20"

    return newText

print(urlify("aaa bbb c"))