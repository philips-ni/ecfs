# mul 2 

```
x << 1

>>> x = 100
>>> x << 1
200
```

# div 2

```
x << 1

>>> x = 100
>>> x >> 1
50
>>>
```

# Check if the number is even of not

```
x & 1

>>> a,b = 100,101
>>> a & 1
0
>>> b &1
1
```

# Clear the rightmost 'set 1' bit from a integer

```
x & (x - 1)

>>> x = 100
>>> bin(x)
'0b1100100'
>>> y = x & (x - 1)
>>> bin(y)
'0b1100000'
>>>
```

# Get the No i bit value of a integer

```
(x >> i) & 1

>>> x = 100
>>> bin(x)
'0b1100100'
>>> (x >> 1) &1
0
>>> (x >> 2) &1
1
>>> (x >> 5) &1
1
>>>
```

# Set the No. i bit of interger to 1
```
x | (1 << i)

>>> x = 100
>>> bin(x)
'0b1100100'
>>> y = x | (1 << 1)
>>> bin(y)
'0b1100110'
>>>
```
# Set the No. i bit of interger to 0

```
x & (~(1 << i))

>>> x = 100
>>> y = x & (~(1 << 5 ))
>>> bin(y)
'0b1000100'
>>>
```

# Flip the No. i bit of a integer
```
x ^ (1 << i)

>>> x = 100
>>> bin(x)
'0b1100100'
>>> y = x ^ (1 << 1)
>>> bin(y)
'0b1100110'
>>> y = x ^ (1 << 2)
>>> bin(y)
'0b1100000'
>>> y = x ^ (1 << 5)
>>> bin(y)
'0b1000100'
>>>
```

# Flip the No. i bit and No.j bit of a integer
```
x ^ (1 << i | 1 << j)

>>> x = 100
>>> bin(x)
'0b1100100'
>>> y = x ^ (1 << 1 | 1 << 2)
>>> bin(y)
'0b1100010'
>>>
```

# Reference
  - http://graphics.stanford.edu/~seander/bithacks.html
