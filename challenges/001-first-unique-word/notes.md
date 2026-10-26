# First Unique Word

October 26, 2026

Find the first word in a sentence that appears exactly once.

## What I learned

- `split()` separates a string into a list of words.
- `replace()` can remove punctuation by replacing it with an empty string.
- `Counter("hello")` counts characters, not words.
- `Counter(["hello", "world"])` counts words.
- Lists preserve order.
- Functions implicitly return `None` if no return is reached.

## Mistakes

Initially passed the sentence directly to `Counter`, which counted characters instead of words.

Also tried calling `replace()` after `split()`. That doesn't work because `split()` returns a list, and `replace()` is a string method.

## Solution

Count word frequencies first, then iterate through the original list until a word with a count of 1 is found.

Time: O(n)  
Space: O(n)