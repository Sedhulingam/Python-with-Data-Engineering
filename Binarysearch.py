a= [10,20,35,40,50,60]
n = len(a)
left = 0
right = n-1
val = int(input("Enter the value: "))
while left<=right:
    mid = int((left+right)/2)
    if(val==a[mid]):
        print(f"Position is {mid+1}")
        break
    if(val<a[mid]):
        right = mid-1
    if(val>a[mid]):
        left = mid+1

else:
    print("Value not found")