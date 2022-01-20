from itertools import *
count = 0
for i in permutations('12345678'):
  count+=1  
print(count)
