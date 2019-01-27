"""
CMTE_ID: identifies the flier, which for our purposes is the recipient of this contribution ZIP_CODE:
zip code of the contributor (we only want the first five digits/characters)
TRANSACTION_DT: date of the transaction
TRANSACTION_AMT: amount of the transaction
OTHER_ID: a field that denotes whether contribution came from a person or an entity
"""

import pandas as pd

def readinputfile(file):
    data= {}
    tokens = []
    lines = []
    read_file = open(file, 'r')
    data_heading = ['cmte_id', 'zip_code', 'transaction_dt', 'transaction_amt', 'other_id']

    for line in read_file:

        lines.append(line.split('|'))
    print lines

readinputfile('itcont.txt')