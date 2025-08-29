a = [1,5,3,2,7,8,31]
n = int(input("Enter the number to be found: "))
for i in range(len(a)):
    if a[i]==n:
        print(f"Value {n} is placed in the position {i+1}")
        break
else:
    print("Number not found")
    
