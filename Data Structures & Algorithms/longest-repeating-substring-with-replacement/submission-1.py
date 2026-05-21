from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = Counter()
        left = right = 0
        ans = 0

        def find_max_freq():
            max_freq = 0
            for _,v in table.items():
                max_freq = max(max_freq, v)
            
            return max_freq
        
        for right in range(len(s)):
            # move right
            right_char = s[right]
            table[right_char] += 1

            # move left
            if (right - left + 1) - find_max_freq() > k:
                left_char = s[left]
                table[left_char] -= 1
                left +=1
            ans = max(ans, right-left+1)


        return ans