
class Solution(object):
    def simplifyPath(self, s):
        stack = []
        l  = [item for item in s.split("/") if item != ""]
        for item in l:
            if item == ".":
                next
            elif item == "..":
                if len(stack) == 0:
                    next
                else:
                    stack.pop()
            else:
                stack.append(item)
        return "/" + "/".join(stack)
