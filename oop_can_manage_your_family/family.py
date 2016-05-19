'''
family.py script describes a Person Class with required specs
'''

class Person:

    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]
    
    #Init method used to initialize an instance
    def __init_(self, id, first_name, date_of_birth, genre, eyes_color):
        
        #Getter of id, eyes_color, genre, date_of_birth, first_name
        def get_id(self):
            return self.__id
                        
        def get_eyes_color(self):
            return self.__eyes_color

        def get_genre(self):
            return self.__genre

        def get_date_of_birth(self):
            return self.__date_of_birth

        def get_first_name(self):
            return self.__first_name

        #Exceptions
        if type(id) < 0 or type(id) is not int:
            raise Exception("id is not an integer")
        self.__id = id

        if type(first_name) is "" or type(first_name) is not str:
            raise Exception("string is not a string")
        self.__first_name = first_name

        if type(date_of_birth) not in list[int]:
            raise Exception("date_of_birth is not a valid date")
        self.__date_of_birth = date_of_birth

        if type(genre) is not str and type(genre) not in Person.GENRES:
            raise Exception("genre is not valid")
        self.__genre = genre

        if type(eyes_color) is not str and type(eyes_color) not in Person.EYES_COLORS:
            raise Exception("eyes_color is not valid")
        self.__eyes_color = eyes_color

        #Public attribute
        self.last_name = "to be determined"
