from collections import defaultdict
class MyDBV1(object):
    def __init__(self):
        self.data = defaultdict(lambda: None)
        self.trans = []
        
    def existInPrevTrans(self, k):
        prevTrans = self.trans[-1]
        for ( ck, _) in prevTrans:
            if k == ck:
                return True
        return False
    
    def set(self, k, v):
        if len(self.trans) > 0:
            if not self.existInPrevTrans(k):
                orig_v = self.data[k]
                self.trans[-1].append((k,orig_v))
        self.data[k] = v

    def get(self, k):
        return self.data[k]
    
    def delete(self, k):
        self.data[k] = None
        
    def count(self, v):
        counter = 0
        for k in self.data:
            if self.data[k] == v:
                counter += 1
        return counter
    
    def begin_trans(self):
        self.trans.append([])

    def commit(self):
        self.trans = []
    
    def rollback(self):
        if len(self.trans) == 0:
            return False
        replay_ops = self.trans.pop()
        for (k,v) in replay_ops:
            self.data[k] = v
        return True


class MyDB(object):
    def __init__(self):
        self.data = defaultdict(lambda: None)
        self.counter_dict = defaultdict(lambda: 0)
        self.trans = []

    def existInCurrentTrans(self, k):
        prevTrans = self.trans[-1]
        for ( ck, _) in prevTrans:
            if k == ck:
                return True
        return False
    
    def set(self, k, v):
        if self.data[k] != v:        
            if len(self.trans) > 0:
                if not self.existInCurrentTrans(k):
                    orig_v = self.data[k]
                    self.trans[-1].append((k,orig_v))
            self.data[k] = v
            self.counter_dict[v] += 1
        else:
            pass # do nothing

    def get(self, k):
        return self.data[k]
    
    def delete(self, k):
        self.set(k, None)
        # self.data[k] = None
        
    def count(self, v):
        return self.counter_dict[v]
    
    def begin_trans(self):
        self.trans.append([])

    def commit(self):
        self.trans = []
    
    def rollback(self):
        if len(self.trans) == 0:
            return False
        replay_ops = self.trans.pop()
        for (k,v) in replay_ops:
            self.data[k] = v
        return True
