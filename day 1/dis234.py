a,b,c,d=map(int,input().split())
fa=a-a*c//100
fb=b-b*c//100
print(fa,fb)
if fa<fb:
    print("first")
elif fa>fb:
    print("second")
else:
    print("any")
