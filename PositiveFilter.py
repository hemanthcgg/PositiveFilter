# Program to print positive numbers
l=list(map(int,input().split()))
res=[]
for i in l:
    if(i>0):
        res.append(i)
print(res)