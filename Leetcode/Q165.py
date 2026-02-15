'''
Question topic - String
Question link - https://leetcode.com/problems/compare-version-numbers/description/
'''
# Sol - 
def compareVersion(version1: str, version2: str) -> int:
    version1 = version1.split('.')
    version2 = version2.split('.')
    version1 = [int(x) for x in version1]
    version2 = [int(x) for x in version2]
    l_v1 = len(version1)
    l_v2 = len(version2)
    if l_v1 > l_v2:
        for i in range(l_v1 - l_v2):
            version2.append(0)
    if l_v1 < l_v2:
        for i in range(l_v2 - l_v1):
            version1.append(0)
    if version1 > version2:
        return 1
    elif version1 < version2:
        return -1
    else:
        return 0
