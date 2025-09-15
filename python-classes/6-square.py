#!/usr/bin/python3

"""Write an empty class Square that defines a square."""


class Square:
    """Class Square with size validation"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square with setter and getter

        Args:
            size (int, optional): size of the square. Defaults to 0.
            position (tuple, optional): position of the square.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Setter with validation."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):

        """Setter for position with validation"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        elif not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        elif not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = value

    def area(self):
        """Calculate and return the current square area

        Returns:
            int: area of the square (size * size)
        """

        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
