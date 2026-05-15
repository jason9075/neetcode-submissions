class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find first column
        up = 0
        down = len(matrix)-1

        if matrix[up][0] == target or matrix[down][0] == target:
            return True

        while up < down:

            mid = up + (down - up) // 2
            if matrix[mid][0] == target:
                return True
            
            if target < matrix[mid][0]:
                down = mid - 1
            else:
                up = mid + 1
        
        left = 0
        right = len(matrix[0])-1

        # find row
        if len(matrix)==1:
            column_idx = 0
        elif target < matrix[mid][0]:
            column_idx = up
        elif matrix[down][0] < target:
            column_idx = down
        else:
            column_idx = mid

        if matrix[column_idx][left] == target or matrix[column_idx][right] == target:
            return True

        while left < right:

            mid = left + (right - left)//2
            print(column_idx)
            if matrix[column_idx][mid] == target:
                return True
            if matrix[column_idx][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return False
            

        