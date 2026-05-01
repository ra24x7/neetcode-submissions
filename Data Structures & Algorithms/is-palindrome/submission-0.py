class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = "".join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(cs)-1
        while l < r :
            if cs[l] == cs[r]:
                l, r = l+1, r-1
            else:
                return False
        return True

        