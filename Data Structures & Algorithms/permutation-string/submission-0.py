from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False
        
        # 統計 s1 的字元頻率
        s1_count = Counter(s1)
        # 初始化 s2 第一個視窗（長度跟 s1 一樣）的字元統計
        window_count = Counter(s2[:n1])
        
        # 如果一開始就中了，直接收工
        if s1_count == window_count:
            return True
            
        # 視窗開始往右滑動，i 代表新加入視窗的右界指標
        for i in range(n1, n2):
            # 1. 右邊新字元進來
            right_char = s2[i]
            window_count[right_char] += 1
            
            # 2. 左邊舊字元移出視窗
            left_char = s2[i - n1]
            window_count[left_char] -= 1
            
            # 為了讓 Counter 比較時完全精準，數量變 0 的字元要砍掉
            if window_count[left_char] == 0:
                del window_count[left_char]
                
            # 3. 檢查當前視窗是否符合
            if s1_count == window_count:
                return True
                
        return False        