class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            middle = (left+right) // 2
            row = middle // cols
            column = middle % cols 
            middle_value = matrix[row][column]

            if middle_value == target:
                return True
            elif middle_value < target:
                left = middle + 1
            else: 
                right = middle - 1
        return False

