from tkinter import Tk, Frame, Button
from tkinter import messagebox
import numpy as np

from bam import BAM

from grid_editor import GridEditor, BACKGROUND_COLOR

def symbol_to_list(grid_symbol,rows,columns):
    
    bitstring2 = grid_symbol.flatten()
    bitstring = np.array([int(x) for x in bitstring2])
    bitstring = bitstring.reshape(rows,columns)
    print(f"naber : {bitstring}")
    return bitstring


def list_to_bitstring(lst):
    result = ''
    for bit in lst:
        result += '0' if bit == 0 else '1'
    return result


class BAM_UI:
    """
    Defines the user interface of the BAM.
    """

    def __init__(self, bam, A_rows, A_columns, B_rows, B_columns):
        """
        Initializes the grid editor panels and wires up event
        listeners.
        """
        root = Tk()
        root.configure(bg=BACKGROUND_COLOR)
        root.geometry('800x600')
        root.title('BAM')
        
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(1, weight=1)
        self.root = root

        self.bam = bam
        self.Arows = A_rows
        self.Acolumns = A_columns
        self.Brows = B_rows
        self.Bcolumns = B_columns

        self.A_symbol = GridEditor(root, A_rows, A_columns) 
        self.B_symbol = GridEditor(root, B_rows, B_columns)
        
        self.A_symbol.grid(row=0, column=0)
        self.B_symbol.grid(row=0, column=1)
        
        button_frame = Frame(root, bg=BACKGROUND_COLOR)
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_columnconfigure(2, weight=1)
        button_frame.grid_columnconfigure(3, weight=1)
        button_frame.grid_columnconfigure(4, weight=1)

        clear_button = Button(button_frame, text='Clear', bg='#DEFEFE', 
                              command=self.clear)
        clear_button.grid(row=0, column=0, padx=60)

        memorize_button = Button(button_frame, text='Memorize', bg='#FBFAB8',
                                 command=self.memorize_pair)
        memorize_button.grid(row=0, column=1, padx=20)

        recall_button = Button(button_frame, text='Recall', bg='#FBFAB8',
                               command=self.recall_pair)
        recall_button.grid(row=0, column=2, padx=60)

        reset_button = Button(button_frame, text='Reset', fg='white', bg='#AA0000',
                              command=self.reset)
        reset_button.grid(row=0, column=3, padx=20)

        quit_button = Button(button_frame, text='Quit', fg='white', bg='#AA0000',
                             command=self.quit)
        quit_button.grid(row=0, column=4, padx=20)
        button_frame.grid(row=1, columnspan=2, padx=20)
        
        root.protocol('WM_DELETE_WINDOW', self.quit)

        self.bam.print_correlation_matrix()
        
        root.mainloop()


    def quit(self):
        """
        This method will terminate the application if the user confirms
        to do so.
        """
        if messagebox.askokcancel('Quit', 'Do you want to quit?'):
            self.root.destroy()


    def memorize_pair(self):
        space_left = self.bam.remaining_associations()
        if space_left > 0:
            if messagebox.askokcancel('Memorize', 
                          'Do you want to memorize this pair?\n'
                          + f'{space_left} associations remaining'):
                A = symbol_to_list(self.A_symbol, self.Arows,self.Acolumns)
                B = symbol_to_list(self.B_symbol, self.Brows, self.Bcolumns)
                space_left = self.bam.learn_association(A, B)
                if space_left > 0:
                    messagebox.showinfo('Pair memorized', 
                                        f'Pair memorized.\n{space_left} ' 
                                      + 'associations remaining')
        else:
            messagebox.showinfo('Not memorized', 'Pair NOT memorized')
        self.bam.print_correlation_matrix()
        

    def recall_pair(self):
        A = symbol_to_list(self.A_symbol)
        B = symbol_to_list(self.B_symbol)
        A, B = self.bam.recall(A, B)
        self.A_symbol.assign(list_to_bitstring(A))
        self.B_symbol.assign(list_to_bitstring(B))


    def clear(self):
        self.A_symbol.clear()
        self.B_symbol.clear()
        

    def reset(self):
        """
        This method totally erases the BAM's memory.
        """
        if messagebox.askokcancel('Reset', 'Do you want to erase the BAM\'s memory?'):
            self.bam = BAM(self.A_symbol.rows * self.A_symbol.columns,
                           self.B_symbol.rows * self.B_symbol.columns)
            self.clear()
        
