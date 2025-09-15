🐍 Python - More Classes and Objects
🎯 Learning Objectives
✨ Object-Oriented Programming in Python:

Deepen understanding of classes and objects

Master advanced class features and special methods

🔐 Private Attributes:

Implement data encapsulation with private instance attributes

Use property decorators for getters and setters

🎭 Special Methods:

__str__() for human-readable string representation

__repr__() for official string representation

__del__() for cleanup operations

📊 Class Attributes:

Shared data across all instances

Track instance count and shared configuration

⚡ Advanced Methods:

Static methods for utility functions

Class methods for alternative constructors

🧮 Geometry Operations:

Calculate area and perimeter of rectangles

Compare rectangles based on area

📋 Requirements
General
Requirement	Description
Allowed editors	vi, vim, emacs
Python version	3.8.5 (Ubuntu 20.04 LTS)
File format	All files end with new line, first line #!/usr/bin/python3
Style guide	pycodestyle (version 2.7.*)
Executable	All files must be executable
README	Mandatory README.md at project root
No imports	Not allowed to import any module
🚀 Tasks
#	Task Name	Description	File Name	Points
0	Simple rectangle	Empty class that defines a rectangle	0-rectangle.py	0/6
1	Real definition of a rectangle	Class with width and height properties	1-rectangle.py	0/16
2	Area and Perimeter	Add area and perimeter methods	2-rectangle.py	0/10
3	String representation	Implement __str__ method	3-rectangle.py	0/11
4	Eval is magic	Implement __repr__ method	4-rectangle.py	0/10
5	Detect instance deletion	Implement __del__ method	5-rectangle.py	0/8
6	How many instances	Track instances with class attribute	6-rectangle.py	0/12
7	Change representation	Customizable print symbol	7-rectangle.py	0/13
8	Compare rectangles	Static method to compare areas	8-rectangle.py	0/11
9	A square is a rectangle	Class method to create squares	9-rectangle.py	0/13
📖 Detailed Task Descriptions
0. Simple rectangle
Create an empty class Rectangle that defines a rectangle.

Example:

python
my_rectangle = Rectangle()
print(type(my_rectangle))  # <class '0-rectangle.Rectangle'>
print(my_rectangle.__dict__)  # {}
1. Real definition of a rectangle
Enhance the Rectangle class with:

Private attributes width and height with getters/setters

Type and value validation

Optional initialization

2. Area and Perimeter
Add methods to calculate:

area(): returns width × height

perimeter(): returns 2×(width+height) (0 if either dimension is 0)

3. String representation
Implement __str__() method to print rectangle using # characters.

4. Eval is magic
Implement __repr__() method to return string that can recreate object with eval().

5. Detect instance deletion
Implement __del__() method to print farewell message when instance is deleted.

6. How many instances
Add class attribute number_of_instances to track active Rectangle instances.

7. Change representation
Add class attribute print_symbol to customize string representation symbol.

8. Compare rectangles
Add static method bigger_or_equal() to compare rectangles based on area.

9. A square is a rectangle
Add class method square() to create Rectangle instances with equal width and height.

🚀 Usage
To run any task, make the file executable and execute it:

bash
chmod +x <task>-main.py
./<task>-main.py
Example for task 0:

bash
chmod +x 0-main.py
./0-main.py
"Python classes are like blueprints for objects - they define what an object can do and what data it contains." 🐍✨

