'''
Script circle.py describes a Circle Class w/specific specs: private attributes, public attributes & public method
'''
import math

class Circle:
    #Constructor
    def __init__(self, radius):
        self.__radius = radius
        self.name = "circle"

    #Destructor
    def __del__(self):
        pass

    #Getter for color
    def get_color(self):
        return self.__color

    #Setter for color
    def set_color(self, color):
        self.__color = color

    #Getter for radius
    def get_radius(self):
        return self.__radius

    #Setter for radius
    def set_radius(self, radius):
        self.__radius = radius
    
    #Setter for center
    def set_center(self, center):
        self.__center = [0, 0]

    #Getter for center
    def get_center(self):
        return self.__center

    #Find and return area
    def area(self):
        return self.__radius * self.__radius * math.pi
