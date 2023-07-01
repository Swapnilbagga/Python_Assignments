class TooYoungException(Exception):
    def __init__(self,age):
        self.age=age
class TooOldException(Exception):
    def __init__(self,age):
        self.age=age
try:

    age=int(input('enter age: '))
    if age<18:
        raise TooYoungException('please wait sometime')
    elif age>65:
        raise TooOldException('your age is old')
    else:
        print('we will find one girl soon')
except TooYoungException as e:
    print('please wait....')
except TooOldException as e:
    print('you are old...')
# Output-- enter age: 20
# we will find one girl soon