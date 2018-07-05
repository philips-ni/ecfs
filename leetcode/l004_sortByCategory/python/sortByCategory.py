"""
There is an array which has numbers in categories (Low, Medium, High) something like
2 1 3 5 7 9 6
H M H L M L M


You have to sort the numbers according to the category. So after sorting the output of above array will be-
5 9 1 7 6 2 3
L L M M M H H

The input to the function is just an array. And you can assume that you have helper functions which tell if number belong to this category or not, 
isHigh(n), isLow(n), isMedium(n)
You have to sort this in place without using any extra lists.
"""
import functools
cat_level_dict = {
    'H': 2,
    'M': 1,
    'L': 0
}
class Solution(object):
    def sortByCategory(self, l, cat_dict):
        def compare(n1,n2):
            return cat_level_dict[cat_dict[n1]] - cat_level_dict[cat_dict[n2]]
        l.sort(key=functools.cmp_to_key(compare))
