from functools import reduce
class Solution(object):
    def dayOfYear(self, date):
        days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        leaf_days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
        (year_s, month_s,day_s) = date.split('-')
        year = int(year_s)
        month = int(month_s)
        day = int(day_s)
        
        ret = 0
        if self.isLeafYear(year):
            ret = reduce(lambda x,y: x+y, leaf_days[0:month]) + day
        else:
            ret = reduce(lambda x,y: x+y, days[0:month]) + day
        return ret

    def isLeafYear(self, year):
        if year % 4 == 0 and year % 100 !=0:
            return True
        if year % 100 == 0 and year % 400 == 0:
            return True
        return False
