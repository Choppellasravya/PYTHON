n=int(input())
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev+digit**3
    n//=10
if rev==temp:
    print("armstrong")
else:
    print("not a armstrong number")
    


