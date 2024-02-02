class Solution:
    def minCostClimbingStairs(self, cost):
        cost.append(0)
        print("Length of cost = "+str(len(cost)))

        for i in range(len(cost)-3,-1,-1):
            print("value of i="+str(i))
            cost[i]+=min(cost[i+1], cost[i+2])
            print(cost)
        return  min(cost[0],cost[1])


c=Solution()
print(c.minCostClimbingStairs([10,15,20])     ) 

