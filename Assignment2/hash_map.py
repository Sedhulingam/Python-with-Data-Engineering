class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

hm = HashMap()

hm.put("name", "Alice")
hm.put("age", 25)
hm.put("location", "New York")

print("Name:", hm.get("name"))             
print("Age:", hm.get("age"))               

hm.put("age", 26)                          
print("Updated Age:", hm.get("age"))       

hm.remove("location")
print("Location after removal:", hm.get("location"))  
