<p align="center">
  <img src="https://1.bp.blogspot.com/-tRUfbhCbapU/Xo_xGuV6CJI/AAAAAAAAbzU/8QhYnL0p06ceYd43zO-mubZ-DFIev0n0wCLcBGAsYHQ/w1200-h630-p-k-no-nu/How-to-Learn-Python.jpg" alt=" python banner image."><br>

<h1 align="center">  Basics of Python programming  </h1>
<h3 align="center">🎓 Course | 📝 Notes | 🔰 Beginner</h3>

<br>
<br>

## What is python programming ?

Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.

Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.

<br>


## How to create a Python file ?

All the files related to Python ends with .py ( .py is the extension to specify that it's a Python program ).

eg :- `main.py`, `basics.py`

<br>


## what is a module?

A Python module is a file containing Python definitions and statements. A module can define functions, classes, and variables.

A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use. It also makes the code logically organized.

😵‍💫😵‍💫😵‍💫 ❓❓

<br>

### In simple language ,

modules is a collection of predefined functions, Classes.

( predefined functions are those functions that are already defined and available to use in the program )

😮😮😮

in different languages its know by different name like library, header file, etc. (so don't be confused)

examples :-

`math`, `string`, `random`

<br>

> We include the modules by using _`import`_

```python
syntex :-
    import <module>
```

```python
example:-
    import numpy
```

You can choose to import only parts from a module, by using the _`from`_ keyword.

```py
syntex:-
    from <module> import <function>

example:-
    from math import sqrt
```

<br>

## 🤖 what are datatype?

In computer science and computer programming,
a data type or simply type is an attribute of data which tells the compiler or interpreter how the programmer intends to use the data.

**Note** :- Most programming languages support basic data types of integer numbers (of varying sizes),
floating-point numbers (which approximate real numbers), characters and Booleans.

A data type constrains the values that an expression, such as a variable or a function, might take.

This data type defines the operations that can be done on the data, the meaning of the data, and the way values of that type can be stored.

A data type provides a set of values from which an expression (i.e. variable, function, etc.) may take its values.

<br>

> **TRANSLATION:-**

Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data. Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.

> in singleLine explanation "datatype are the classification of data in to different types"

😮😮😮

we have a wide range of datatype

like:-

-   int
-   float
-   boolean
-   char

<br>

---

## 📦 what are variables ?

> click [here](../week-0-basics/variables.py) or open the variables.c file from week-0-Basics to see the reference code

Python is not “statically typed”. We do not need to declare variables before using them or declare their type. A variable is created the moment we first assign a value to it. A variable is a name given to a memory location. It is the basic unit of storage in a program.

-   The value stored in a variable can be changed during program execution.

-   A variable is only a name given to a memory location, all the operations done on the variable effects that memory location.

> variables are containers thats stores a value.

assigning value AKA giving Value to a variable, its just like saying `x = 1` in Maths

so, `x = 1` means what, It means that there is a variable named x and it stores a value of 1 ( its Value is 1 ).

```python
    y = 2	# variable declaration and assigning value in a single line
```

> Rules for creating variables in Python:

-   A variable name must start with a letter or the underscore character.
-   A variable name cannot start with a number.
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ ).
-   Variable names are case-sensitive (name, Name and NAME are three different variables).
-   The reserved words(keywords) cannot be used naming the variable.
