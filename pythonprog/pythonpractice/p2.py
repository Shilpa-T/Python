def double_char(str):
  str1=''
  for i in range(len(str)):
    str1=str1+str[i]*2
  return str1

print double_char('The')


def end_other(a, b):
  a=a.lower()
  b=b.lower()
  x=len(b)
  y=len(a)
  if len(a) > len(b):
    if a[x:-1] == b[:]:
        print a[x:-1],b[:]
        return True
  else:
    if b[y:-1] == a[:]:
        print b[y:-1],a[:]
        return True

print end_other('AbC', 'HiaBc')

