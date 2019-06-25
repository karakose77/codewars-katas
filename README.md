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
13. **["mk013-human_readible_time.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk013-human_readible_time.ipynb)**: Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    * HH = hours, padded to 2 digits, range: 00 - 99  
    * MM = minutes, padded to 2 digits, range: 00 - 59 
    * SS = seconds, padded to 2 digits, range: 00 - 59
    * The maximum time never exceeds 359999 (99:59:59)
14. **["mk014-first_non_repeating_letter.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk014-first_non_repeating_letter.ipynb)**: Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string. For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

    As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
    
    If a string contains all repeating characters, it should return an empty string ("") or None.

15. **["mk015-is_perfect_power.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk015-is_perfect_power.ipynb)**: A perfect power is a classification of positive integers:

    In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive integer. More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that mk = n.
    
    Your task is to check whether a given integer is a perfect power. If it is a perfect power, return a pair m and k with mk = n as a proof. Otherwise return Nothing, Nil, null, NULL, None or your language's equivalent.
    
    Note: For a perfect power, there might be several pairs. For example 81 = 3^4 = 9^2, so (3,4) and (9,2) are valid solutions. However, the tests take care of this, so if a number is a perfect power, return any pair that proves it.
    
16. **["mk016-tic_tac_toe_solved.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk016-tic_tac_toe_solved.ipynb)**: If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

    Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:
    ```
    [[0, 0, 1],
     [0, 1, 2],
     [2, 1, 0]]
    ```
    We want our function to return:
    ```
    -1 if the board is not yet finished (there are empty spots),
    1 if "X" won,
    2 if "O" won,
    0 if it's a cat's game (i.e. a draw).
    ```
     You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

17. **["mk017-letter_sort.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk017-letter_sort.ipynb)**: Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.
    ```
    s1 = "A aaaa bb c"
    s2 = "& aaa bbb c d"
    s1 has 4 'a', 2 'b', 1 'c'
    s2 has 3 'a', 3 'b', 1 'c', 1 'd'
    ```
    So the maximum for `'a'` in `s1` and `s2` is `4` from `s1`; the maximum for `'b'` is `3` from `s2`. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.
    
    We can resume the differences between `s1` and `s2` in the following string: `"1:aaaa/2:bbb"` where `1` in `1:aaaa` stands for string `s1` and `aaaa` because the maximum for `a` is `4`. In the same manner `2:bbb` stands for string `s2` and `bbb` because the maximum for `b` is `3`.
    
    The task is to produce a string in which each lowercase letters of `s1` or `s2` appears as many times as its maximum if this maximum is strictly greater than `1`; these letters will be prefixed by the number of the string where they appear with their maximum value and `:`. If the maximum is in `s1` as well as in `s2` the prefix is `=:`.
    
    In the result, substrings (a substring is for example `2:nnnnn` or `1:hhh`; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by `'/'`.
    
    Hopefully other examples can make this clearer.
    ```
    s1 = "my&friend&Paul has heavy hats! &"
    s2 = "my friend John has many many friends &"
    mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
    
    s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
    s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
    mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
    
    s1="Are the kids at home? aaaaa fffff"
    s2="Yes they are here! aaaaa fffff"
    mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
    ```
18. **["mk018-sum_of_intervals.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk018-sum_of_intervals.ipynb)**: Write a function called `sum_of_intervals` that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

    Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: `[1, 5]` is an interval from 1 to 5. The length of this interval is 4.
    
    List containing overlapping intervals:
    
    `[[1,4], [7, 10], [3, 5]]`
    
    The sum of the lengths of these intervals is 7. Since `[1, 4]` and `[3, 5]` overlap, we can treat the interval as `[1, 5]`, which has a length of 4.
    
    Examples:
    
    `sum_of_intervals([[1,2], [6, 10], [11, 15]]) => 9`  
    `sum_of_intervals([[1,4], [7, 10], [3, 5]]) => 7`  
    `sum_of_intervals([[1,5], [10, 20], [1, 6], [16, 19], [5, 11]]) => 19`  
19. **["mk019-smallest_possible_sum.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk019-smallest_possible_sum.ipynb)**: Given an array X of positive integers, its elements are to be transformed by running the following operation on them as many times as required:

    `if X[i] > X[j] then X[i] = X[i] - X[j]`
    
    When no more transformations are possible, return its sum ("smallest possible sum"). For instance, the successive transformation of the elements of input `X = [6, 9, 21]` is detailed below:
    
    `X_1 = [6, 9, 12] : X_1[2] = X[2] - X[1] = 21 - 9 = 12`  
    `X_2 = [6, 9, 6]   : X_2[2] = X_1[2] - X_1[0] = 12 - 6 = 6`  
    `X_3 = [6, 3, 6]  : X_3[1] = X_2[1] - X_2[0] = 9 - 6 = 3`  
    `X_4 = [6, 3, 3]  : X_4[2] = X_3[2] - X_3[1] = 6 - 3 = 3`  
    `X_5 = [3, 3, 3]  : X_5[1] = X_4[0] - X_4[1] = 6 - 3 = 3`  
    
    The returning output is the sum of the final transformation (here 9).
20. **["mk020-the-millionth_fibonacci.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk020-the-millionth_fibonacci.ipynb)**: In this kata you will have to calculate fib(n) where:

    `fib(0) := 0`   
    `fib(1) := 1`  
    `fin(n + 2) := fib(n + 1) + fib(n)`  
    
    Write an algorithm that can handle n up to 2000000. Your algorithm must output the exact integer answer, to full precision. Also, it must correctly handle negative numbers as input.
    
    HINT: Can you rearrange the equation `fib(n + 2) = fib(n + 1) + fib(n)` to find `fib(n)` if you already know `fib(n + 1)` and `fib(n + 2)`? Use this to reason what value fib has to have for negative values.
 21. **["mk021-squirrel_and_tree.ipynb"](https://github.com/karakose77/codewars-katas/blob/master/mk021-squirrel_and_tree.ipynb)**: Since the weather was good, some 
 students decided to go for a walk in the park after the first 
 lectures of the new academic year. There they saw a squirrel, 
 which climbed a tree in a spiral at a constant angle to the 
 ground. They calculated that in one loop the squirrel climbes 
 `h` meters (vertical height), the height of the tree is equal 
 to `H`, and the length of its circumference equals `S`. 
 
      These calculations were exhausting, so now the students
      need your help to figure out how many meters the path 
      length of squirrel climbed when it reached the tree top. 
      The result should be rounded to 4 decimal places. Code 
      should be less than 52 characters.
      
      Example 
      
      For h = 4, H = 16, S = 3, the output should be 20. 
      
      For h = 8, H = 9, S = 37, the output should be 42.5869.
