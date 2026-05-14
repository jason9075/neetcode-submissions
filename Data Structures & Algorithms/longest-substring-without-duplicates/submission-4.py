class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = {}
        if not s:
            return 0
        
        left = 0
        result = 0
        
        for right in range(len(s)):
            # 如果發現重複，且該字元確實在目前的視窗內 (index >= left)
            # 我們使用 .get() 來檢查，或者直接判斷 key 是否在 record 中
            if s[right] in record and record[s[right]] >= left:
                # 左邊界跳到重複字元位置的下一個
                left = record[s[right]] + 1
            
            # 更新字元最後出現的位置
            record[s[right]] = right
            
            # 計算當前視窗長度：右索引 - 左索引 + 1
            result = max(result, right - left + 1)

        
        return result
                    

        