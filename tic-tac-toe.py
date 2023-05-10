from x_or_o import XorO
import os


# create a function for creating the playing board
def create_board(values_list):
    return [[values_list[0].fill, "|", values_list[1].fill, "|", values_list[2].fill], ["----------"], [values_list[3].fill, "|", values_list[4].fill, "|", values_list[5].fill], ["----------"], [values_list[6].fill, "|", values_list[7].fill, "|", values_list[8].fill]]


# create a function for printing the board 
def print_board(board):
    for line in board:
        print(*line)


# create a function to carry out logic for taking a turn, including defensive programming for inputs
def take_turn(player_no):
    print(f"Player {player_no}: choose your location from the grid")
    while True:
        try:
            turn = int(input())
            if turn in range(1, 10):
                if values[turn-1].fill == " ":
                    if player_no == 1:
                        values[turn-1].x()
                        check_win(turn, "X")
                    else:
                        values[turn-1].o()
                        check_win(turn, "O")
                    print_board(create_board(values))
                    
                    break
                else:
                    print("Sorry, that location is taken. Try another location.")
            else:
                print("Sorry, that's not right. Please input a number between 1-9")
        except ValueError:
            print("Sorry, that's not right. Please input a number between 1-9")
        

# create a function to check for a winning combination
def check_win(location, fill):
    winning_combos = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for combo in winning_combos:
        if location in combo:
            matching = []
            for number in combo:
                if values[number - 1].fill == fill:
                    matching.append("y")
            if matching == ["y", "y", "y"]:
                print_board(create_board(values))
                print(f"{fill} wins")
                return os._exit(0)
            

# create a list of objects for the gameplay
values = [XorO(n) for n in range(1,10)]

# define a location board to show which keys are associated with the locations
location_board = [[values[0].id, "|", values[1].id, "|", values[2].id], ["----------"], [values[3].id, "|", values[4].id, "|", values[5].id], ["----------"], [values[6].id, "|", values[7].id, "|", values[8].id]]

# set up the gameplay in the console
print(f"Use the numbers keypad to pick locations: {print_board(location_board)}")

i = 1
while i < 10:
    if i % 2 == 1:
        take_turn(1)
    else:
        take_turn(2)
    i += 1

print("Game drawn.")
