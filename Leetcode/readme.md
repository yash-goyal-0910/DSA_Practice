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

**Summary Table**

| Question | Difficulty | Time Complexity | Space Complexity | Topic |
|----------|-----------|-----------------|------------------|-------|
| Q14 | Easy | O(S) | O(1) | String Matching |
| Q18 | Medium | O(n³) | O(1) | Multi-pointer |
| Q26 | Easy | O(n) | O(1) | Two Pointer |
| Q27 | Easy | O(n) | O(1) | Two Pointer |
| Q28 | Easy | O(n*m) | O(1) | String Search |
| Q38 | Medium | O(2^n) | O(2^n) | String Generation |
| Q55 | Medium | O(n) | O(1) | Greedy |
| Q80 | Medium | O(n) | O(1) | Two Pointer |
| Q88 | Easy | O(m+n) | O(1) | Merge |
| Q121 | Easy | O(n) | O(1) | Array Tracking |
| Q122 | Medium | O(n) | O(1) | Greedy |
| Q165 | Medium | O(max(n,m)) | O(n+m) | Version Comparison |
| Q169 | Easy | O(n) | O(1) | Voting Algorithm |
| Q189 | Medium | O(n*k) | O(1) | Array Rotation |
| Q242 | Easy | O(n+m) | O(1) | Frequency Counting |
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
