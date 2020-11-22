class Solution:
    def maxArea(self, height: List[int]) -> int:
    # 1 全遍历
        # final = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         area = (j-i)* min(height[i],height[j])
        #         final = max(area, final)
        # return final

    # 2 左右收敛
        i,j,final = 0,len(height)-1,0
        #以下是我仿照课上的思路java改写成了Python但是一直不对，看了题解以后改成了先计算area的方式。
        #但我还是没想通为什么不对呢？
        # while (i < j):
        #     if (height[i] < height[j]):
        #         i+=1
        #         minheight = height[i]
        #     else:
        #         j-=1
        #         minheight = height[j]
        #     area = (j-i+1) * minheight
        #     final = max(area,final)
        # return final
        while (i<j):
            area = (j-i)*min(height[i],height[j])
            final = max(area,final)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return final


