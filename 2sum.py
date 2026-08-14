l= eval(input("ent valus by commas "))
l=list(l)
x=int(input("ent target"))
for i in range(len(l)):
    for j in range(i):
        if l[i]+l[j]==x:
            print(i,j)