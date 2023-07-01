# symmetric difference 
set1 = {10, 20, 30}
set2 = {30, 40, 100}
new_set = set1.symmetric_difference(set2)
print(new_set)
#  OR 
set1 = {'A', 'B'}
set2 = {'A','C'}
new_set = set1 ^ set2
print(new_set)


# SET DIFFERENCE 
setn1 = set([1, 1, 2, 3, 4, 5])
setn2 = set([1, 5, 6, 7, 8, 9])
print("\nOriginal sets:")
print(setn1)
print(setn2)
r1 = setn1.difference(setn2)
print("\nDifference of setn1 - setn2:")
print(r1)
r2 = setn2.difference(setn1)
print("\nDifference of setn2 - setn1:")
print(r2)