#!/usr/bin/python3

"""Write an empty class Square that defines a square."""


class Square:
    """Class Square with size validation"""

    def __init__(self, size=0):
        """Initialize Square with setter and getter

        Args:
            size (int, optional): size of the square. Defaults to 0.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size

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

    def area(self):
        """Calculate and return the current square area

        Returns:
            int: area of the square (size * size)
        """

        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
