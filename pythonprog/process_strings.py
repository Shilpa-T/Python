"""

collect strings and display:
"""

def Collectstrings():

    string_list = []
    while True:
        string = raw_input("Enter the string vaue(enter to quit):")
        if not string:
            break
        string_list.append(string)
    return string_list

  

def CollectAndJoinStrings():
    string_list = Collectstrings()
    glue_string = "and".join(string_list)
    return glue_string

print CollectAndJoinStrings()