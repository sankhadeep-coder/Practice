l=[2, 2, 1, 1, 1, 2, 2,1,1]
x=len(l)/2
c=0
s={}
for i in l:
    if i in s:
        s[i]+=1
    else:
        s[i]=1
    if s[i] > len(l) / 2:
        print(f'number apper more than n/2 times is {i}')
        break
print(s)