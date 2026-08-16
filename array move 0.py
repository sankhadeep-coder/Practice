l=[0, 1, 0, 3, 12]
pos = 0

for i in range(len(l)):
    if l[i] != 0:
       l[i], l[pos] = l[pos], l[i]
       pos+=1
 

print(l)