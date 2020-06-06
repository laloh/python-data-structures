import string
import re
def palindrome(string, n, i=0):
    equal = string[i] == string[n]
    if n == 0 or equal == False:
        return f"is {string} a palindrome? "+ str(equal)
    else:
        return palindrome(string, n-1, i+1)

string = "Wassamassaw – a town in South Dakota" \
    .replace(" ", "") \
    .lower()

string = re.sub(r'[^\w\s]','',string)
print(palindrome(string, len(string)-1))