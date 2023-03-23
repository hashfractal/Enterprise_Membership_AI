def palindrome(stri):
    if stri.lower().replace(" ", "") == stri[::-1].lower().replace(" ", ""):
        return True
    return False

print( palindrome("qw  Q"))
print( palindrome("qwe"))