
class Solution(object):
    def letterCombinations(self, digits):
        nc_dict = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],            
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]            
        }
        combinations = []        
        if len(digits) == 0:
            return []
        elif len (digits) == 1:
            return nc_dict[digits[0]]
        else:
            tmpSets = self.letterCombinations(digits[:-1])
            for s in tmpSets:
                for e in nc_dict[digits[-1]]:
                    combinations.append( s + e )
        return combinations
        
            
