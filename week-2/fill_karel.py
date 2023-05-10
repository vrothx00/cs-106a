from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    fill_one_line()
    return_home()
    while(left_is_clear()):
        move_next_row()
        fill_one_line()
        return_home()
    move_to_end()

def move_to_end():
    while(front_is_clear()):
        move()

def fill_one_line():
    while(front_is_clear()):
        put_beeper()
        move()
    put_beeper()

def return_home():
    turn_right()
    while(front_is_clear()):
        move()
    turn_right()

def turn_right():
    turn_left()
    turn_left()

def move_next_row():
    turn_left()
    move()
    turn_right()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
