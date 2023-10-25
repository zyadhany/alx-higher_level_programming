#!/usr/bin/python3

"""class square."""


class Square:
    """square."""

    def __init__(self, size=0):
        """ new square """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    @property
    def size(self):
        """get value"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ setvalue """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ square area """
        return (self.__size ** 2)

    def my_print(self):
        """print square"""
        for i in range(self.size):
            print("#" * self.size)
