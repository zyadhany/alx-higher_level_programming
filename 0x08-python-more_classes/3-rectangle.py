#!/usr/bin/python3

"""class Rectangle."""


class Rectangle:
    """Rectangle."""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if not self.__width or not self.height:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        
        s = ""
        
        if not self.__width or not self.height:
            return (s)

        for i in range(self.__height):
            s += "#" * self.__width + "\n"
        return (s[:-1])

    pass
