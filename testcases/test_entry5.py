n=[53,34,56,23,57,89,98]
v=[]
for i in range(0,len(n)):
    s=n[i]%10
    r=n[i]//10
    if s-r==1:
        print(n[i])
        print(v.append(n[i]))
print(v)
print(max(v))








