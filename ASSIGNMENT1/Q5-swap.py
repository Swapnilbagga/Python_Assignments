a='hello'
b='welcome'
c=a[0:2]
a=b[0:2] + a[2:5]
b=c[0:2] +b[2:]
d=a[0:] +' '+b[0:]
print(d)