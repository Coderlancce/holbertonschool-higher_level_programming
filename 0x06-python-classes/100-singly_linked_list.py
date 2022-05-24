#!/usr/bin/python3
"""Write a class Node"""


class Node:
    """ defines a node of a singly linked list """

    def __init__(self, data, next_node=None):
        """ inizialise Node object """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ retrieve the data of Node obj """
        return self._Node__data

    @data.setter
    def data(self, value):
        """ set the data of Node obj """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self._Node__data = value

    @property
    def next_node(self):
        """ retrieve the next_node of Node obj """
        return self._Node__next_node

    @next_node.setter
    def next_node(self, value):
        """ set the next_node of Node obj """
        if type(value) != Node and value:
            raise TypeError("next_node must be a Node object")
        self._Node__next_node = value


class SinglyLinkedList:
    """ defines a singly linked list """

    def __init__(self):
        """ inizialise Node object """
        self.head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position
        in the list (increasing order)"""
        if self.head is None:
            self.head = Node(value)
            return

        new = Node(value, self.head)
        current = new
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new.next_node = current.next_node
        if current != new:
            current.next_node = new
        else:
            self.head = new

    def __str__(self):
        """ format to print all node data's """
        current = self.head
        buff = []
        while current:
            buff.append(current.data)
            current = current.next_node
        return "\n".join([str(x) for x in buff])
