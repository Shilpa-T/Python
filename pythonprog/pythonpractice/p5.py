def up_low(s):
    u = 0
    l = 0
    lis = s.split()
    for w in lis:
        for i in range(len(w)):
            if w[i].isupper():
                u += 1
            elif w[i].islower():
                l += 1
    print "No. of Upper case characters :", u
    print "No. of Lower case Characters :", l


#up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


def unique_list(l):
    new_l=[]
    for item in l:
        if item not in new_l:

            print item
            new_l.append(item)
    print new_l



unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


def palindrome(s):
    if s[::] ==s[::-1]:
        return True
    else:
        return False

print palindrome('helleh')
print palindrome('madam')

import string

def ispangram(str1,alphabet=string.ascii_lowercase):
    str2=[]
    l=[]
    lis = str1.split()
    for w in lis:
        for i in range(len(w)):
            str2.append(w[i].lower())
    f=''.join(sorted(set(str2)))
    if f == alphabet:
        return True
    else:
        return False

#print ispangram("The quick brown fox jumps over the lazy dog")


def word_lengths1(phrase):
    l=[]
    for word in phrase.split(' '):
        l.append(len(word))
    return l

def word_lengths(phrase):
    return list(map(len,phrase.split(' ')))
print word_lengths('How long are the words in this phrase')

def digits_to_num(digits):
    c=len(digits)-1
    sum=0
    for l in digits:
        sum=sum+l*10**c
        print sum , l,c
        c-=1
    return sum

print digits_to_num([3,4,3,2,1])