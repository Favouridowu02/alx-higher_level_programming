#!/usr/bin/python3
from models.rectangle import Rectangle
"""
    This is the Square Class that inherits from Rectangle Class
"""


class Square(Rectangle):
    """
    Arg:
        size: The size of the square
        x: the x-axis co-ordinate
        y: the y-axis co-ordinate
        id: the id
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This is the initialization of the square class

       Arg:
            size: The size of the square
            x: the x-axis co-ordinate
            y: the y-axis co-ordinate
            id: the id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            This function returns the size of the house
        """
        return (self.width)

    @size.setter
    def size(self, size):
        """
            This is the setter functon for the size
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the Square.
            
        Args:
            *args (ints): New attribute values.
            - 1st argument represents id attribute
            - 2nd argument represents size attribute
            - 3rd argument represents x attribute
            - 4th argument represents y attribute
        
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """
            This is the string Representation of Class
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
