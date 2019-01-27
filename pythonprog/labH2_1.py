"""
program to convert dollar to euros
test it for error

"""

Amount = raw_input("provide dollar amount ")
Exchange_rate = 1.19
try:
    dollar_amount = float(Amount)
except ValueError :
    print "Enter the correct amount "
else:
    num_euros = dollar_amount * Exchange_rate
    print "Number of euros",num_euros

