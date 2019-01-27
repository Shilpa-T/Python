"""
input1 ="big document so. So it is not a list. So keep track of the words. Words are awesome!"

Make sure capital word and small word ar counted same.
that means word and Word are same
make sure they are no special characters so, awesome! and awesome is same.
output should be
decreasing order of freq count
if there is duplicate freq count, then the order should be based on alphabetical order

foo, 3
a,2
b,2
bar,2
c,2
h,1


uopdate it
"""
import string
def CountWords(input1):
    """
    Function  returns number of words in a file.
    :param file_name:
    :return:
    """
    tokens = []

    d={}

    tokens = tokens+input1.lower().split()

    for token in tokens:
        # Remove Punctuation
        word=token.replace("!", "")
        word=word.replace(".", "")
        d[word] = d.get(word,0)+1

    word_frq=[]
    for i,v in d.items():
        word_frq.append((v,i))
    word_frq.sort(reverse=True)

    for word in word_frq:
        print (word[1],word[0])





input1 ="big document so. So it is not a list. So keep track of the words. Words are awesome!"

CountWords(input1)