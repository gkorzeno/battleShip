import random

def printTitle():
    print("Welcome to Battleship")
    print("")

def initialChoice():
    choice = input("Would you like to play(press p), quit(press q) or read the instructions(press i)")
    while choice != "p" and choice != "i" and choice != "q":
        print("ERROR: Please enter 'p', 'i', or 'q'...")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    return choice

# keeps track of where the ships are without displaying them to the user.
hiddenGrid = [['-' for j in range(10)] for j in range(10)]
grid = [['-' for j in range(10)] for j in range(10)]

ships = {'destroyer': 2, 'submarine': 3, 'cruiser': 3, 'battleship': 4, 'carrier': 5}
total = []
turns = []

# places all the ships in random places without overlapping.
def placeShips(hiddenGrid):
    shipLengths = [5, 4, 3, 3, 2]
    for length in shipLengths:
        while True:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                row = random.randint(0, 9)
                col = random.randint(0, 10 - length)
                if all(hiddenGrid[row][col+i] == '-' for i in range(length)):
                    for i in range(length):
                        hiddenGrid[row][col+i] = length
                        hiddenGrid[row][col+i] = 'O'
                    break
            else:
                row = random.randint(0, 10 - length)
                col = random.randint(0, 9)
                if all(hiddenGrid[row+i][col] == '-' for i in range(length)):
                    for i in range(length):
                        hiddenGrid[row+i][col] = length
                        hiddenGrid[row+i][col] = 'O'
                    break

# prints a grid the user can see, but does not contain the ships positions until there have been hits.
def printGrid(grid):
    print('  ', end='')
    for i in range(10):
        print(i, end=' ')
    print()

    for i, row in enumerate(grid):
        print(i, ' '.join(row))

# Places the user's guess, if its a hit there is an x, if its a miss there is a +
def placeGuess(hiddenGrid, row, col):
    if hiddenGrid[row][col] == 'O':
        grid[row][col] = 'X'
        total.append(1)
        turns.append(1)
        print("You got a hit!")
        return True
    else:
        grid[row][col] = '+'
        turns.append(1)
        print("You missed")
        return False

# goes through all the previous functions to play the game, finishes when all ships are sunk by keeping track of the hits in the total list.
def main():
    printTitle()
    choice = initialChoice()
    if choice == "p":
        placeShips(hiddenGrid)
        num_hits = 0
        while sum(total) < 17:
            printGrid(grid)

            row = int(input('Enter row number (0-9): '))
            col = int(input('Enter column number (0-9): '))

            if placeGuess(hiddenGrid, row, col):
                num_hits
        print("Congrats, you won in " + str(sum(turns)) + " turns!")
    elif choice == "i":
        print("There is a 10x10 grid, on it there are 5 ships. One has a length of 5 spaces, the other is 4, there are two ships that are 3 spaces long, and one is 2 spaces. These ships are placed randomly accross the board and do not overlap. You need to guess the row and column they are in using as few turns as possible. If you hit a ship, an 'X' will appear in the space. If you miss a '+' will appear. Good luck!")
    elif choice == "q":
        print("Bye")
    else:
        print("Please enter 'i', 'q', or 'p'")

if __name__ == "__main__":
    main()