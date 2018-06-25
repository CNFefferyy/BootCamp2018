# shut_the_box.py

# import statements
import box
import sys
import numpy as np
import random
import time

# Order of command line arguments: file name, player's name, time limits

# if there are exactly 3 command line arguments, start the game
if len(sys.argv) == 3:

    # save player name
    playerName = sys.argv[1]
    # save time limit as an int
    timeLimit = float(sys.argv[2]) # time limit, in seconds
    # initialize a list of integers 1 through 9
    remaining = list(np.arange(9)+1)

    remainingTime = timeLimit

    while remainingTime > 0:
        # Begin the timer for this loop
        startLoopTime = time.time()
        # Sum the elements of the player's remaining number list to see how many
        # dice should be rolled
        sumRemaining = sum(remaining)
        roll1 = np.random.randint(1,6)
        # if the sum of the player’s remaining numbers is 6 or less,
        # role only one die.
        if sumRemaining <= 6:
            roll2 = 0
        else:
            roll2 = np.random.randint(1,6)
        sumRolls = roll1 + roll2

        # Decrement the amount of time remaining
        endLoopTime = time.time()
        loopTime = endLoopTime - startLoopTime
        remainingTime -= loopTime

        # Update the player on the status of the game:
        print("\nNumbers flushleft: " + str(remaining)
              + "\nRoll : " + str(sumRolls)
              + "\nSeconds left " + str(round(remainingTime, 2)))

        # Check if there exists a combination of the entries
        # of 'remaining' that sum up to
        isvalidRoll = box.isvalid(sumRolls, remaining)

        # If not, then the game is over and the player lost.
        if not isvalidRoll:
            print("\nScore for player " + playerName + ": 0 points")
            print("Time played: " + str(round((timeLimit - remainingTime), 2)) + " seconds.")
            print('You lost, ' + playerName + ".")
            break

        # Loop until the player enters valid input (but if they run out of time
        # while in this while loop, they still loose upon entering correct numbers)
        correctInput = False
        while not correctInput:

            # Begin the timer for this loop
            startLoopTime = time.time()

            inputVals = input("Numbers to eliminate: ")
            choices = box.parse_input(inputVals, remaining)
            if choices != []:
                # See if the player's choices sum to the correct number
                if sum(choices) == sumRolls:
                    correctInput = True
                    break
            print("Invalid input. Try again.")

            # Decrement the amount of time remaining
            endLoopTime = time.time()
            loopTime = endLoopTime - startLoopTime
            remainingTime -= loopTime

            print("\nSeconds left " + str(round(remainingTime, 2)))


        # Remove the player's choices
        for x in choices:
            remaining.remove(x)

        # Decrement the amount of time remaining
        endLoopTime = time.time()
        loopTime = endLoopTime - startLoopTime
        remainingTime -= loopTime

        if remainingTime < 0:
            print("\nScore for player " + playerName + ": 0 points")
            print("You ran out of time and lost, " + playerName + "!")
            print("Time played: " + str(round((timeLimit - remainingTime), 2)) + " seconds.")
            break

        if not remaining:
            print("\nScore for player " + playerName + ": 1 point")
            print('You won, ' + playerName + "!")
            print("Time played: " + str(round((timeLimit - remainingTime), 2)) + " seconds.")
# if there are not 3 command line arguments, don't start the game
else:
    # Don't start game
    print("Need exactly three command line arguments to play the game.")
