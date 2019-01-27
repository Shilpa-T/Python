"""
A program that asks user name and user age  in years.
report user age in hours
"""

user_name = raw_input( "whats your name ?")
user_age_string = raw_input("how old are you ?")
user_age = float(user_age_string)
user_age_hours = user_age * 365 * 24

print " whats your name ?",user_name
print " How old are you ?",user_age
print user_name, " you are ",user_age_hours,"hours old"




