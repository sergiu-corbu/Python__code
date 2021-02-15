#the minimum of 2 maximums

def trap(height):
    left, right = 0, len(height) -1
    left_wall, right_wall = 0,0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_wall:
                left_wall = height[left] 
            else:
                water += left_wall - height[left]
                left += 1
        else:
            if height[right] >= right_wall:
                right_wall = height[right]
            else:
                water += right_wall - height[right]
                right -= 1
    return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
