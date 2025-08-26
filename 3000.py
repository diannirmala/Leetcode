import math

class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max_diagonal = 0
        max_area = 0

        for length, width in dimensions: 
            diagonal = math.sqrt(length**2 + width**2)
            area = length * width

            if diagonal > max_diagonal: 
                max_diagonal = diagonal
                max_area = area
            elif diagonal == max_diagonal: 
                max_area = max(max_area, area)

        return max_area
        

solution = Solution()
print(solution.areaOfMaxDiagonal([[1,2],[3,4],[5,6]]))
print(solution.areaOfMaxDiagonal([[3, 9], [8, 6]]))