class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        max_len = 0
        char_map = {} # to track charecters in their position
        # to traverse through the loop
        for i in range ( len(s)):
            # to check if current charecter is already in the window
            if s[i] in char_map:

                #update the start of the window

                start = max(start, char_map[s[i]] + 1)
            # add current and its position to the map    
            char_map [s[i]] = i

            # update the maximum length of the window 
            max_len = max(max_len , i - start + 1)

        return max_len
