def input(str):
    if len(str)<3:
       return str
    if (str[-3:]=='ing'):
        return str[0:] + 'ly'
    else:
        return str[0:]+ 'ing'

print(input("According"))
print(input("abc"))
print(input("hi"))

