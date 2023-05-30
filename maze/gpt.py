from levels import levels

maze = levels[3]

start = (0, 1)
end = (7, 9)
visited = set()

def solve_maze(maze, current):
    visited.add(current)
    row, col = current

    if current == end:
        return True

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]

        if (
            0 <= new_row < len(maze) and
            0 <= new_col < len(maze[0]) and
            maze[new_row][new_col] not in ('═', '║') and
            (new_row, new_col) not in visited
        ):
            if solve_maze(maze, (new_row, new_col)):
                return True

    return False

if solve_maze(maze, start):
    solution = []
    for row in maze:
        solution.append(''.join(row))
    for row in solution:
        print(row)
else:
    print("The maze does not have a solution.")
