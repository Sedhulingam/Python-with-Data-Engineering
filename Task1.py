data = {'a': 10, 'b': 25, 'c': 18}
# Sum of the values
total = sum(data.values())
print("Sum:", total)
# Print the Max value and Key
maximum = max(data, key=data.get)
print("Maximum:", data[maximum])
print("Key with Max value:", maximum)
# Print the Min value and Key
minimum = min(data, key=data.get)
print("Minimum:", data[minimum])
print("Key with Min value:", minimum)
