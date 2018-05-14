class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            print "tortoise: %d, hare: %d" % (tortoise, hare)
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            print "tortoise: %d, hare: %d" % (tortoise, hare)            
            if tortoise == hare:
                break
        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        
        return ptr1
