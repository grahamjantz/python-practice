global_char_x_pos = 1
global_char_y_pos = 0

PATH = ' '

back = '█'
wall = '#'
char = 'X'
endd = 'O'

ver1 = '║'
ver2 = '╣'
ver3 = '╠'

hor1 = '═'
hor2 = '╦'
hor3 = '╩'

cor1 = '╔'
cor2 = '╗'
cor3 = '╝'
cor4 = '╚'

cros = '╬'

level_one = [
    [cor1, hor1, hor1, hor1, hor1, hor1, cor2],
    [ver1, PATH, PATH, PATH, PATH, PATH, ver1],
    [ver3, hor1, hor1, hor1, hor1, PATH, ver1],
    [ver1, PATH, PATH, PATH, PATH, PATH, ver1],
    [ver1, PATH, hor1, hor1, hor1, hor1, ver2],
    [ver1, PATH, PATH, PATH, PATH, PATH, ver1],
    [cor4, hor1, hor1, hor1, hor1, endd, cor3]
]

level_two = [
    [cor1, hor1, hor1, hor1, hor1, hor1, hor1, hor2, hor1, hor2, hor1, cor2],
    [ver1, PATH, PATH, PATH, PATH, PATH, PATH, ver1, PATH, ver1, PATH, ver1],
    [ver3, hor1, hor1, cor2, PATH, ver1, PATH, ver1, PATH, ver1, PATH, ver1],
    [ver1, PATH, PATH, ver1, PATH, cor4, hor1, cor3, PATH, ver1, PATH, ver1],
    [ver3, hor1, PATH, ver1, PATH, PATH, PATH, PATH, PATH, PATH, PATH, ver1],
    [ver1, PATH, PATH, cor4, hor1, PATH, ver1, PATH, ver1, PATH, hor1, ver2],
    [ver1, PATH, PATH, PATH, PATH, PATH, ver1, PATH, ver1, PATH, PATH, ver1],
    [cor4, hor1, hor1, hor1, hor1, hor1, hor3, hor1, hor3, hor1, endd, cor3],
]

