password=input("Enter your favourite password:")
u,l,d,s=0,0,0,0
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
digits="0123456789"
specialchar="$@#"
if len(password)>=6 and len(password)<=16:
    for i  in password:
        if (i in capitalalphabets):
            u+=1
        if (i in smallalphabets):
            l+=1
        if (i in digits):
            d+=1
        if (i in specialchar):
            s+=1
    if (u>=1 and l>=1 and d>=1 and s>=1 and u+l+d+s==len(password)):
        print("Valid password")
    else:
        print("Invalid password")

else:
    print("Alert!....password must be between 6-16 characters")
        