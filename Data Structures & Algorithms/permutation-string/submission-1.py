from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False
        
        # 1. 建立 s1 的 Hash Map
        s1_map = {}
        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1
            
        # 2. 建立 s2 第一個視窗 (長度為 n1) 的 Hash Map
        window_map = {}
        for i in range(n1):
            char = s2[i]
            window_map[char] = window_map.get(char, 0) + 1
            
        # 如果第一個視窗就剛好配對成功
        if s1_map == window_map:
            return True
            
        # 3. 開始滑動視窗 (i 代表新加入視窗的右界指標)
        for i in range(n1, n2):
            # 右邊新字元進入視窗
            right_char = s2[i]
            window_map[right_char] = window_map.get(right_char, 0) + 1
            
            # 左邊舊字元離開視窗
            left_char = s2[i - n1]
            window_map[left_char] -= 1
            
            # 關鍵：如果計數歸零，必須把 Key 徹底拔除，否則兩個 dict 在比較 == 時會因為多出這個 Key 而失敗
            if window_map[left_char] == 0:
                del window_map[left_char]
                
            # 直接比較兩個指標（Python 的 dict 比較不看順序，只看 Key-Value 是否完全相同）
            if s1_map == window_map:
                return True
                
        return False       