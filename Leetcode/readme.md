**LeetCode Solutions \- Time & Space Complexity Analysis**

**Repository: yash-goyal-0910/DSA\_Practice**  
**Folder: Leetcode**

**Overview**  
**This document provides a comprehensive analysis of all LeetCode solutions in the repository, including detailed time and space complexity breakdowns for each problem.**

**\===============================================================================**

**Q14: Longest Common Prefix**  
**Topic: String**  
**Link: https://leetcode.com/problems/longest-common-prefix/**

**Approach:**  
**The solution iterates through each string and compares characters at each position with the longest string found so far. It maintains a running \`longest\` variable that gets trimmed whenever characters don't match.**

**Time Complexity: O(S) where S is the sum of all characters in all strings. In the worst case, we compare every character of every string.**

**Space Complexity: O(1) \- Only using a constant amount of extra space for the longest variable (excluding output).**

**\===============================================================================**

**Q28: Implement strStr()**  
**Topic: String**  
**Link: https://leetcode.com/problems/implement-strstr/**

**Approach:**  
**Uses Python's built-in string.find() method which internally uses an optimized string matching algorithm (likely Boyer-Moore or similar).**

**Time Complexity: O(n\*m) in worst case where n is length of haystack and m is length of needle. Built-in Python implementation is highly optimized.**

**Space Complexity: O(1) \- No extra space used.**

**\===============================================================================**

**Q38: Count and Say**  
**Topic: String**  
**Link: https://leetcode.com/problems/count-and-say/**

**Approach:**  
**Recursive solution that builds the sequence. For each number n, it calls count\_say(n-1) and then applies the "count and say" logic by iterating through the result, counting consecutive identical characters.**

**Time Complexity: O(2^n) \- The sequence grows exponentially. Each sequence can be roughly twice as long as the previous one in the worst case.**

**Space Complexity: O(2^n) \- The recursion depth is n, and each level stores the string result which grows exponentially.**

**\===============================================================================**

**Q165: Compare Version Numbers**  
**Topic: String**  
**Link: https://leetcode.com/problems/compare-version-numbers/description/**

**Approach:**  
**Splits both version strings by '.', converts to integers, pads with zeros to make them equal length, then compares element by element.**

**Time Complexity: O(max(n, m)) where n is the number of version parts in version1 and m is the number of parts in version2. We iterate through each part once.**

**Space Complexity: O(n \+ m) \- Space needed for the split lists and potentially padding with zeros.**

**\===============================================================================**

**Q242: Valid Anagram**  
**Topic: String**  
**Link: https://leetcode.com/problems/valid-anagram/description/**

**Approach:**  
**Uses a fixed-size array (26 for lowercase letters) to count character frequencies. Increments for string s, decrements for string t. If all counts are zero at the end, strings are anagrams.**

**Time Complexity: O(n \+ m) where n is length of s and m is length of t. We iterate through each string once.**

**Space Complexity: O(1) \- Uses a fixed-size array of 26 elements for lowercase English letters, which is constant space.**

**\===============================================================================**

**Q686 (Solution 1): Repeated String Match**  
**Topic: String**  
**Link: https://leetcode.com/problems/repeated-string-match**

**Approach:**  
**Complex logic checking if string b can be formed by repeating string a. Validates alignment, checks character sequences, and handles edge cases.**

**Time Complexity: O(n\*m) where n is length of a and m is length of b. Multiple string find() operations and character-by-character comparisons.**

**Space Complexity: O(1) \- Only using variables for indices and counts, no significant extra data structures.**

**\===============================================================================**

**Q686\_2: Repeated String Match (Alternative)**  
**Topic: String**  
**Link: https://leetcode.com/problems/repeated-string-match**

**Approach:**  
**Iterative approach that concatenates string a until its length is sufficient, then uses find() to search for b in the concatenated string. If not found, tries adding the original string a up to 3 more times.**

**Time Complexity: O(k\*n) where k is approximately (m/n \+ 2\) and m is length of b, n is length of a. The find() operations dominate the complexity.**

**Space Complexity: O(k\*n) \- Stores the concatenated string a multiple times in memory.**

**\===============================================================================**

**Q1312: Minimum Insertion Steps to Make a String Palindrome**  
**Topic: String**  
**Link: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/**

**Approach:**  
**Incomplete/Incorrect solution (as noted in comments). Uses a character count approach that doesn't correctly solve the problem. The logic attempts to track unpaired characters but doesn't implement a proper dynamic programming solution.**

**Time Complexity: O(n) where n is length of string s. Single pass through the string.**

**Space Complexity: O(1) \- Only uses a list to track characters, which won't exceed string length.**

**\===============================================================================**

**Summary Table**

| Question | Difficulty | Time Complexity | Space Complexity | Topic |
|----------|-----------|-----------------|------------------|-------|
| Q14      | Easy      | O(S)            | O(1)             | String Matching |
| Q28      | Easy      | O(n*m)          | O(1)             | String Search |
| Q38      | Medium    | O(2^n)          | O(2^n)           | String Generation |
| Q165     | Medium    | O(max(n,m))     | O(n+m)           | Version Comparison |
| Q242     | Easy      | O(n+m)          | O(1)             | Frequency Counting |
| Q686     | Medium    | O(n*m)          | O(1)             | Pattern Matching |
| Q686_2   | Medium    | O(k*n)          | O(k*n)           | Pattern Matching |
| Q1312    | Hard      | O(n)            | O(1)             | DP (Incomplete) |



**\===============================================================================**

**Key Insights & Learning Points**

**1\. String Matching: Multiple approaches exist \- naive, using built-in methods, or optimized algorithms like Boyer-Moore**  
**2\. Frequency Counting: Fixed-size arrays for known character sets are more efficient than hash maps**  
**3\. Recursion: Exponential time complexity (like Q38) requires careful consideration for larger inputs**  
**4\. Padding/Normalization: Sometimes normalizing input (like Q165) simplifies comparison logic**  
**5\. State Tracking: Complex problems benefit from maintaining state at each step (like Q686)**

**\===============================================================================**  
