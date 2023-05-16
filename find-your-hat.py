import random 

print('Hello welcome to Find Your Hat\n')

field_character = '░'

field = []
num_of_rows = int(input("How many rows would you like to use? "))
num_of_columns = int(input("How many Columns? "))
difficulty = int(input("What difficulty would you like? (1-10) "))
difficulty /= 10
print(difficulty)

diff = round(num_of_columns * difficulty)
print(diff)

char_x_index = 0
char_y_index = 0

play_game = True

def generate_field():
    for i in range(num_of_rows):
        temp = []
        for i in range(num_of_columns):

            temp.append(field_character)
        for i in range(diff):
            index = random.randint(0,num_of_columns -1)
            temp[index] = 'O'
        
        field.append(temp)
    hat_x_index = random.randint(0, num_of_rows - 1)
    hat_y_index = random.randint(0, num_of_columns - 1)
    field[hat_x_index][hat_y_index] = "^"

generate_field()

def print_field():
    field[char_y_index][char_x_index] = "X"
    for num_of_rows in field:
        for char in num_of_rows:
            print(char, end='')
        print('')

print_field()


while play_game == True:
    move = input('Move? W, A, S, D ')
    if move == 'W' or move == 'w':
        if char_y_index == 0:
            play_game = False
            print('Lose! Out of bounds!')
        elif field[char_y_index - 1][char_x_index] == "O":
            play_game = False
            print('Lose! Fell in hole!')
        elif field[char_y_index - 1][char_x_index] == "^":
            play_game = False
            print('Win! You found your hat!')
        else: 
            field[char_y_index][char_x_index] = field_character
            char_y_index -= 1
            print_field()
    elif move == 'A' or move == 'a':
        if char_x_index == 0:
            play_game = False
            print('Lose! Out of bounds!')
        elif field[char_y_index][char_x_index - 1] == "O":
            play_game = False
            print('Lose! Fell in hole!')
        elif field[char_y_index][char_x_index - 1] == "^":
            play_game = False
            print("Win! You found your hat!")
        else:
            field[char_y_index][char_x_index] = field_character
            char_x_index -= 1
            print_field()
    elif move == 'S' or move == 's':
        if field[char_y_index + 1][char_x_index] == "O":
            play_game = False
            print('Lose! Fell in hole!')
        elif field[char_y_index + 1][char_x_index] == "^":
            play_game = False
            print("Win! You found your hat!")
        elif char_y_index < num_of_rows-1:
            field[char_y_index][char_x_index] = field_character
            char_y_index += 1
            print_field()
        else:
            play_game = False
            print('Lose! Out of bounds!')
    elif move == 'D' or move == 'd':
        if field[char_y_index][char_x_index + 1] == "O":
            play_game = False
            print('Lose! Fell in hole!')
        elif field[char_y_index][char_x_index + 1] == "^":
            play_game = False
            print("Win! You found your hat!")
        elif char_x_index < num_of_columns-1:
            field[char_y_index][char_x_index] = field_character
            char_x_index += 1
            print_field()
        else:
            play_game = False
            print('Lose! Out of bounds!')
    else:
        print('Invalid! Enter W, A, S, D to move!')