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
5. **["mk005-complementary_dna.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk005-complementary_dna.ipynb)**: Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms. In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". DNA strand is never empty or there is no DNA at all. Given one side of the DNA as a string; returns the other complementary side. 
6. **["mk006-order.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk006-order.ipynb)**: Sorts a given string. Each word in the string will contain a single number. This number is the position the word should have in the result. The words in the input String will only contain valid consecutive numbers. If the input string is empty, returns an empty string.  
    
   Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
7. **["mk007-shortest_word_length.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk007-shortest_word_length.ipynb)**: Given a string of words, returns the length of the shortest word(s). String will never be empty and you do not need to account for different data types.