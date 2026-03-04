'''
Question topic - Array
Question link - https://leetcode.com/problems/insert-delete-getrandom-o1/description
'''
# Sol - 
import random

class RandomizedSet:
    def __init__(self):
        self.a = set()
    def insert(self, val: int) -> bool:
        if val not in self.a:
            self.a.add(val)
            return True
        else:
            return False
    
    def remove(self, val: int) -> bool:
        if val not in self.a:
            return False
        else:
            self.a = self.a - {val}
            return True

    def getRandom(self) -> int:
        return random.choice(list(self.a))