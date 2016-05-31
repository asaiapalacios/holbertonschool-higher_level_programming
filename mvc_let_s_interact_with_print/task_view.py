'''
Python View Script Using Tkinter Library: Tkinter Turns Python Code into Tcl Code with Tcl's TK Widgets to Build GUI Applications in Python
'''

import Tkinter as tk

'''Class is a subclass of the Tkinter Toplevel'''
class TaskView(tk.Toplevel):

    '''Constructor'''
    def __init__(self, master):
        tk.Toplevel.__init__(self, master) # Inherit base class attributes
        
        '''Policy for when window is closed'''
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        
        if self.master != tk.Tk():
            Exception("master is not a tk.Tk()")
        
        # Public attribute
        self.master = master
        
        # Private attributes
        self.__title_var = tk.StringVar() # StringVar - a variable that holds onto a str
        self.__title_label = tk.Label(self, textvariable=self.__title_var) # Paramater passes instance and 2nd argument given for Label widget
        
        '''Pack lets Tkinter figure out where objects should go; it's a method to insert a widget in the available space'''
        self.__title_label.pack(side='right') # Aligns to right

        self.toggle_button = tk.Button(self, text="Reverse")
        self.toggle_button.pack(side='left') # Aligns to left

    '''Method'''
    def update_title(self, title):
        if type(title) is not str or not title:
            Exception("title is not a string")
        else:
            self.__title_var.set(title)
