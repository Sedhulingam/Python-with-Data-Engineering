# import sys


# n = len(sys.argv)
# print("Size= ",n)
# for i in range(1,n):
#     print(sys.argv[i])


import sys
n = len(sys.argv)

a = []
try:
    for i in range(1,n):
        a.append(float(sys.argv[i]))
    print("Maximum Value: ",max(a))
    print("Minimum Value: ",min(a))
except ValueError:
    print("Invalid Entry")




        

    