p = list(map(int,input("ent values").split()))
t=int(input("ent num "))
for i in range(len(p)):
    if p[i]+p[i-1]==t:
        print(i,i-1)
