grid = [
    [".", ".", ".", ".", ".", "."],
    [".", "O", "O", ".", ".", "."],
    ["O", "O", "O", "O", ".", "."],
    ["O", "O", "O", "O", "O", "."],
    [".", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "."],
    ["O", "O", "O", "O", ".", "."],
    [".", "O", "O", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]

# Print every first item on the list of list
# grid[0][0]
# grid[1][0]
# get the list length
for y_index, _ in enumerate(grid[0]):
    for x_index, _ in enumerate(grid):
        print(_[y_index], end="")
    print()
