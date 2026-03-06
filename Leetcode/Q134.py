'''
Question topic - Array
Question link - https://leetcode.com/problems/gas-station
'''
# Sol - 
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    n = len(gas)
    s = 0
    tank = 0
    k = 0
    for i in range(n):
        temp = gas[i] - cost[i]
        s += temp
        tank += temp
        if tank < 0:
            k = i + 1
            tank = 0        
    if s < 0:
        return -1
    else:
        return k
        
    
print(canCompleteCircuit([6,1,4,3,5],[3,8,2,4,2]))