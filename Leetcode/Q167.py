'''
Question topic - Array
Question link - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
'''
# Sol - 
def twoSum(numbers: List[int], target: int) -> List[int]:
    i,j = 0,len(numbers)-1
    while i < j:
        while target > (numbers[i]+numbers[j]) and i < j:
            i += 1
        while target < (numbers[i]+numbers[j]) and i < j:
            j -= 1
        if target == (numbers[i]+numbers[j]):
            return [i+1,j+1]

print(twoSum([2,7,11,15],9))