#!/usr/bin/env python3
from 1-task_01_duck_typing import Circle, Rectangle, shape_info

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

print("Circle info:")
shape_info(circle)

print("\nRectangle info:")
shape_info(rectangle)
