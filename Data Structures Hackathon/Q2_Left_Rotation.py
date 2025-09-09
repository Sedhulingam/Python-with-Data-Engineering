def rotateLeft(d, arr):
    n = len(arr)
    d = d % n 
    return arr[d:] + arr[:d]
d = int(input("Enter the number of rotations you want:"))
arr = [1, 2, 3, 4, 5]
rotated = rotateLeft(d, arr)
print("Final List: \n",rotated)  
