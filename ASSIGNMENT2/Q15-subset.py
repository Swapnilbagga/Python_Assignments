a={1,4,5,7,8}
b={5,4,0,9,7,1}
c={1,4,7}
print("set1:",a)
print("set2:",b)
print("set3:",c)
if (a.issubset(b)):
     print(" set1 is subset of set2")
if (b.issubset(a)):
      print("If set2 is subset of set1")
if (b.issubset(c)):
      print("If set2 is subset of set3")
if (c.issubset(b)):
      print("If set3 is subset of set2")
