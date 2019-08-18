import heapq
class Solution:
    def carPooling(self, trips, capacity):
        heap = []
        curr_cap = 0
        '''sort by start time, end time and capacity respectively'''
        sorted_trip = sorted(trips, key = lambda x: (x[1], x[2], x[0]))
        for passenger, start, end  in sorted_trip:
            curr_cap += passenger
            '''while start time is equal to or greater than first trip's end time; decrease car capacity '''
            while heap and heap[0][0]<=start:
                curr_cap -= heapq.heappop(heap)[1]
            if curr_cap > capacity:
                return False
            heapq.heappush(heap, (end, passenger))
            print(heap)
        return True
