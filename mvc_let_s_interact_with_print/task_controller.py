'''
Python Controller Script: Describes a Class that Controls Model and View Instances
'''

import Tkinter as tk
from task_model import TaskModel
from task_view import TaskView

class TaskController():

    '''Constructor'''
    def __init__(self, master, model):
        if master.__class__.__name__ != tk.Tk():
            Exception("master is not a tk.Tk()")

        if isinstance(model, TaskModel) == False:
            Exception("model is not a TaskModel")
        
        # Private attribute
        self.__model = model
        self.__view = TaskView(master) # Creates the View

        '''Link all callbacks from model to update view'''

        '''Link the button of view to update model'''
