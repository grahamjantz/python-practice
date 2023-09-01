from levels import levels

print("Welcome to the Maze!\n")
print('Your goal is to get your character: X to the exit: O without touching any of the walls: #\n')
print('Good luck!\n')

PATH = ' '
wall = '#'
char = 'X'
end = 'O'

current_level = 1
global_play_game = True
global_char_x_pos = 1
global_char_y_pos = 0


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
    print('\n\t//═══════════════WIN═══════════════//\n')

def move_up(maze, char_x_pos, char_y_pos):
    if char_y_pos >= 0:
        if maze[char_y_pos - 1][char_x_pos] == end:
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
        if maze[char_y_pos + 1][char_x_pos] == end:
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
        if maze[char_y_pos][char_x_pos -1] == end:
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
        if maze[char_y_pos][char_x_pos + 1] == end:
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
    print('\n\t\tCurrent Level: Level ', current_level, '\n')
    play_level = levels[current_level - 1]
    print_maze(play_level)
    move = input('\n\t\t    Move: W,A,S,D: \n\t\t    ')

    if move == 'W' or move == 'w':
        res = move_up(play_level, global_char_x_pos, global_char_y_pos)
        if res == False:
            global_play_game = False
        elif res == 2:
            global_char_x_pos = 1
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
            global_char_x_pos = 1
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
            global_char_x_pos = 1
            global_char_y_pos = 0
            current_level += 1
    elif move == 'D' or move == 'd':
        res = move_right(play_level, global_char_x_pos, global_char_y_pos)
        if res == False:
            global_play_game = False
        elif res == 2:
            global_char_x_pos = 1
            global_char_y_pos = 0
            current_level += 1
        else:
            global_char_x_pos += 1
            play_level[global_char_y_pos][global_char_x_pos - 1] = PATH
    else:
        print('Invalid move! W,A,S,D to move!')
    if current_level > len(levels):
        print('\n\t\tThank you for playing! \n\tYou have beaten all the levels so far!\n')
        global_play_game = False