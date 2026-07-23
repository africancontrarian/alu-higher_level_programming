#!/usr/bin/python3
"""Defines a Node class and a SinglyLinkedList class."""


class Node:
    """Represent a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data to store in this node.
            next_node (Node): The next node in the list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data stored in this node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data stored in this node.

        Args:
            value (int): The new data for this node.

        Raises:
            TypeError: If value is not an integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node linked to this one."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node linked to this one.

        Args:
            value (Node): The next node in the list, or None.

        Raises:
            TypeError: If value is neither None nor a Node instance.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list that stays sorted in increasing order."""

    def __init__(self):
        """Initialize a new, empty SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node with value into its sorted position.

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while (current.next_node is not None and
                current.next_node.data < value):
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return the list's data, one value per line."""
        lines = []
        current = self.__head
        while current is not None:
            lines.append(str(current.data))
            current = current.next_node
        return "\n".join(lines)
