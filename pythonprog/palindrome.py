def is_palindrome(input):

    i=0
    j=len(input)-1

    while i<=j:
        if input[i]!=input[j]:
            return False
        i +=1
        j -=1
    return True

print is_palindrome('shilpa')
print is_palindrome('madam')
print is_palindrome('madem')
print is_palindrome('abccba')
