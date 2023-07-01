def multiple_of_4(str):
    strng=""
    if len(str)%4==0:
        rev_strng=str[::-1]
        print(rev_strng)
    else:
        print(str)
    return strng

print(multiple_of_4('helo'))
print(multiple_of_4('helooooo'))
print(multiple_of_4('heloo'))
print(multiple_of_4('he'))