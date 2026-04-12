**LeetCode Solutions - Time & Space Complexity Analysis**

**Repository: yash-goyal-0910/DSA_Practice**
**Folder: Leetcode**

**Overview**
**This document provides a comprehensive analysis of all LeetCode solutions in the repository, including detailed time and space complexity breakdowns for each problem.**

===============================================================================

**Q14: Longest Common Prefix**
**Topic: String**
**Link: https://leetcode.com/problems/longest-common-prefix/**

**Approach:**
**The solution iterates through each string and compares characters at each position with the longest string found so far. It maintains a running `longest` variable that gets trimmed whenever characters don't match.**

**Time Complexity: O(S) where S is the sum of all characters in all strings. In the worst case, we compare every character of every string.**

**Space Complexity: O(1) - Only using a constant amount of extra space for the longest variable (excluding output).**

===============================================================================

**Q18: 4Sum**
**Topic: Array**
**Link: https://leetcode.com/problems/4sum/**

**Approach:**
**Sorts the array first, then uses nested loops with two pointers to find all unique quadruplets that sum to the target value. The two-pointer approach reduces the innermost operation from O(n) to O(1) amortized. Handles duplicates by skipping repeated values.**

**Time Complexity: O(n³) where n is the length of the array. Sorting is O(n log n), followed by three nested loops with two-pointer comparisons in the innermost loop.**

**Space Complexity: O(1) - Only using pointers and variables for computation (excluding the output array).**

===============================================================================

