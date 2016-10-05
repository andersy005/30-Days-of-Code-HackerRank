"""Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring. """


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        left = 0
        last = {}
        
        for i in range(len(s)):
            # if the character is alredy in the dict, increment left
            if s[i] in last and last[s[i]] >= left:
                left = last[s[i]] + 1
                
        
            # if the char is not in dict alread, add it with a key being its index
            last[s[i]] = i 
            ans = max(ans, i - left + 1)
            
        return ans