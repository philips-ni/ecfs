"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
class Solution(object):
    def groupAnagrams(self, strs):
        # print strs
        sign_dict = {}
        for s in strs:
            signatiure = self.getSign(s)
            # print signatiure
            if signatiure in sign_dict:
                sign_dict[signatiure].append(s)
            else:
                sign_dict[signatiure] = [s]
        # print sign_dict
        return sign_dict.values()

    def getSign(self,s):
        dict = {}
        idx = 0
        while idx < len(s):
            if s[idx] not in dict:
                dict[s[idx]] = 1
            else:
                dict[s[idx]] += 1
            idx += 1
        sign = ""
        for k in sorted(dict):
            sign += "%s%d," %(k, dict[k])
        return sign
