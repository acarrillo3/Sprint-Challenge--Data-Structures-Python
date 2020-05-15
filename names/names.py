import time

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

class BinaryTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None 

    def insert(self, value):
        if self.value == None:
            self.value = value

        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        else: 
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)   
    def contains(self, target):

        if self.value == target:
            duplicates.append(self.value)

        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if target > self.value:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target) 

# tree = BinaryTree()

# for names in names_1:
#     tree.insert(names)

# for names in names_2:
#     tree.contains(names)


names1 = list(set(names_1))
names2 = list(set(names_2))

names = sorted(names1 + names2)

for i in range(len(names) - 1):
    if names[i] == names[i+1]:
        duplicates.append(names[i])




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
