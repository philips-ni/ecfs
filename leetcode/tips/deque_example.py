import collections

"""
d = collections.deque("abcdefg")
print 'Deque:', d
print 'Length:', len(d)
print 'Left end:', d[0]
print 'Right end:', d[-1]

d.remove('c')
print 'remove(c):', d


d = collections.deque(["ab","c","d"])
print 'Deque:', d
print 'Length:', len(d)
print 'Left end:', d[0]
print 'Right end:', d[-1]

d.remove('c')
print 'remove(c):', d

d = collections.deque([1,2,3,4])
print 'Deque:', d
print 'Length:', len(d)
print 'Left end:', d[0]
print 'Right end:', d[-1]

d.remove(3)
print 'remove(c):', d


######Populating
# Add to the right
d = collections.deque()
d.extend('abcdefg')
print 'extend    :', d
d.append('h')
print 'append    :', d

# Add to the left
d = collections.deque()
d.extendleft('abcdefg')
print 'extendleft:', d
d.appendleft('h')
print 'appendleft:', d
"""

#### Genernal Queque OP
d = collections.deque()
d.append(1)
d.append(2)
print d
a = d.popleft()
print a
print d
