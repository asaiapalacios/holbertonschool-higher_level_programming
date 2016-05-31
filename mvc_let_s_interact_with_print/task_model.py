'''
Script that describes a TaskModel Class
'''

'''Class'''
class TaskModel():
    '''Constructor'''
    def __init__(self, title):
        if type(title) is not str or type(title) == "":
            raise Exception("title is not a string")
        #private attributes
        self.__title = title 
        self.__callback_title = None 

    '''Getter of title'''
    def get_title(self):
        return self.__title

    '''Setter of callback_title'''
    def set_callback_title(self, callback_title):
        self.__callback_title = callback_title

    '''Reverse a string'''
    def toggle(self):
        self.__title = self.__title[::-1] # "slices" your string, going through all of it by steps of -1; reverses string value
        if self.__callback_title != None:
            self.__callback_title(self.__title) # Calls back title already in reverse value

    '''Return value for title attribute'''
    def __str__(self):
        return self.__title
