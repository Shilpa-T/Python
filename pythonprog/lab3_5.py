"""
Project:program for a hardware store.
The program aks for how many square feet she wants to paint,and
tell her how many cans to buy.

"""

PRICE_CAN = 17.95
tax = .0825
while True:
    square_feet_value = raw_input("How many square feet you want to paint")
    if square_feet_value == '':
        continue
    elif square_feet_value =='quit':
        break
    try:
        square_feet_value = int(square_feet_value)
    except ValueError:
        print"Provide correct value"
    else:
        div=square_feet_value/200
        mod=square_feet_value%200
        if mod == 0:
            paint_can = div
        else:
            paint_can=div+1
        charge_can = float((PRICE_CAN +tax)* paint_can)
        print "Number of cans to Buy",paint_can
        print " charge of paint can",charge_can
