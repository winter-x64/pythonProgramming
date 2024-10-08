# Arrays in Python

In Python, an array is a collection of items stored at contiguous memory locations. They can hold items of the same type and are useful for performing numerical computations. However, Python does not have a built-in array data type like some other languages. Instead, it provides a few options for working with arrays:

1. **Lists**: The most common way to create a dynamic array. Lists can hold items of different types, and their size can change dynamically.

   ```python
   my_list = [1, 2, 3, 4, 5]
   ```

2. **The `array` module**: This module provides a way to create arrays that are more efficient than lists for certain types of numeric data. Arrays created using this module can only hold items of the same type.

   ```python
   import array
   my_array = array.array('i', [1, 2, 3, 4, 5])  # 'i' indicates integer type
   ```

> In simple terms, Array is a collection of data (int, float, etc), which is stored in a single variable

## Key Differences

- **Type Flexibility**: Lists can hold mixed types, while arrays (from the `array` module and NumPy) require all elements to be of the same type.

## When to Use Which

- Use **lists** for general-purpose collections when you need flexibility in types.
- Use the **array module** for performance-critical applications that require basic numerical data handling with uniform types.
