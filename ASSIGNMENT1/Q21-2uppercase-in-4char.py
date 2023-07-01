def strng_upper(str1):
    num_upper=0
    for letter in str1[:4]:
        if letter.upper()==letter:
            num_upper+=1
    if num_upper>=2:
        return str1.upper()
    return str1

strng_upper('python')
strng_upper('pyThon')