number_of_tree = 4
meters_taken = 6
tree_height = [20,15,8,17]
saw_height = max(tree_height)
total = 0

while total <= meters_taken:
    for i in range(number_of_tree):
        if tree_height[i] > saw_height:
            total += tree_height[i]-saw_height
    saw_height -= 1

print(saw_height)
