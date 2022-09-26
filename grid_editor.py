import tkinter as tk
from tkinter import Tk, Frame, Label
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

SCALE_FACTOR = 50
BACKGROUND_COLOR = '#dddddd'


class GridEditor(tk.Canvas):
    """ 
    Provides the graphical surface that allows the user to draw figures. 
    """

    def __init__(self, root, rows, columns):
        """
        Initializes the grid with a given Tk root and
        rows x columns dimensions.
        """
        super().__init__(root, width=SCALE_FACTOR*columns, 
                         height=SCALE_FACTOR*rows, 
                         cursor='crosshair',
                         bg=BACKGROUND_COLOR,
                         highlightbackground=BACKGROUND_COLOR)

        self.root = root
        self.rows = rows
        self.columns = columns
        self.erasing = False

        self.bind('<KeyPress>', self.keypressed)
        self.bind('<Motion>', self.mouse_moved)
        self.bind('<Button-1>', self.mouse_pressed)
        self.bind('<Shift-Button-3>', lambda event: self.clear())
        self.bind('<ButtonRelease-1>', self.mouse_released)

        self.square_array = [[None for c in range(self.columns)] for r in range(self.rows)]

        # Add the editable squares
        for r in range(self.rows):
            for c in range(self.columns):
                x, y = self.to_x_y(r, c)
                span = SCALE_FACTOR - 1
                rect = self.create_rectangle(x, y, x + span, y + span,
                                                    outline='lightgray', fill='white')
                self.square_array[r][c] = rect

        self.dragging = False


    def to_row_column(self, x, y):
        """
        Maps an (x, y) window coordinate to a row, column grid location.
        """
        row = int(y / SCALE_FACTOR) % self.rows
        col = int(x / SCALE_FACTOR) % self.columns
        return row, col


    def to_x_y(self, row, column):
        """
        Maps a row, column grid location to an (x, y) window coordinate.
        """
        x = SCALE_FACTOR * column
        y = SCALE_FACTOR * row 
        return x, y


    def clear(self):
        """
        Makes the grid empty.
        """
        for row in range(self.rows):
            for col in range(self.columns):
                self.itemconfig(self.square_array[row][col], fill='white')


    def keypressed(self, event):
        """
        Invokes a method in response to a user keypress.
        """
        ch = event.char.lower()
        if len(ch) == 1:
            if ch == 'c':
                print(self.flatten())
            elif ch == 'e':   
                if self.erasing == True:
                    self.erasing = False
                    self.config(cursor='crosshair')
                else:
                    self.erasing = True
                    self.config(cursor='pirate')
            elif event.state & 0x1 != 0 and ord(ch) == 27:   # Escape key with shift
                self.clear()
            elif ord(ch) == 27:   # Escape key
                if messagebox.askokcancel('Clear', 'Do you really want to clear?'):
                    self.clear()
            elif ch == 'm':
                print('Memorize pair')
            elif ch == 'r':
                print('Recall pair')


    def modify_square(self, x, y):
        """
        Depending on the current editing mode, turns on or off a grid cell 
        that contains the window coordinate (x, y).
        """
        row, col = self.to_row_column(x, y)
        square = self.square_array[row][col]
        color = 'white' if self.erasing else 'blue'
        self.itemconfig(square, fill=color)


    def mouse_moved(self, event):
        """
        Called in response to mouse movement.
        If the button is depressed, depending on 
        the current editing mode, the motion turns
        on or off the grid cell under the mouse cursor.
        """
        self.focus_set()
        if self.dragging:
            self.modify_square(event.x, event.y)


    def mouse_pressed(self, event):
        """
        Subsequent mouse movements will be "dragging" 
        events.
        """
        self.dragging = True


    def mouse_released(self, event):
        """
        Called in response to releasing the mouse button.
        Depending on the current editing mode, the motion turns
        on or off the grid cell under the mouse cursor.
        Subsequent mouse movements will be "NOT dragging" 
        events.
        """
        self.dragging = False
        self.modify_square(event.x, event.y)


    def assign(self, bitstring):
        """
        Fills the grid row by row with the contents of the bitstring.
        The grid dimensions must be compatible with the bitstring's length.
        """
        assert(self.rows * self.columns == len(bitstring))
        self.clear()
        index = 0
        for row in range(self.rows):
            for col in range(self.columns):
                if bitstring[index] == '1':
                    square = self.square_array[row][col]
                    self.itemconfig(square, fill='blue')
                index += 1

        self.root.update()


    def flatten(self):
        """
        Returns the contents of the grid as a flattened bitstring.
        """
        result = ''
        for row in range(self.rows):
            for col in range(self.columns):
                color = self.itemcget(self.square_array[row][col], 'fill')
                result += '0' if color == 'white' else '1'
        return result
