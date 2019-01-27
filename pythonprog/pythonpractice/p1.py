def front_back(str):
    if len(str) <= 1:
        return str
    mid = str[1:len(str)-1]
    return str[len(str)-1]+mid+str[0]

print front_back('code')



def not_string(str):
  if str[0]=='n' and str[1]=='o' and str[2]=='t':
      print str
      return str
  else:
      return 'not'+' '+ str

print not_string('candy')
print not_string('not sad')


def front3(str):
  if len(str) <=3:
    return str
  else:
    return str[:3]*3

print front3('Java')