try:
    print('outer try block')
    n=int(input('enter a number: '))
    print(10/n)
    try:
        print('inner try')
        print('anu'+'preet')
    except TypeError:
        print('Hello')
    else:
        print('inner no exception')
except ArithmeticError:
        print(10/5)
else:
        print('outer no exception')
finally: print('finally block')
# Output--enter a number: 2
# 5.0
# inner try
# anupreet
# inner no exception
# outer no exception
# finally block