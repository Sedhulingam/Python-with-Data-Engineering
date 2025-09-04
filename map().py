# square numbers are list
numbers = [1,2,3,4,5]
sqno = list(map(lambda x:x**2,numbers))
print(sqno)

# convert string to uppercase
words = ["hello", "python", "map"]
up_words = map(words.upper,words)
up_words = list(up_words)
print(up_words)