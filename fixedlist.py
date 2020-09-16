# Basic data structure that creates a list of fixed length, and pops excess elements from the list whenever a new addition makes the list exceed the length.
# (First in first out pops)
class fixedlist(list):
    def __init__(self, length):
        super().__init__()
        self.length = length;
    def append(self, item):
        list.append(self, item)
        if len(self) > self.length: del self[0]
