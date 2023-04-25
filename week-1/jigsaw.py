from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper
(puzzle piece) and placing it in the right spot. Karel should
end in the same position Karel starts in -- the bottom left
corner of the world.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    walk()
    pick_beeper()
    move()
    turn_left()
    walk()
    put_beeper()
    turn_right()

    move()
    move()
    turn_right()
    turn_left()
    walk()
    move()
    turn_right()

def turn_right():
    turn_left()
    turn_left()

def walk():
    move()
    move()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
