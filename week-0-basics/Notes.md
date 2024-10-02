<p align="center">
  <img src="https://www.digitalscholarshipleiden.nl/images/uploads/_articleHeader/Python_image.jpg" alt=" python banner image."><br>

<h1 align="center">  Notes of week 0 </h1>
<br>
<br>
# Lets do some practical stuff

## How to print a output to the user

> click [here](../week-0-basics/helloWorld.py) or open the helloWorld.py file from week-0 to see the reference code :-

`print()` is a function the prints stuff on the screen

like in the [helloWorld](../week-0-basics/helloWorld.py) program, we printed hello world on the terminal

```python
syntex:-
    print("your_message")

example:-
    print("Hello world")

    # here we printed text inside double quotes
    # which is "Hello world"
```

## How to Get user Input

> click [here](../week-0-basics/inputProgram.py) or open the inputProgram.py file from week-0 to see the reference code :-

'input()' is used to get the user input and stores it in a variable

```python
syntex:-
    variable_name = input("your_message")

example:-
    name = input("Enter your name => ")
```

So, If you're running this code and check the datatype of the variable

```python
number = input("Enter a number => ")
print(type(name))
```

you will get a `<class 'str'>` as the output that means it's a string not an Integer, you can't do any math stuff to it like add, sub

So how will you do it?, You have to convert the str to int by using `int()` function

```python
number = int(input("Enter a number => "))
print(type(name))
```

Now you will get the output as `<class 'int'>`
So here is an example for Arithmetic operations, [click here](/week-0-basics/MathOperations.py)
