class HashTable:
    def __init__(self):
        # The library shelves
        self.collection = {}

    def hash(self, key):
        # Calculate sum of Unicode values using ord()
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hash_val = self.hash(key)
        # If the shelf (hash_val) doesn't exist, create it
        if hash_val not in self.collection:
            self.collection[hash_val] = {}
        # Store the key-value pair on that shelf
        self.collection[hash_val][key] = value

    def remove(self, key):
        hash_val = self.hash(key)
        # Check if shelf exists and key is on it
        if hash_val in self.collection and key in self.collection[hash_val]:
            del self.collection[hash_val][key]
            # Optional cleanup: remove shelf if it's now empty
            if not self.collection[hash_val]:
                del self.collection[hash_val]

    def lookup(self, key):
        hash_val = self.hash(key)
        # Return value if found, else None
        if hash_val in self.collection and key in self.collection[hash_val]:
            return self.collection[hash_val][key]
        return None