level_three = [
    [cor1, hor1, hor1, hor1, hor1, hor2, hor1, hor2, hor1, hor1, hor1, hor1, hor1, hor1, cor2, ],
    [ver1, PATH, PATH, PATH, PATH, ver1, PATH, ver1, PATH, PATH, PATH, PATH, PATH, PATH, ver1, ],
    [ver3, hor1, hor1, hor1, PATH, ver1, PATH, cor4, hor1, PATH, PATH, cor1, hor1, PATH, ver1, ],
    [ver1, PATH, PATH, PATH, PATH, ver1, PATH, PATH, PATH, PATH, cor1, cor3, PATH, PATH, ver1, ],
    [ver3, hor1, hor1, hor1, PATH, ver1, PATH, ver1, PATH, hor1, cros, hor1, PATH, hor1, ver2, ],
    [ver1, PATH, PATH, PATH, PATH, ver1, PATH, ver1, PATH, PATH, ver1, PATH, PATH, PATH, ver1, ],
    [ver1, PATH, hor1, hor1, hor1, cor3, PATH, cor4, hor2, hor1, hor3, hor1, hor1, PATH, ver1, ],
    [ver1, PATH, PATH, PATH, PATH, PATH, PATH, PATH, ver1, PATH, PATH, PATH, PATH, PATH, ver1, ],
    [ver3, hor1, hor1, hor1, hor1, hor1, hor1, hor1, cor3, PATH, hor1, hor1, hor1, hor1, ver2, ],
    [ver1, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, ver1, ],
    [ver1, PATH, hor1, hor1, hor1, hor1, hor2, hor1, hor1, hor1, hor1, hor1, hor1, PATH, ver1, ],
    [ver1, PATH, PATH, PATH, PATH, PATH, ver1, PATH, PATH, PATH, PATH, PATH, PATH, PATH, ver1, ],
    [ver3, hor1, hor1, PATH, hor1, hor1, cros, hor1, hor1, PATH, cor1, hor1, hor1, hor1, ver2, ],
    [ver1, PATH, PATH, PATH, PATH, PATH, ver1, PATH, PATH, PATH, ver1, PATH, PATH, PATH, ver1, ],
    [ver1, PATH, cor1, hor1, hor1, hor1, cor3, PATH, cor1, hor1, cor3, PATH, ver1, PATH, ver1, ],
    [ver1, PATH, ver1, PATH, PATH, PATH, PATH, PATH, ver1, PATH, PATH, PATH, ver1, PATH, ver1, ],
    [ver1, PATH, ver1, PATH, hor1, hor1, hor1, hor1, cor3, PATH, ver1, PATH, ver1, PATH, ver1, ],
    [ver1, PATH, ver1, PATH, PATH, PATH, PATH, PATH, PATH, PATH, ver1, PATH, ver1, PATH, ver1, ],
    [cor4, hor1, hor3, hor1, hor1, hor1, hor1, hor1, hor1, hor1, hor3, hor1, hor3, endd, cor3, ],
]
level_four = [
    [cor1, hor1, hor2, hor1, hor1, hor1, hor1, hor1, hor1, hor1, hor1, hor1, hor1, hor1, hor1, hor1, hor1, hor1, hor1, hor2, hor1, hor1, hor1, hor1, hor2, hor1, hor1, hor1, hor1, hor1, cor2, ],
    [ver1, PATH, ver1, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, ver1, PATH, PATH, PATH, PATH, ver1, PATH, PATH, PATH, PATH, PATH, ver1, ],
    [ver1, PATH, ver1, PATH, ver1, PATH, cor1, hor1, hor1, hor1, hor2, hor1, hor1, hor1, hor1, hor1, PATH, hor1, hor1, cor3, PATH, cor1, hor1, PATH, ver1, PATH, cor1, hor1, cor2, PATH, ver1, ],
    [ver1, PATH, ver1, PATH, ver1, PATH, ver1, PATH, PATH, PATH, ver1, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, ver1, PATH, PATH, ver1, PATH, ver1, PATH, ver1, PATH, ver1, ],
    [ver1, PATH, ver1, PATH, ver1, PATH, ver1, PATH, ver1, PATH, PATH, PATH, cor1, hor1, PATH, cor1, hor1, hor1, hor1, hor1, hor1, cor3, PATH, cor1, cor3, PATH, ver1, PATH, ver1, PATH, ver1, ],
    [ver1, PATH, ver1, PATH, ver1, PATH, PATH, PATH, ver3, hor1, hor1, hor1, ver2, PATH, PATH, ver1, PATH, PATH, PATH, PATH, PATH, PATH, PATH, ver1, PATH, PATH, ver1, PATH, ver1, PATH, ver1, ],
    [ver1, PATH, ver1, PATH, ver1, PATH, hor1, hor1, ver2, PATH, PATH, PATH, ver1, PATH, cor1, hor3, hor1, hor1, hor1, hor1, cor2, PATH, PATH, ver1, PATH, cor1, cor3, PATH, ver1, PATH, ver1, ],
    [ver1, PATH, PATH, PATH, ver1, PATH, PATH, PATH, cor4, hor1, hor1, PATH, ver1, PATH, ver1, PATH, PATH, PATH, PATH, PATH, ver1, PATH, hor1, cor3, PATH, ver1, PATH, PATH, ver1, PATH, ver1, ],
    [ver1, PATH, cor1, hor1, hor3, hor1, cor2, PATH, PATH, PATH, PATH, PATH, ver1, PATH, ver1, PATH, cor1, hor1, cor2, PATH, PATH, PATH, PATH, PATH, PATH, ver1, PATH, cor1, cor3, PATH, ver1, ],
    [ver1, PATH, ver1, PATH, PATH, PATH, cor4, hor1, hor2, hor1, hor2, hor1, cor3, PATH, cor4, PATH, ver1, PATH, ver1, PATH, cor1, hor1, hor1, hor1, hor1, cor3, PATH, PATH, PATH, PATH, ver1, ],
    [ver1, PATH, ver1, PATH, ver1, PATH, PATH, PATH, ver1, PATH, ver1, PATH, PATH, PATH, PATH, PATH, ver1, PATH, cor4, hor1, ver2, PATH, PATH, PATH, PATH, PATH, PATH, PATH, cor1, hor1, ver2, ],
    [ver1, PATH, PATH, PATH, ver1, PATH, cor1, PATH, ver1, PATH, ver1, PATH, cor1, hor1, hor1, hor1, cor3, PATH, PATH, PATH, ver1, PATH, ver1, PATH, ver1, PATH, PATH, hor1, cor3, PATH, ver1, ],
    [ver3, hor1, hor1, hor1, ver2, PATH, ver1, PATH, PATH, PATH, ver1, PATH, ver1, PATH, PATH, PATH, PATH, PATH, ver1, PATH, cor4, hor1, hor3, hor1, ver2, PATH, PATH, PATH, PATH, PATH, ver1, ],
    [ver1, PATH, PATH, PATH, cor4, hor1, cros, hor1, hor1, PATH, ver1, PATH, ver1, PATH, cor1, hor1, hor1, hor1, cor3, PATH, PATH, PATH, PATH, PATH, ver1, PATH, ver1, PATH, ver1, PATH, ver1, ],
    [ver1, PATH, ver1, PATH, PATH, PATH, ver1, PATH, PATH, PATH, ver1, PATH, cor4, hor1, cor3, PATH, PATH, PATH, PATH, PATH, cor1, hor1, hor1, PATH, ver3, hor1, hor3, hor1, ver2, PATH, ver1, ],
    [ver1, PATH, cor4, hor1, cor2, PATH, PATH, PATH, ver1, PATH, ver1, PATH, PATH, PATH, PATH, PATH, cor1, hor1, hor1, PATH, ver1, PATH, PATH, PATH, ver1, PATH, PATH, PATH, ver1, PATH, ver1, ],
    [ver1, PATH, PATH, PATH, cor4, hor1, hor2, hor1, cor3, PATH, cor4, hor1, hor1, cor2, PATH, cor1, cor3, PATH, PATH, PATH, cor4, hor1, hor1, hor1, hor3, hor1, hor1, PATH, ver1, PATH, ver1, ],
    [ver1, PATH, PATH, PATH, PATH, PATH, ver1, PATH, PATH, PATH, PATH, PATH, PATH, ver1, PATH, ver1, PATH, PATH, ver1, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, ver1, PATH, ver1, ],
    [cor4, hor1, hor1, hor1, hor1, hor1, hor3, hor1, hor1, hor1, hor1, hor1, hor1, hor3, hor1, hor3, hor1, hor1, hor3, hor1, hor1, hor1, hor1, hor1, hor1, hor1, hor1, hor1, hor3, endd, cor3, ],
]


levels = [level_one, level_two, level_three, level_four] 



def print_maze(maze):
    maze[global_char_y_pos][global_char_x_pos] = char
    for row in maze:
        print('\t\t', end='')
        for block in row:
            print(block, end='')
        print('')
    print('\n')


def print_all_levels(levs):
    count = 1
    for level in levs:
        print('Level ', count, ':')
        print_maze(level)
        count += 1

# print_all_levels(levels)

# print_maze(level_four)