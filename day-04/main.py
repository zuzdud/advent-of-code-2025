with open("day-04/my_input.txt") as file:
    rolls_grid = [line.rstrip() for line in file]

offset_map = {
    1: (-1, -1), 2: (-1, 0),  3: (-1, 1),
    8: (0, -1),               4: (0, 1),
    7: (1, -1),  6: (1, 0),   5: (1, 1)
}

def check_neighbour(x, y, directions):
    counter = 0
    for index in directions:
        dx, dy = offset_map[index]
        if rolls_grid[x+dx][y+dy] == "@":
            counter += 1

    if counter >= 4:
        return False
    else:
        return True


def can_be_accessed(x, y):
    if x == 0 and y == 0:
        return True
    if x == 0 and y == len(rolls_grid[0])-1:
        return True
    if x == len(rolls_grid)-1 and y == len(rolls_grid[0])-1:
        return True
    if x == len(rolls_grid)-1 and y == 0:
        return True

    if x == 0:
        return check_neighbour(int(x), int(y), [4, 5, 6, 7, 8])

    if x == len(rolls_grid)-1:
        return check_neighbour(int(x), int(y), [4, 1, 2, 3, 8])

    if y == 0:
        return check_neighbour(int(x), int(y), [2, 3, 4, 5, 6])

    if y == len(rolls_grid[0])-1:
        return check_neighbour(int(x), int(y), [2, 1, 8, 7, 6])

    return check_neighbour(int(x), int(y), [1, 2, 3, 4, 5, 6, 7, 8])


rolls_counter = 0
for x in range(0, len(rolls_grid)):
    for y in range(0, len(rolls_grid[0])):
        if rolls_grid[x][y] == "@":
            if can_be_accessed(int(x), int(y)):
                rolls_counter += 1

print(rolls_counter)
