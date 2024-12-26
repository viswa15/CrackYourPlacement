class RandomizedCollection:

    def __init__(self):
        self.vals = []  # List to store values
        self.indices = {}  # Dictionary to store indices of each value


    def insert(self, val: int) -> bool:
        is_new = val not in self.indices
        if is_new:
            self.indices[val] = set()
        self.indices[val].add(len(self.vals))
        self.vals.append(val)
        return is_new


    def remove(self, val: int) -> bool:
        if val not in self.indices or not self.indices[val]:
            return False

        # Remove an index of the value
        remove_idx = self.indices[val].pop()
        last_val = self.vals[-1]

        # Replace the removed value with the last value in the list
        self.vals[remove_idx] = last_val
        self.indices[last_val].add(remove_idx)
        self.indices[last_val].discard(len(self.vals) - 1)

        # Remove the last element from the list
        self.vals.pop()

        # Clean up the dictionary if no indices remain for the value
        if not self.indices[val]:
            del self.indices[val]

        return True





    def getRandom(self) -> int:
        return random.choice(self.vals)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()