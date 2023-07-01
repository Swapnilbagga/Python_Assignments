# Right angle triangle
from ast import pattern


for i in range(5):
    for j in range(i):
        print('*',end=' ')
    print()


# downward half pyramid 
rows = int(input("Enter the number of rows: "))  
for i in range(rows + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  


# triangle pyramid 
n = int(input("Enter the number of rows: "))  
m = (2 * n) - 2  
for i in range(0, n):  
    for j in range(0, m):  
        print(end=" ")  
    m = m - 1  # decrementing m after each loop  
    for j in range(0, i + 1):  
        # printing full Triangle pyramid using stars  
        print("* ", end=' ')  
    print(" ")  


# downward triangle 
rows = int(input("Enter the number of rows: "))  
  
# It is used to print space  
k = 2 * rows - 2  
# Outer loop in reverse order  
for i in range(rows, -1, -1):  
    # Inner loop will print the number of space.  
    for j in range(k, 0, -1):  
        print(end=" ")  
    k = k + 1  
    # This inner loop will print the number o stars  
    for j in range(0, i + 1):  
        print("*", end=" ")  
    print("")  


# two pyramid in single pattern
rows = input("Enter the number of rows: ")  
  
# Outer loop will print the number of rows  
for i in range(0, rows):  
    # This inner loop will print the stars  
    for j in range(0, i + 1):  
        print("*", end=' ')  
    # Change line after each iteration  
    print(" ")  
# For second pattern  
for i in range(rows + 1, 0, -1):  
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  

# diamond
rows = int(input("Enter the number of rows: "))  
  
# It is used to print the space  
k = 2 * rows - 2  
# Outer loop to print number of rows  
for i in range(0, rows):  
    # Inner loop is used to print number of space  
    for j in range(0, k):  
        print(end=" ")  
    # Decrement in k after each iteration  
    k = k - 1  
    # This inner loop is used to print stars  
    for j in range(0, i + 1):  
        print("* ", end="")  
    print("")  
  
# Downward triangle Pyramid  
# It is used to print the space  
k = rows - 2  
# Output for downward triangle pyramid  
for i in range(rows, -1, -1):  
    # inner loop will print the spaces  
    for j in range(k, 0, -1):  
        print(end=" ")  
    # Increment in k after each iteration  
    k = k + 1  
    # This inner loop will print number of stars  
    for j in range(0, i + 1):  
        print("* ", end="")  
    print("")  