print("Welcome to the Maze!\n")
print('Your goal is to get your character: X to the exit: O without touching any of the walls: #\n')
print('Good luck!\n')

PATH = '░'
wall = '#'
char = 'X'
end = 'O'
vert = '║'
hor = '═'
cor1 = '╔'
cor2 = '╗'
cor3 = '╝'
cor4 = '╚'
# PATH = 'v'
current_level = 1
global_play_game = True
global_char_x_pos = 1
global_char_y_pos = 0

level_one = [
    [cor1, hor, hor, hor, hor, hor, cor2],
    [vert, PATH, PATH, PATH, PATH, PATH, vert],
    ['╠', hor, hor, hor, hor, PATH, vert],
    [vert, PATH, PATH, PATH, PATH, PATH, vert],
    [vert, PATH, hor, hor, hor, hor, '╣'],
    [vert, PATH, PATH, PATH, PATH, PATH, vert],
    [cor4, hor, hor, hor, hor, end, cor3]
]

level_two = [
    [cor1, hor, hor, hor, hor, hor, hor, hor, hor, hor, hor, cor2],
    [vert, PATH, wall, wall, wall, wall, wall, wall, wall, wall, wall, vert],
    [vert, PATH, PATH, PATH, PATH, PATH, PATH, wall, wall, PATH, wall, vert],
    ['╠', hor, hor, cor2, PATH, wall, PATH, wall, wall, PATH, wall, vert],
    [vert, PATH, PATH, vert, PATH, wall, wall, wall, wall, PATH, PATH, vert],
    ['╠', hor, PATH, vert, PATH, PATH, PATH, PATH, PATH, PATH, PATH, vert],
    [vert, PATH, PATH, cor4, hor, PATH, vert, PATH, vert, PATH, hor, '╣'],
    [vert, PATH, PATH, PATH, PATH, PATH, vert, PATH, vert, PATH, PATH, vert],
    [cor4, hor, hor, hor, hor, hor, '╩', hor, '╩', hor, end, cor3],
]

level_three = [
    [PATH, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall],
    [PATH, PATH, wall, wall, wall, wall, wall, PATH, PATH, PATH, wall, PATH, PATH, PATH, wall],
    [wall, PATH, wall, PATH, PATH, PATH, wall, PATH, wall, PATH, PATH, PATH, wall, PATH, wall],
    [wall, PATH, PATH, PATH, wall, wall, wall, PATH, wall, wall, wall, wall, wall, PATH, wall],
    [wall, PATH, wall, wall, PATH, PATH, wall, PATH, wall, PATH, PATH, PATH, PATH, PATH, wall],
    [wall, PATH, wall, PATH, wall, PATH, wall, PATH, wall, PATH, wall, wall, wall, wall, wall],
    [wall, PATH, wall, PATH, wall, PATH, wall, PATH, wall, PATH, PATH, PATH, PATH, PATH, wall],
    [wall, PATH, PATH, PATH, wall, PATH, wall, PATH, wall, wall, wall, wall, wall, PATH, wall],
    [wall, PATH, wall, PATH, PATH, PATH, wall, PATH, wall, PATH, PATH, PATH, PATH, PATH, wall],
    [wall, PATH, PATH, PATH, PATH, PATH, PATH, PATH, wall, wall, wall, wall, wall, PATH, wall],
    [wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, PATH, end],
]


levels = [level_two, level_three] 

def print_maze(maze):
    maze[global_char_y_pos][global_char_x_pos] = char
    for row in maze:
        print('\t\t', end='')
        for block in row:
            print(block, end='')
        print('')

def out_of_bounds():
    print('Lose! Out of bounds!')

def hit_wall():
    print('Lose! You hit a wall!')
    
def win():
    print('//==========-----WIN-----==========//')

def move_up(maze, char_x_pos, char_y_pos):
    if char_y_pos >= 0:
        if maze[char_y_pos - 1][char_x_pos] == 'O':
            win()
            return 2
        elif maze[char_y_pos - 1][char_x_pos] != PATH:
            hit_wall()
            return False
        return 1
    else:
        out_of_bounds()
        return False
    
def move_down(maze, char_x_pos, char_y_pos):
    if char_y_pos < len(maze) - 1:
        if maze[char_y_pos + 1][char_x_pos] == 'O':
            win()
            return 2
        elif maze[char_y_pos + 1][char_x_pos] != PATH:
            hit_wall()
            return False
        return 1
    else:
        out_of_bounds()
        return False

def move_left(maze, char_x_pos, char_y_pos):
    if char_x_pos > -1:
        if maze[char_y_pos][char_x_pos -1] == 'O':
            win()
            return 2
        elif maze[char_y_pos][char_x_pos - 1] != PATH:
            hit_wall()
            return False
        return 1
    else:
        out_of_bounds()
        return False

def move_right(maze, char_x_pos, char_y_pos):
    if char_x_pos < len(maze[0]):
        if maze[char_y_pos][char_x_pos + 1] == 'O':
            win()
            return 2
        elif maze[char_y_pos][char_x_pos + 1] != PATH:
            hit_wall()
            return False
        return 1
    else:
        out_of_bounds()
        return False




while global_play_game == True:
    print('\n\tCurrent Level: Level ', current_level, '\n')
    play_level = levels[current_level - 1]
    print_maze(play_level)
    move = input('\n\t    Move: W,A,S,D: \n\t    ')

    if move == 'W' or move == 'w':
        res = move_up(play_level, global_char_x_pos, global_char_y_pos)
        if res == False:
            global_play_game = False
        elif res == 2:
            global_char_x_pos = 0
            global_char_y_pos = 0
            current_level += 1
        else:
            global_char_y_pos -= 1
            play_level[global_char_y_pos + 1][global_char_x_pos] = PATH
    elif move == 'A' or move == 'a':
        res = move_left(play_level, global_char_x_pos, global_char_y_pos)
        if res == False:
            global_play_game = False
        elif res == 2:
            global_char_x_pos = 0
            global_char_y_pos = 0
            current_level += 1
        else:
            global_char_x_pos -= 1
            play_level[global_char_y_pos][global_char_x_pos + 1] = PATH
    elif move == 'S' or move == 's':
        res = move_down(play_level, global_char_x_pos, global_char_y_pos)
        if res == False:
            global_play_game = False
        elif res == 1:
            global_char_y_pos += 1
            play_level[global_char_y_pos - 1][global_char_x_pos] = PATH
        elif res == 2:
            global_char_x_pos = 0
            global_char_y_pos = 0
            current_level += 1
    elif move == 'D' or move == 'd':
        res = move_right(play_level, global_char_x_pos, global_char_y_pos)
        if res == False:
            global_play_game = False
        elif res == 2:
            global_char_x_pos = 0
            global_char_y_pos = 0
            current_level += 1
        else:
            global_char_x_pos += 1
            play_level[global_char_y_pos][global_char_x_pos - 1] = PATH
    else:
        print('Invalid move! W,A,S,D to move!')