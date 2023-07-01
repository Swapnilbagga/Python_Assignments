class Vehicle:
    def __del__(self):
        print("vehicle object destroyed")
        print(10/0)
v=Vehicle()
del v
# Output--    
# print(10/0) ZeroDivisionError: division by zero