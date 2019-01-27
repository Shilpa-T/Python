"""
CMTE_ID: identifies the flier, which for our purposes is the recipient of this contribution ZIP_CODE:
zip code of the contributor (we only want the first five digits/characters)
TRANSACTION_DT: date of the transaction
TRANSACTION_AMT: amount of the transaction
OTHER_ID: a field that denotes whether contribution came from a person or an entity
"""

def readinputfile(file):
    data_ZIP = {}
    median_zip = {}
    tokens = []
    lines = []
    read_file=open(file,'r')
    data_heading = ['cmte_id','zip_code','transaction_dt','transaction_amt','other_id']

    for line in read_file:

        tokens = line.split('|')
        cmte_id = tokens[0]
        zip_code = tokens[10][0:5]
        transaction_dt = tokens[13]
        transaction_amt = tokens[14]
        other_id = tokens[15]
        if other_id == '':
            occur = 1
            median = int(transaction_amt)
            sum = int(transaction_amt)
            print zip_code
            if zip_code not in data_ZIP:

                data_ZIP[zip_code]=[median,occur,sum]
                prev_median = 0
                m = calculate_median(median,prev_median)

                median_zip[zip_code] = m
            else:

                prev_median = m

            print cmte_id+'|'+zip_code+'|'+'|'.join( str(x) for x in data_ZIP[zip_code]) + '\n'

readinputfile('itcont.txt')


