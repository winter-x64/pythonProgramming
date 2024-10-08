# Indexing in Python

1. **Zero-Based Indexing**:
   - Python uses zero-based indexing, meaning the first element is at index `0`, the second at index `1`, and so on.
   - For example, in the list `my_list = [10, 20, 30, 40]`:
     - `my_list[0]` refers to `10`
     - `my_list[1]` refers to `20`
     - `my_list[2]` refers to `30`
     - `my_list[3]` refers to `40`

2. **Negative Indexing**:
   - You can also use negative indices to access elements from the end of the list.
   - For example:
     - `my_list[-1]` refers to the last element (`40`)
     - `my_list[-2]` refers to the second-to-last element (`30`)

3. **Slicing**:
   - You can get a portion (slice) of the array using a range of indices.
   - Syntax: `my_list[start:end]` (includes `start`, excludes `end`).
   - For example:

    ```python
     my_list = [10, 20, 30, 40, 50]
    sub_list = my_list[1:4]  # This will give [20, 30, 40]
     ```

> Here is an example for Array, [Click here](/week-1-arrays-string/code/arrayindexing.py)

## Summary

- **Indexing** allows you to access individual elements using their position.
- **Negative indexing** lets you count backwards from the end.
- **Slicing** lets you grab a part of the array.

This makes working with arrays and lists very flexible and powerful