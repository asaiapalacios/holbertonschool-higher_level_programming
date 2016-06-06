import json
from xml.dom.minidom import Document

'''Car Class specs'''

class Car():
    '''Constructor'''
    def __init__(self, *args, **kwargs):
        #Key values
        if len(args) > 0 and isinstance(args[0], dict):
            hash = args[0]
            name = hash.get('name')
            brand = hash.get('brand')
            nb_doors = hash.get('nb_doors')
        else:
            name = kwargs.get('name')
            brand = kwargs.get('brand')
            nb_doors = kwargs.get('nb_doors')

        if name == None or not isinstance(name, str):
            raise Exception("name is not a string")
        self.__name = name

        if brand == None or not isinstance(brand, str):
            raise Exception("brand is not a string")
        self.__brand = brand

        if nb_doors == isinstance(nb_doors, int) or (nb_doors <= 0):
            raise Exception("nb_doors is not > 0")
        self.__nb_doors = nb_doors

    '''Getters'''
    def get_name(self):
        return self.__name

    def get_brand(self):
        return self.__brand

    def get_nb_doors(self):
        return self.__nb_doors

    '''Setters'''
    def set_name(self, name):
        self.__name = name

    def set_brand(self, brand):
        self.__brand = brand

    def set_nb_doors(self, nb_doors):
        self.__nb_doors = nb_doors

    '''Method'''
    #Return a dictionary data structure which describes the car
    def to_hash(self):
        return {'name': self.__name,
            'brand': self.__brand,
            'nb_doors': self.__nb_doors}

    #Return a string: ":name :brand (:nb_doors)"
    def __str__(self):
        return self.__name + " " + self.__brand + " " + "(" + str(self.__nb_doors) + ")"

    #Update private attribute nb_doors to what is now being passed (number)
    def set_nb_doors(self, number):
        self.__nb_doors = number

    #Return a string in JSON format (going from data structure to string, aka dump format)
    def to_json_string(self):
        return json.dumps(self.to_hash()) 

    #Return the DOM element
    '''Required XML is:
        <car nb_doors = "5">
            <name>
                <![CDATA[Rogue]]>
            </name>
            <brand>
                Nissan
            </brand>
        </car>'''
    def to_xml_node(self, doc):
        car = doc.createElement('car')
        car.setAttribute('nb_doors', str(self.__nb_doors))
        doc.appendChild(car)
        name = doc.createElement('name')
        car.appendChild(name)
        name_cdata = doc.createCDATASection(self.__name)
        name.appendChild(name_cdata)
        brand = doc.createElement('brand')
        car.appendChild(brand)
        brand_content = doc.createTextNode(self.__brand)
        brand.appendChild(brand_content)
        return car
