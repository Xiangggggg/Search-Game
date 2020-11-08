import random as r
size = 5
ratio = 1/3
p = r.sample([i for i in range(size*size)], int(size*size*ratio))
print(p)