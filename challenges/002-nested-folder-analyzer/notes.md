# 002 - Nested Folder Analyzer

**Date:** October 27, 2026  
**Language:** Python  
**Topics:** Recursion, Dictionaries, Scope, Tuples

## What I learned

- `isinstance()` checks whether a value belongs to a particular type.
- `dict.values()` returns the values in a dictionary, while `dict.items()` returns key-value pairs.
- Each recursive call creates its own local variables. Previous calls retain their values.
- When a recursive call finishes, execution resumes in the previous call.
- Functions can return multiple values as a tuple.
- Tuple unpacking assigns returned values to separate variables.
- An empty dictionary naturally acts as a base case in this problem.

## Mistakes

- Initially tried using `len(directory)` to count files, but it only counts entries in the current dictionary.
- Called the function recursively without using its returned values.
- Confused the dictionary being passed into the function with the tuple being returned.
- Thought local variables resetting in a recursive call meant the previous call lost its values.

## Approach

Iterate through the dictionary. If a value is an integer, count it as a file and add its size. If it's another dictionary, recursively analyze it and add the returned counts and sizes to the current totals.

## Complexity

- Time: O(n)
- Space: O(d), where d is the maximum nesting depth.

## Takeaway

Each recursive call has its own local variables. Returning values allows the previous call to combine the results without losing its existing state.