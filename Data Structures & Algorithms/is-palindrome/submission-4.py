class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        if len(s) <=1:
            return True

        s = s.lower()
        while left<right:
            # move left
            while not s[left].isalnum():
                if(left==len(s)-1):
                    return True
                left +=1 

            # move right
            while not s[right].isalnum():
                right -=1
        
            if left >= right:
                return True

            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True