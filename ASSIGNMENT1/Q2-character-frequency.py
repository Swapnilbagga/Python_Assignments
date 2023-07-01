strng="google.com"
dict={}
for n in strng:
    keys=dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict=1
    print(dict)