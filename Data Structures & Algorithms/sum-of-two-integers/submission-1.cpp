class Solution {
public:
    int getSum(int a, int b) {
        if (a == 0)
            return b;
        while (a != 0){
            // 1. 算出哪些地方有進位（必須先存起來，因為後面 b 會被更動）
            int carry = (int)((uint32_t)(a & b) << 1);
            
            // 2. 算出不進位的加法結果
            b = a ^ b;
            
            // 3. 把進位賦值給 a，繼續下一輪加法
            a = carry;
        }
        return b;

    }
};
