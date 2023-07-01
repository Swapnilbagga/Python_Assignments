

from matplotlib.pyplot import flag


num=int(input("enter the number:"))
flag=False
if num>1:
    for i in range(2,num):
        if num%i==0:
            flag=True
            break
if flag:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")