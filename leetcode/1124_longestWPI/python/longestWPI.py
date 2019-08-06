"""
class Solution {
public:
    int longestWPI(vector<int>& hours) {
        map<int, int> m;
        int sum = 0;
        int ans = 0;
        for(int i=0;i<hours.size();i++){
            sum += hours[i]>8?1:-1;
            if(sum > 0){
                ans = i+1;
            }else{
                if(m.count(sum-1)){
                    ans = max(ans, i - m[sum-1]);
                }
            }
            if(m.count(sum) == 0){
                m[sum] = i;
            }
            
        }
        return ans;
    }
};

"""

class Solution(object):
    def longestWPI(self, hours):
        m = {}
        s = 0
        ans = 0
        for i in range(len(hours)):
            print("i:{}".format(i))            

            if hours[i] > 8:
                s += 1
            else:
                s -= 1
            print("s:{}".format(s))                            
            if s > 0:
                ans = i + 1
            else:
                if s - 1 in m:
                    ans = max(ans, i-m[s-1])
            if s not in m:
                m[s] = i
            print("ans:{}".format(ans))
            print("m:{}".format(m))            
        return ans
            
                
