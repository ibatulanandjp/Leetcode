from collections import OrderedDict


# Method: Using OrderedDict collections
class LRUCache:

    def __init__(self, capacity: int):
        # Initialize the hashmap (ordered) and the capacity
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # If the key doesn't exist, return -1
        if key not in self.cache:
            return -1
    
        # Else move the fetched pair to the right end (Most recent), and then return the value 
        self.cache.move_to_end(key, last=True)
        return self.cache.get(key)

    def put(self, key: int, value: int) -> None:

        # If the key already exist, just move the pair to the right end (Most recent)
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
            
        else:
            # If the capacity has exceeded already, pop from the left end (Least recent)
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)

        # Add/Update the key-pair
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
