'''
Question topic - Array
Question link - https://leetcode.com/problems/longest-substring-without-repeating-characters/description
'''
# Sol - 
def longest_subarray(s):
    st = []
    m = 0
    n = 0
    for x in s:
        if x in st:
            m = max(m,n)
            n = len(st) - (st.index(x) + 1)
            st = st[st.index(x)+1::]
            n += 1
            st.append(x)
        else:
            n += 1
            st.append(x)
    m = max(m,n)
    return m

print(longest_subarray(" "))