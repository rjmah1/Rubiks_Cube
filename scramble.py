import random

# randomize the seed.
random.seed()

# create an enum/list to choose values from ie U D L R F B
Possible_move_direction = ['U', 'D', 'L', 'R', 'F', 'B']
Possible_move_modifier = ['', '2', "'"]

# function to poll a random number between the possible move sets

# if the number corresponds with the same move as previous ie U with U' or U2
# then the value is discarded and a new number is taken


# scramble function
def generate_scramble():
    scramble_length = random.randint(20, 30)
    counter = 0
    previous_move_direction_num = 6 #outside the length of the possibleMoveDirection
    output_scramble = "" #initialize the output string
    while counter <= scramble_length:
        current_move_direction_num = random.randint(0, 5)
        if current_move_direction_num != previous_move_direction_num:
            previous_move_direction_num = current_move_direction_num
            modifier = random.randint(0, 2)
            output_scramble += Possible_move_direction[current_move_direction_num]
            output_scramble += Possible_move_modifier[modifier]
            output_scramble += ' '
            counter += 1
    return output_scramble


if __name__ == "__main__":
    scramble = generate_scramble()
    print(scramble)
