# allows for random list generation in solution 2
import random

# sample lists
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

overlap = list()

# solution 2: randomly generates two lists of integers
list1 = random.sample(range(0,51), 12)
list2 = random.sample(range(0,51), 16)

# using lists a and b
overlap = [i for i in list1 if i in list2]
# print(overlap)
results = [i for i in overlap if overlap.count(i) == 1]
if len(results) == 0:
    print('No overlaps.')
print(results)