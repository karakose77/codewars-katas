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
6. **["mk006-sort_string.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk006-sort_string.ipynb)**: Sorts a given string. Each word in the string will contain a single number. This number is the position the word should have in the result. The words in the input String will only contain valid consecutive numbers. If the input string is empty, returns an empty string.     
   Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
7. **["mk007-shortest_word_length.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk007-shortest_word_length.ipynb)**: Given a string of words, returns the length of the shortest word(s). String will never be empty and you do not need to account for different data types.
8. **["mk008-decoder.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk008-decoder.ipynb)**: Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently, he has decided to take a couple of old songs and make dubstep remixes from them. Let's assume that a song consists of some number of words (that don't contain WUB). To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB" before the first word of the song (the number may be zero), after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words, including "WUB", in one string and plays the song at the club. For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX". Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.   
   The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters.   
   Returns the words of the initial song that Polycarpus used to make a dubsteb remix. Separates the words with a space.
9. **["mk009-at_most_n_copies.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk009-at_most_n_copies.ipynb)**: Given a list lst and a number N, create a new list that contains each number of list at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
10. **["mk010-pile_of_cubes.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk010-pile_of_cubes.ipynb)**: Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of $n^3$, the cube above will have volume of $(n-1)^3$ and so on until the top which will have a volume of $1^3$. You are given the total volume m of the building. Given m can you find the number n of cubes you will have to build? The parameter of the function will be an integer m and you have to return the integer $n$ such as $n^3 + (n-1)^3 + ... + 1^3 = m$ if such a $n$ exists or $-1$ if there is no such n.
11. **["mk011-weigth_of_numbers.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk011-weigth_of_numbers.ipynb)**: Given a string of number sort them according to their weight. For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.
    
    "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99". When two numbers have the same "weight", let us class them as if they were strings and not numbers: 100 is before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since, having the same "weight" (9) it comes before as a string. All numbers in the list are positive numbers and the list can be empty.
    
    * It may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers.
    * Don't modify the input.
12. **["mk012-number_isqual_digit_power.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk012-number_isqual_digit_power.ipynb)**: The number $89$ is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number. In effect: $89 = 8^1 + 9^2$. The next number in having this property is $135$. See this property again: $135 = 1^1 + 3^2 + 5^3$.

    We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

    `number_isequal_sum_digit_power(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]`  
    `number_isequal_sum_digit_power(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]` 

    If there are no numbers of this kind in the range [a, b] the function should output an empty list:  

    `number_isequal_sum_digit_power(90, 100) == []`