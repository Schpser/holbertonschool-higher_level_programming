# 🐍 Python - Classes

## 🎯 Learning Objectives

### ✨ Why Python programming is awesome
Python's simplicity, readability, and object-oriented capabilities make it excellent for rapid development.

### 🏗️ What is OOP
Object-Oriented Programming is a programming paradigm based on the concept of **"objects"** which can contain data and code.

### 🧱 What is a class
A blueprint for creating objects, providing initial values for state (member variables) and implementations of behavior (member functions or methods).

### 🆚 What is an object and an instance
An object is an instance of a class - a concrete realization of the class blueprint.

### 🔒 What is the difference between a class and an object or instance
A class is the **definition**, while an object/instance is the **concrete realization** of that definition.

### 📋 What is an attribute
Variables that belong to an object or class, representing its state.

### 🔐 Public, protected and private attributes
- **Public**: accessible from anywhere
- **Protected**: accessible within class and subclasses (`_prefix`)
- **Private**: accessible only within class (`__prefix`)

### 🛠️ What is self
A reference to the current instance of the class, used to access variables and methods associated with the class.

### ⚡ What is a method
A function that is defined inside a class and is associated with an object.

### 🏗️ What is the special `__init__` method and how to use it
The constructor method that is automatically called when a new object is created.

### 📦 What is Data Abstraction, Data Encapsulation, and Information Hiding
Key OOP principles for managing complexity and protecting data integrity.

### 🎭 What is a property
A special kind of attribute with getter, setter, and deleter methods for controlled access.

### 🔄 What is the difference between an attribute and a property in Python
Attributes are simple variables, while properties are managed through getter/setter methods.

### 🖨️ What is the Pythonic way to write getters and setters in Python
Using the `@property` decorator for getters and `@<attribute>.setter` for setters.

### 🧠 How to dynamically create arbitrary new attributes for existing instances of a class
By simply assigning values to new attribute names on the instance.

### 🔗 How to bind attributes to object and classes
Attributes can be bound to instances (object-specific) or to classes (shared across all instances).

### 🤔 What is the `__dict__` of a class and/or instance of a class and what does it contain
A dictionary containing the class's or instance's namespace and attributes.

### 🧬 How does Python find the attributes of an object or class
Through the Method Resolution Order (MRO) which follows the inheritance hierarchy.

### 🔍 How to use the `getattr` function
A built-in function to access an object's attribute by name, with optional default value.

## 📋 Requirements

### General

| Requirement | Description |
|-------------|-------------|
| **Allowed editors** | `vi`, `vim`, `emacs` |
| **Python version** | 3.8.5 (Ubuntu 20.04 LTS) |
| **File format** | All files end with new line, first line `#!/usr/bin/python3` |
| **Style guide** | `pycodestyle` (version 2.7.*) |
| **Executable** | All files must be executable |
| **README** | Mandatory `README.md` at project root |
| **Length check** | Files tested using `wc` |
| **Test files** | All modules should have test files |
| **Documentation** | Modules and functions must be documented |

## 🚀 Tasks

| # | Task Name | Description | File Name |
|---|-----------|-------------|-----------|
| **0** | My first square | Write an empty class `Square` that defines a square | `0-square.py` |
| **1** | Square with size | Write a class `Square` with private instance attribute `size` | `1-square.py` |
| **2** | Size validation | Add size validation to `Square` class | `2-square.py` |
| **3** | Area of a square | Add `area` method to `Square` class | `3-square.py` |
| **4** | Access and update private attribute | Add getter and setter for `size` attribute | `4-square.py` |
| **5** | Printing a square | Add method to print square with `#` character | `5-square.py` |
| **6** | Coordinates of a square | Add `position` attribute and update printing method | `6-square.py` |

## 🚀 Usage

To run any task, make the file executable and execute it:

```bash
chmod +x <task>-main.py
./<task>-main.py
```

### Example for task 0:

```bash
chmod +x 0-main.py
./0-main.py
```

---

> *"Python is the second best language for everything."* - Unknown 🐍✨

This project explores the fundamentals of **Object-Oriented Programming** in Python, focusing on:
- Class creation
- Attributes
- Methods  
- Properties
- Encapsulation principles

Each task builds upon the previous one to create a fully-featured `Square` class with validation, properties, and visualization capabilities.