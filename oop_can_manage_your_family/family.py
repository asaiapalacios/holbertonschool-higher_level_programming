'''
family.py script describes a Person Class with required specs
'''
import json

class Person():

    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    #Init method used to initialize an instance
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):

        #Initializing and exceptions
        if type(id) < 0 or type(id) is not int:
            raise Exception("id is not an integer")
        self.__id = id

        if type(first_name) is "" or type(first_name) is not str:
            raise Exception("string is not a string")
        self.__first_name = first_name

        if(len(date_of_birth) is not 3 and all(isinstance(item, int) for item in date_of_birth)):
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
        self.is_married_to = 0

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

    #Return a string with first_name & last_name attached by a space
    def __str__(self):
        return "%s %s" % (self.__first_name, self.last_name)

    #Check if Person is male
    def is_male(self):
        if self.__genre == "Male":
            return True

    #Return the current age in year based on DOB and the date
    def age(self):
        today = [5, 20, 2016]
        return today[2] - self.__date_of_birth[2] - ((today[0], today[1]) < (self.__date_of_birth[1], self.__date_of_birth[0]))

    #Overloading methods which support comparison operators
    def __gt__(self, other):
        return self.age() > other.age()
    def __ge__(self, other):
        return self.age() >= other.age()
    def __lt__(self, other):
        return self.age() < other.age()
    def __le__(self, other):
        return self.age() <= other.age()
    def __eq__(self, other):
        return self.age() == other.age()
    def __ne__(self, other):
        return self.age() != other.age()
'''
TASK 3
#Return a hash describing the person by keys
    def json(self): 
        return { 'id': self.__id, 'eyes_color': self.__eyes_color, 'genre': self.__genre, 'date_of_birth': self.__date_of_birth, 'first_name': self.__first_name, 'last_name': self.last_name, 'is_married_to': self.is_married_to }

#Set all Person attributes by value from the Hash
    def load_from_json(self, json): 
        self.__id = json['id'] 
        self.__eyes_color = json['eyes_color'] 
        self.__genre = json['genre'] 
        self.__date_of_birth = json['date_of_birth'] 
        self.__first_name = json['first_name'] 
        self.last_name = json['last_name']
        self.is_married_to = json ['is_married_to']

#Implement 2 new functions (not part of any Class)
def save_to_file(list, filename)

def load_from_file(filename)
'''
#Child classes of Person
class Baby(Person):
    def can_run(self):
        return False
    def need_help(self):
        return True
    def is_young(self):
        return True
    def can_vote(self):
        return False
    def can_be_married(self):
        return False
    def is_married(self):
        if self.is_married_to != 0:
            return True
        else:
            return False 
    def divorce(self, p):
        return False
    def just_married_with(self, p):
        return False

class Teenager(Person):
    def can_run(self):
        return True
    def need_help(self):
        return False
    def is_young(self):
        return True
    def can_vote(self):
        return False
    def can_be_married(self):
        return False 
    def is_married(self):
        if self.is_married_to != 0:
            return True
        else:
            return False
    def divorce(self, p):
        return False
    def just_married_with(self, p):
        return False

class Adult(Person):
    def can_run(self):
        return True
    def need_help(self):
        return False
    def is_young(self):
        return False
    def can_vote(self):
        return True
    def can_be_married(self):
        return True
    def is_married(self):
        if self.is_married_to != 0:
            return True
        else:
            return False
    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0
    #def just_married_with(self, p):
        

class Senior(Person):
    def can_run(self):
        return False
    def need_help(self):
        return True
    def is_young(self):
        return False
    def can_vote(self):
        return True
    def can_be_married(self):
        True
    def is_married(self):
        if self.is_married_to != 0:
            return True
        else:
            return False
    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0
    #def just_married_with(self, p):
