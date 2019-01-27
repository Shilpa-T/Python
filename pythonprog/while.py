"""
while.py demonstrates  looping,
"""

number = "none given yet"

while number == "none given yet":
    answer = raw_input("what is  your favourite number")
    if answer == 'quit':
        break
    try:
        number = int(answer)
    except ValueError:
        print "Please give whole number"
else:
    print number," is good number"

