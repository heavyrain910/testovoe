from itertools import *  #все_перестановки
count = 0
for i in permutations([1,2,3,4,5,6,7,8], 8):
  count+=1  
print(count)

#перестановки_без_повторений
count = 0
for i in permutations([1,2,3,4,5,6,7,8], 1):
  count+=1  
print(count)
