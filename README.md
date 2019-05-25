# codewars-katas

Includes my katas(exercises) from **["CodeWars"](https://www.codewars.com/)**. The files are in jupyter notebook format and "~/.ipython/profile_default/ipython_kernel_config.py" file should have the following lines:

`c.IPKernelApp.matplotlib = 'inline'`  
`c.InlineBackend.figure_format = 'retina'`

---

## Table of Contents

1. **["mk001-anagram.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk001-anagram.ipynb)**: Returns all anagrams of a word from a list of words. Two words are anagrams of each other if they both contain the same letters.
2. **["mk002-is_triangle.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk002-is_triangle.ipynb)**: Returns true if a triangle can be built with the sides of given length and false in any other case.
3. **["mk003-duplicate_encoder.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk003-duplicate_encoder.ipynb)** : The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Capitalization is ignored.
4. **["mk004-highest_and_lowest.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk004-highest_and_lowest.ipynb)**: Given a string of space separated numbers, returns the highest and lowest number. All numbers are valid Int32, no need to validate them. There will always be at least one number in the input string. Output string must be two numbers separated by a single space, and highest number is first.