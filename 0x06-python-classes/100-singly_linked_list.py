#!/usr/bin/python3

"""class lnked list."""


class Node:
    """node."""

    def __init__(self, data, next_node=None):
        """ new node """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get value"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """ setvalue """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """get value"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ setvalue """
        if not isinstance(value, Node) and value:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """sigle linked list"""

    def __init__(self):
        """ new list """
        self.__head = None

    def sorted_insert(self, value):
        """insert new node"""
        node = Node(value)
        tmp = self.__head

        if not self.__head:
            self.__head = node
            return
        elif self.__head.data >= value:
            node.next_node = self.__head
            self.__head = node
            return

        while tmp:
            if not tmp.next_node:
                tmp.next_node = node
                return
            if tmp.next_node.data >= node.data:
                node.next_node = tmp.next_node
                tmp.next_node = node
                return
            tmp = tmp.next_node

    def __str__(self):
        """print all list"""
        s = ""
        tmp = self.__head
        while tmp:
            s += str(tmp.data)
            if tmp.next_node:
                s += "\n"
            tmp = tmp.next_node
        return (s)
