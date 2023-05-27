# Write a program that draws a circle wherever the mouse is located on the screen. 
# The user will move their mouse within the canvas, and a circle should be drawn with its left and top x and y values as the x and y values of the user's mouse. 
# Each circle should have a width and height of CIRCLE_SIZE (a constant defined for you in the starter code), and a color of your choosing. 
# The animation should have a delay of DELAY (another constant defined for you in the starter code). 


from graphics import Canvas

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
DELAY = 0.01

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # animation loop 
    while True:
        # get the locations of the mouse
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        
        # check that the mouse location is in bounds
        if mouse_x >= 0 and mouse_x <= CANVAS_WIDTH and mouse_y >=0 and mouse_y <= CANVAS_HEIGHT:
            
            # draw a circle for where the mouse is
            canvas.create_oval(mouse_x, mouse_y, mouse_x + CIRCLE_SIZE, mouse_y + CIRCLE_SIZE, 'cyan')
        
        # typical animation loop code 
        # canvas.mainloop()  # Ignore this line for current solutions.
        time.sleep(DELAY)


if __name__ == "__main__":
    main()