# Tuple Activities
# (Ordered, immutable, indexed)

# Activity 1: Access Elements
colors = ("red", "green", "blue")

print("Activity 1:")
print("First item:", colors[0])
print("Last item:", colors[-1])
print()

# Activity 2: Slicing
numbers = (10, 20, 30, 40, 50)

print("Activity 2:")
print(numbers[1:4])  # (20, 30, 40)
print()

# Activity 3: Tuple Methods
nums = (1, 2, 2, 3, 2)

print("Activity 3:")
print("Count of 2:", nums.count(2))
print("Index of 3:", nums.index(3))
print()

# Activity 4: Tuple Packing & Unpacking
point = (5, 10)
x, y = point

print("Activity 4:")
print("x =", x)
print("y =", y)
print()

# Activity 5: Combine Tuples
t1 = (1, 2)
t2 = (3, 4)

result = (t1 + t2) * 2

print("Activity 5:")
print(result)