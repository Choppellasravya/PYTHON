s=input()
s1=""
for i in s:
    for i in "aeiouAEIOU":
        if s.count(i)%2!=0:
            s1+=i
print(min(s1))
