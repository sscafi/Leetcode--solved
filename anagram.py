class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Convert both strings to lowercase and remove whitespace
        s = s.lower().replace(" ", "")
        t = t.lower().replace(" ", "")

        # Check if the lengths of the strings are equal
        if len(s) != len(t):
            return False

        # Create dictionaries to count the frequency of each character
        count_s = {}
        count_t = {}

        # Count the frequency of characters in s
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        # Count the frequency of characters in t
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # Compare the dictionaries
        if count_s == count_t:
            return True
        else:
            return False