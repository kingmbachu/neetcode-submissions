class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            water_height = min(heights[left], heights[right])
            area = width * water_height

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

            if area > max_area:
                max_area = area

        return max_area
  