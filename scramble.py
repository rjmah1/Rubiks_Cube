import random

# randomize the seed.
random.seed()

# create an enum/list to choose values from ie U D L R F B
PossibleMoveDirection = ['U', 'D', 'L', 'R', 'F', 'B']
PossibleMoveModifier = ['', '2', "'"]

# function to poll a random number between the possible move sets

# if the number corresponds with the same move as previous ie U with U' or U2
# then the value is discarded and a new number is taken


# scramble function
def generate_scramble():
    scrambleLength = random.randint(18, 25)
    counter = 0
    previousMoveDirectionNum = 6 #outside the length of the possibleMoveDirection
    outputScramble = "" #initialize the output string
    while counter <= scrambleLength:
        currentMoveDirectionNum = random.randint(0, 5)
        if currentMoveDirectionNum == previousMoveDirectionNum:
            continue
        previousMoveDirectionNum = currentMoveDirectionNum
        modifier = random.randint(0, 2)
        outputScramble += PossibleMoveDirection[currentMoveDirectionNum]
        outputScramble += PossibleMoveModifier[modifier]
        outputScramble += ' '
        counter += 1
    return outputScramble


if __name__ == "__main__":
    scramble = generate_scramble()
    print(scramble)