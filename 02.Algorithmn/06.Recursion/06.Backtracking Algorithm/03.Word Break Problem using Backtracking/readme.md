**WORD BREAK PROBLEM USING BACKTRACKING**
Given a non-empty sequence s and a dictionary dict[] containing a list of non-empty words, the task is to return all possible ways to break the sentence in individual dictionary words.
Note: The same word in the dictionary may be reused multiple times while breaking.

**INPUT**
Input: s = “catsanddog” , dict = [“cat”, “cats”, “and”, “sand”, “dog”]
**OUTPUT**
Output: 
“cats and dog” 
“cat sand dog”
Explanation: The string is split into above 2 ways, in each way all are valid dictionary words.

**INPUT**
Input: s = “pineapplepenapple” , dict = [“apple”, “pen”, “applepen”, “pine”, “pineapple”]
**OUTPUT**
Output: 
“pine apple pen apple” 
“pineapple pen apple” 
“pine applepen apple” 
Explanation: The string is split into above 3 ways, in each way all are valid dictionary words.

**STEPS TO IMPLEMENT**

1.Convert the dictionary into a hash set for quick search.
2.If the start index reaches the length of the string (s), it signifies a valid sentence has been constructed. Add the current sentence (curr) to the result.
3.Loop through every substring starting at start and ending at all possible positions (end).
4.For each substring, check if it exists in the dictionary (dictSet).
5.If valid:
Append the word to the current sentence (curr).
Recursively call the function for the remaining part of the string (from end onwards).
6.After the recursive call returns, restore the state of curr to ensure the next branch of exploration starts with the correct sentence.



