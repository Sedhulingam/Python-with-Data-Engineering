a= [10,9,8,7,6,5,4,3]
n = len(a)
for i in range(n):
    for j in range(1,n-i):
        if a[j-1]>a[j]:
            a[j-1],a[j]= a[j],a[j-1]
print(a)