**Q26: Remove Duplicates from Sorted Array**
**Topic: Array**
**Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/**

**Approach:**
**Two-pointer technique where one pointer tracks the position to write unique elements and another iterates through the array. When a new unique value is found, it's placed at the write position and counter is incremented.**

**Time Complexity: O(n) where n is the length of the array. Single pass through the array with constant operations at each step.**

**Space Complexity: O(1) - In-place modification using only constant extra space for pointers.**

===============================================================================

**Q27: Remove Element**
**Topic: Array**
**Link: https://leetcode.com/problems/remove-element/**

**Approach:**
**Two-pointer technique. Iterates through the array, and when the target value is found, it's swapped with an element from the end of the valid portion, effectively removing it. Tracks the new length as elements are removed.**

**Time Complexity: O(n) where n is the length of the array. Single pass through the array.**

**Space Complexity: O(1) - In-place modification with only constant extra space used.**

===============================================================================

**Q28: Implement strStr()**
**Topic: String**
**Link: https://leetcode.com/problems/implement-strstr/**

**Approach:**
**Uses Python's built-in string.find() method which internally uses an optimized string matching algorithm (likely Boyer-Moore or similar for efficiency).**

**Time Complexity: O(n*m) in worst case where n is length of haystack and m is length of needle. Built-in Python implementation is highly optimized for average cases.**

**Space Complexity: O(1) - No extra space used beyond the built-in method's implementation.**

===============================================================================

**Q38: Count and Say**
**Topic: String**
**Link: https://leetcode.com/problems/count-and-say/**

**Approach:**
**Recursive solution that builds the sequence iteratively. For each number n, it calls count_say(n-1) and then applies the "count and say" logic by iterating through the result, counting consecutive identical characters and building the next sequence.**

**Time Complexity: O(2^n) - The sequence grows exponentially. Each sequence can be roughly twice as long as the previous one in the worst case, leading to exponential growth.**

**Space Complexity: O(2^n) - The recursion depth is n, and each level stores the string result which grows exponentially.**

===============================================================================

**Q55: Jump Game**
**Topic: Array**
**Link: https://leetcode.com/problems/jump-game/**

**Approach:**
**Greedy algorithm that tracks the maximum index reachable from the starting position. As we iterate through the array, we update the maximum jump reach. If at any point we can't reach further, we stop. Returns True if maximum reach is >= array length - 1.**

**Time Complexity: O(n) where n is the length of the array. Single pass through array with constant operations at each index.**

**Space Complexity: O(1) - Only using variables to track the maximum reachable index.**

===============================================================================

**Q80: Remove Duplicates from Sorted Array II**
**Topic: Array**
**Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/**

**Approach:**
**Two-pointer approach that allows at most 2 occurrences of each element. Maintains a counter for occurrences and only moves elements to the write position when count is <= 2. Handles this by comparing with the element two positions back.**

**Time Complexity: O(n) where n is the length of the array. Single pass through array to identify and position elements.**

**Space Complexity: O(1) - In-place modification using constant extra space for pointers and counter.**

===============================================================================

**Q88: Merge Sorted Array**
**Topic: Array**
**Link: https://leetcode.com/problems/merge-sorted-array/description**

**Approach:**
**Three-pointer technique starting from the end of both arrays. Compares elements from the end of nums1 and nums2, placing the larger element at the end of nums1, moving backwards. This avoids overwriting elements in nums1 that haven't been merged yet.**

**Time Complexity: O(m + n) where m and n are the lengths of nums1 and nums2 respectively. Single pass through both arrays from end to beginning.**

**Space Complexity: O(1) - In-place merge using the end of nums1 as storage space, requiring no extra arrays.**

===============================================================================

**Q121: Best Time to Buy and Sell Stock**
**Topic: Array**
**Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/**

**Approach:**
**Tracks the minimum price seen so far as we iterate through the prices array. At each price, calculates the potential profit if we sell at that price, and updates the maximum profit found. One pass solution.**

**Time Complexity: O(n) where n is the length of the prices array. Single pass through array maintaining running minimum and maximum profit.**

**Space Complexity: O(1) - Only using variables for tracking minimum price and maximum profit.**

===============================================================================

**Q122: Best Time to Buy and Sell Stock II**
**Topic: Array**
**Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/**

**Approach:**
**Greedy approach that captures every upward price movement. Iterates through prices and whenever the next price is higher than current price, adds the difference to total profit. This accumulates all possible gains.**

**Time Complexity: O(n) where n is the length of the prices array. Single pass through array comparing consecutive elements.**

**Space Complexity: O(1) - Only using variables to track previous price and accumulated profit.**

===============================================================================

**Q165: Compare Version Numbers**
**Topic: String**
**Link: https://leetcode.com/problems/compare-version-numbers/description/**

**Approach:**
**Splits both version strings by '.', converts to integers, pads with zeros to make them equal length, then compares element by element to determine which version is larger.**

**Time Complexity: O(max(n, m)) where n is the number of version parts in version1 and m is the number of parts in version2. We iterate through each part once.**

**Space Complexity: O(n + m) - Space needed for the split lists and potentially padding with zeros.**

===============================================================================

**Q169: Majority Element**
**Topic: Array**
**Link: https://leetcode.com/problems/majority-element/**

**Approach:**
**Boyer-Moore Voting Algorithm. Maintains a candidate and a count. Increments count when seeing candidate, decrements for others. When count reaches 0, replaces candidate. The element appearing more than n/2 times is guaranteed to survive this process.**

**Time Complexity: O(n) where n is the length of the array. Single pass to find candidate, optionally a second pass to verify (total still O(n)).**

**Space Complexity: O(1) - Only using variables for tracking candidate and count.**

===============================================================================

**Q189: Rotate Array**
**Topic: Array**
**Link: https://leetcode.com/problems/rotate-array/**

**Approach:**
**Rotation by repeatedly inserting the last element at the beginning and removing it from the end. This is done k times where k is the number of positions to rotate. Uses Python's insert and pop operations.**

**Time Complexity: O(n*k) where n is the array length and k is the rotation steps. Each insert(0) operation requires shifting all elements, making it O(n) per rotation.**

**Space Complexity: O(1) - In-place rotation using only constant extra space (excluding Python's built-in operation overhead).**

===============================================================================

**Q242: Valid Anagram**
**Topic: String**
**Link: https://leetcode.com/problems/valid-anagram/description/**

**Approach:**
**Uses a fixed-size array (26 for lowercase letters) to count character frequencies. Increments count for characters in string s, decrements for string t. If all counts are zero at the end, strings are anagrams.**

**Time Complexity: O(n + m) where n is length of s and m is length of t. We iterate through each string once.**

**Space Complexity: O(1) - Uses a fixed-size array of 26 elements for lowercase English letters, which is constant space.**

===============================================================================

**Q686 (Solution 1): Repeated String Match**
**Topic: String**
**Link: https://leetcode.com/problems/repeated-string-match**

**Approach:**
**Complex logic checking if string b can be formed by repeating string a. Validates alignment, checks character sequences, and handles edge cases. Determines how many times to repeat a based on length of b.**

**Time Complexity: O(n*m) where n is length of a and m is length of b. Multiple string find() operations and character-by-character comparisons.**

**Space Complexity: O(1) - Only using variables for indices and counts, no significant extra data structures.**

===============================================================================

**Q686_2: Repeated String Match (Alternative)**
**Topic: String**
**Link: https://leetcode.com/problems/repeated-string-match**

**Approach:**
**Iterative approach that concatenates string a until its length is sufficient, then uses find() to search for b in the concatenated string. If not found, tries adding the original string a up to 3 more times.**

**Time Complexity: O(k*n) where k is approximately (m/n + 2) and m is length of b, n is length of a. The find() operations dominate the complexity.**

**Space Complexity: O(k*n) - Stores the concatenated string a multiple times in memory.**

===============================================================================

**Q1312: Minimum Insertion Steps to Make a String Palindrome**
**Topic: String**
**Link: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/**

**Approach:**
**Incomplete/Incorrect solution (as noted in comments). Uses a character count approach that doesn't correctly solve the problem. The logic attempts to track unpaired characters but doesn't implement a proper dynamic programming solution.**

**Time Complexity: O(n) where n is length of string s. Single pass through the string.**

**Space Complexity: O(1) - Only uses a list to track characters, which won't exceed string length.**

===============================================================================

**Q11: Container With Most Water**
**Topic: Array**
**Link: https://leetcode.com/problems/container-with-most-water**

**Approach:**
**Two-pointer approach. Starts with pointers at the beginning and end. Calculates area, updates max area. Then it skips pointers inwards if they aren't taller than the current 'high'. It uses an optimization to skip multiple shorter lines dynamically.**

**Time Complexity: O(n) where n is the length of the height array. Both pointers only move inwards once, overall iterating n times.**

**Space Complexity: O(1) - Only using constant extra space for pointers, width, and max area tracking.**

===============================================================================

**Q15: 3Sum**
**Topic: Array**
**Link: https://leetcode.com/problems/3sum**

**Approach:**
**Divides the input array into lists of negative, positive, and zero numbers. Constructs unique triplets efficiently by using sets to verify matching numbers without nested loops for all three elements. Uses a combination of separate collections iteration to hit `O(n^2)` time overall since we use two nested loops targeting subsets of the input.**

**Time Complexity: O(n²) where n is the length of the array, due to nested loops exploring combinations in positive and negative subset arrays.**

**Space Complexity: O(n) - Extra space used to store positive, negative, and zero arrays and sets to avoid duplications.**


**Q3: Longest Substring Without Repeating Characters**
**Topic: Sliding Window**
**Link: https://leetcode.com/problems/longest-substring-without-repeating-characters**

**Approach:**
**Uses a sliding window approach maintaining a queue/list for current substring. If a repeating character is found, it updates max length, removes elements up to the duplicate from the list, and continues. O(N^2) time due to `.index()` inside loop.**

**Time Complexity: O(N^2) where N is length of string due to list search.**

**Space Complexity: O(N) array for tracking substring.**

===============================================================================

**Q12: Integer to Roman**
**Topic: Math / String**
**Link: https://leetcode.com/problems/integer-to-roman**

**Approach:**
**Converts number to string and builds Roman numeral character by character by dividing the base by powers of 10. Handles 4 and 9 as special edge cases explicitly appending equivalent combinations.**

**Time Complexity: O(log N) based on length of the number.**

**Space Complexity: O(log N) for storing list of roman letters.**

===============================================================================

**Q20: Valid Parentheses**
**Topic: String / Stack**
**Link: https://leetcode.com/problems/valid-parentheses**

**Approach:**
**Uses a stack to keep track of open brackets. Iterates through the string, pushing open brackets to stack, and when closing bracket is found, checks if it matches the top of the stack. Uses a dictionary for mapping.**

**Time Complexity: O(N) where N is string length.**

**Space Complexity: O(N) for stack worst case.**

===============================================================================

**Q30: Substring with Concatenation of All Words**
**Topic: Sliding Window / Hash Map**
**Link: https://leetcode.com/problems/substring-with-concatenation-of-all-words**

**Approach:**
**Iterates through possible starting windows in the string. For each window, extracts word chunks and checks against a frequency dictionary of required words. If valid, records the starting index.**

**Time Complexity: O(N * M) overall where N is length of string and M is number of words, due to re-checking substrings within window.**

**Space Complexity: O(W) where W is number of words for temporary dictionary per window.**

===============================================================================

**Q42: Trapping Rain Water**
**Topic: Array / Two Pointers**
**Link: https://leetcode.com/problems/trapping-rain-water**

**Approach:**
**Attempts a two-pointer approach tracking minimum depth inward. Modifies an auxiliary array iteratively to log water heights. Performs subsequent array iteration to compute differences.**

**Time Complexity: O(N^2) in worst case due to nested assignments over height sub-arrays.**

**Space Complexity: O(N) for storing the depth profile array.**

===============================================================================

**Q45: Jump Game II**
**Topic: Array / Greedy**
**Link: https://leetcode.com/problems/jump-game-ii**

**Approach:**
**Implicit BFS / Greedy strategy tracking farthest point reachable at current level boundaries. When iteration reaches the end of current jump level, increments jump count and shifts boundary.**

**Time Complexity: O(N) looping through array once.**

**Space Complexity: O(1) storing boundary integers.**

===============================================================================

**Q76: Minimum Window Substring**
**Topic: Sliding Window**
**Link: https://leetcode.com/problems/minimum-window-substring**

**Approach:**
**Employs a sliding window over string `s` tracking characters found from target `t`. Two pointers expand or contract window while maintaining validation criteria on a frequency map. Returns shortest valid window.**

**Time Complexity: O(N) amortized for two pointer shifts. Dictionary check incurs minor bounded overhead.**

**Space Complexity: O(K) where K is unique characters in `t`.**

===============================================================================

**Q125: Valid Palindrome**
**Topic: String**
**Link: https://leetcode.com/problems/valid-palindrome**

**Approach:**
**Filters the original string to extract only alphanumeric characters, normalizes to lowercase, and then checks if the resulting string matches its reverse using Python slicing.**

**Time Complexity: O(N) where N is length of string.**

**Space Complexity: O(N) for constructing normalized copied string.**

===============================================================================

**Q134: Gas Station**
**Topic: Array / Greedy**
**Link: https://leetcode.com/problems/gas-station**

**Approach:**
**Maintains total gas variance and a local tank counter across stations. If local tank dips below zero over a stretch, resets the starting candidate position to the next station.**

**Time Complexity: O(N) iterating through stations sequentially once.**

**Space Complexity: O(1) no extra arrays needed.**

===============================================================================

**Q135: Candy**
**Topic: Array / Greedy**
**Link: https://leetcode.com/problems/candy**

**Approach:**
**Uses two sequential passes. First pass left-to-right ensures children with higher ratings than left neighbors get more candy. Second pass right-to-left ensures valid distributions based on right neighbors. Sums results.**

**Time Complexity: O(N) for the two full passes.**

**Space Complexity: O(N) for the candies tracking array.**

===============================================================================

**Q167: Two Sum II**
**Topic: Array / Two Pointers**
**Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted**

**Approach:**
**Utilizes the sorted nature of input by starting two pointers at extremes. Contracts window by incrementing left or decrementing right pointer depending on sum relative to target.**

**Time Complexity: O(N) pointers cross inward exactly once.**

**Space Complexity: O(1) in-place comparison.**

===============================================================================

**Q209: Minimum Size Subarray Sum**
**Topic: Sliding Window**
**Link: https://leetcode.com/problems/minimum-size-subarray-sum**

**Approach:**
**Uses a sliding window to dynamically expand `j` when current sum is below target, and shrink `i` incrementally recording minimum valid window sizes when condition is met.**

**Time Complexity: O(N) each element visited at most twice.**

**Space Complexity: O(1) maintaining running sum integer.**

===============================================================================

**Q238: Product of Array Except Self**
**Topic: Array / Prefix Sum**
**Link: https://leetcode.com/problems/product-of-array-except-self**

**Approach:**
**Calculates total non-zero product and counts zeros. Constructs result by dividing total product by current item, handling explicitly cases where zeros exist in input.**

**Time Complexity: O(N) standard iteration.**

**Space Complexity: O(N) resulting array allocation.**

===============================================================================

**Q274: H-Index**
**Topic: Array / Sorting**
**Link: https://leetcode.com/problems/h-index**

**Approach:**
**Sorts the citation array and linearly iterates evaluating remaining length criteria against citation values to trace out valid max configurations. Optimized for quick returns natively.**

**Time Complexity: O(N log N) dominated by sorting step.**

**Space Complexity: O(N) via sorted internal array structure.**

===============================================================================

**Q380: Insert Delete GetRandom O(1)**
**Topic: Array / OOP / Math**
**Link: https://leetcode.com/problems/insert-delete-getrandom-o1**

**Approach:**
**Implements a data structure primarily relying on native set operations for distinct containment tracking and uses random module lists explicitly for probability retrieval.**

**Time Complexity: O(1) amortized for add/remove. `getRandom` may degrade over `list()` casting in Python.**

**Space Complexity: O(N) internal set state length.**

===============================================================================

**Q392: Is Subsequence**
**Topic: Array / Two Pointers**
**Link: https://leetcode.com/problems/is-subsequence**

**Approach:**
**Iterates simultaneously comparing string sequences via two pointers padding indices if matching targets are aligned. Checks total sub-match count against candidate sequence length.**

**Time Complexity: O(N) upper bound governed by `t`.**

**Space Complexity: O(1) standard integers.**

===============================================================================
===============================================================================

**Summary Table**

| Question | Difficulty | Time Complexity | Space Complexity | Topic |
|----------|-----------|-----------------|------------------|-------|
| Q3  | Medium | O(N^2) | O(N)  | Sliding Window |
| Q11  | Medium | O(n)  | O(1)  | Two Pointer |
| Q12  | Medium | O(log N) | O(log N)  | String/Math |
| Q14 | Easy | O(S) | O(1) | String Matching |
| Q15  | Medium | O(n²) | O(n)  | Array Hash/Set |
| Q18 | Medium | O(n³) | O(1) | Multi-pointer |
| Q20  | Easy | O(N) | O(N)  | String/Stack |
| Q26 | Easy | O(n) | O(1) | Two Pointer |
| Q27 | Easy | O(n) | O(1) | Two Pointer |
| Q28 | Easy | O(n*m) | O(1) | String Search |
| Q30  | Hard | O(N*M) | O(W)  | Sliding Window |
| Q38 | Medium | O(2^n) | O(2^n) | String Generation |
| Q42  | Hard | O(N^2) | O(N)  | Array/Two Pointers |
| Q45  | Medium | O(N) | O(1)  | Greedy |
| Q55 | Medium | O(n) | O(1) | Greedy |
| Q76  | Hard | O(N) | O(K)  | Sliding Window |
| Q80 | Medium | O(n) | O(1) | Two Pointer |
| Q88 | Easy | O(m+n) | O(1) | Merge |
| Q121 | Easy | O(n) | O(1) | Array Tracking |
| Q122 | Medium | O(n) | O(1) | Greedy |
| Q125  | Easy | O(N) | O(N)  | String |
| Q134  | Medium | O(N) | O(1)  | Greedy |
| Q135  | Hard | O(N) | O(N)  | Greedy |
| Q165 | Medium | O(max(n,m)) | O(n+m) | Version Comparison |
| Q167  | Medium | O(N) | O(1)  | Two Pointers |
| Q169 | Easy | O(n) | O(1) | Voting Algorithm |
| Q189 | Medium | O(n*k) | O(1) | Array Rotation |
| Q209  | Medium | O(N) | O(1)  | Sliding Window |
| Q238  | Medium | O(N) | O(N)  | Array/Prefix Sum |
| Q242 | Easy | O(n+m) | O(1) | Frequency Counting |
| Q274  | Medium | O(N log N) | O(N)  | Array/Sorting |
| Q380  | Medium | O(1) | O(N)  | Array/OOP |
| Q392  | Easy | O(N) | O(1)  | Two Pointers |
| Q686 | Medium | O(n*m) | O(1) | Pattern Matching |
| Q686_2 | Medium | O(k*n) | O(k*n) | Pattern Matching |
| Q1312 | Hard | O(n) | O(1) | DP (Incomplete) |

===============================================================================

**Key Insights & Learning Points**

**1. String Matching: Multiple approaches exist - naive, using built-in methods, or optimized algorithms like Boyer-Moore**

**2. Frequency Counting: Fixed-size arrays for known character sets are more efficient than hash maps**

**3. Recursion: Exponential time complexity (like Q38) requires careful consideration for larger inputs**

**4. Padding/Normalization: Sometimes normalizing input (like Q165) simplifies comparison logic**

**5. State Tracking: Complex problems benefit from maintaining state at each step (like Q686)**

**6. Two Pointers: Efficient technique for sorted arrays (Q26, Q27, Q80, Q88)**

**7. Greedy Algorithms: For problems like Jump Game and Stock Trading, greedy approaches yield optimal solutions**

**8. Voting Algorithm: Boyer-Moore voting is elegant for majority element problems**

===============================================================================
