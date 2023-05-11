from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    for i in range(4):
        build_column()
        return_to_base()
        move_forward()

# help beeper to return to base
def return_to_base():
    turn_around()
    while front_is_clear():
        move()
    turn_left()

# build one column wih beepers
def build_column():
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

# help beeper to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# help beeper to turn around
def turn_around():
    turn_left()
    turn_left()

def move_forward():
    if front_is_clear():
        for i in range(4):
            move()



if __name__ == '__main__':
    main()
