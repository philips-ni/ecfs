import collections
class Solution(object):
    def isNStraightHand(self, hand, W):
        if len(hand)%W: return False        
        count = collections.Counter(hand)
        print(count)
        while count:
            m = min(count)
            print(m)
            for k in xrange(m, m+W):
                v = count[k]
                if not v: return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1
        return True
class Solution1(object):
    def isNStraightHand(self, hand, W):
        if len(hand)%W: return False
        C=collections.Counter(hand)
        print(C)
        for n in set(hand):
            if C[n]:
                for i in range(n,n+W):
                    if not C[i]:return False
                    C[i]-=1
        return True
    def isNStraightHand2(self, hand, W):
        if len(hand) == 0:
            return False
        elif len(hand) % W != 0:
            return False
        else:
            sorted_hand = sorted(hand)
            return self.isNStraightHandFromSortedH(sorted_hand, W)
    def isNStraightHandFromSortedH(self, hand, W):
        if len(hand) == 0:
            return True
        min_v = hand[0]
        sublist = range(min_v, min_v + W)
        # print(sublist)
        # print(hand)
        if self.isSubList(sublist, hand):
            hand = self.removeSubList(sublist, hand)
            # print(hand)
            return self.isNStraightHandFromSortedH(hand,W)
        else:
            # print("I'm here")
            return False
    
    def isSubList(self, sublist, l):
        return all(elem in l for elem in sublist)

    def removeSubList(self, sublist, l):
        for elem in sublist:
            # print("removing {}".format(elem))
            l.remove(elem)
        return l
