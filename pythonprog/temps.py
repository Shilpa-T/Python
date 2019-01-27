"""
Demonstrating min,max,aggregating list and
iterating the list with for  and displaying in sorted way.
"""

def Average(numbers):
    return sum(numbers)/len(numbers)

def Asktemp():

     while True:
         temp = raw_input("enter the temperature")
         if temp == '':
             return None
         try:
             return float(temp)
         except ValueError:
             pass
def Asktemps():
    temps=[]
    while True:
        new_temp = Asktemp()
        if new_temp == None:
            return temps
        temps.append(new_temp)

def ReportTemps(temps):
    print "Temperature are"
    for temp in temps:
        print temp
    print "Average temperature",Average(temps)
    print " Max temperature",max(temps)
    print "Min temperature",min(temps)
    print "Sorted"
    for temp in sorted(temps):
        print temp

def processTemps():
    ReportTemps(Asktemps())

processTemps()

