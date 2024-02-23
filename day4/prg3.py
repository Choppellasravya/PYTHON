r,c=int(input()),int(input())
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
min,max=1000,0
for i in l:
    for j in i:
        sum+=j
print(sum/(r*c))
