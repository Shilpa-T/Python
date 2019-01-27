import random
print "your lotto pick:",
for num in range(1,7,1):
    x = random.randrange(1,52)
    print x,
print "\nThat will be $5 . Good luck!"