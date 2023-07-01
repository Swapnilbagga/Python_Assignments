def status(age):
    if age<0:
        raise ValueError("Only positive integrs are allowed")
    if age>22:
        print('eligible for mrg')
    else:
        print('not eligible for mrg, try again after sometime')
try:
    num=int(input('enter your age: '))
    status(num)
except ValueError:
    print('Only positive integrs are allowed ........')
finally:
    print('finally block')
#  Output-- 
# enter your age: 20
# not eligible for mrg, try again after sometime
# finally block
# enter your age: 23
# eligible for mrg
# finally block