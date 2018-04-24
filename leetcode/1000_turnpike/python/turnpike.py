# -*- coding: cp936 -*-  
import sys  
  
class turnpike_problem:  
    def __init__(self, n, D):  
        self.x = [0]*(n+1)#从x[1:]表示解   
        self.n = n  
        self.D = D[:]  
        self.D.sort()  
      
    def place(self, n, D, left, right):  
        found_flag = False  
          
        if len(D) == 0:  
            #print '^_^: ',self.x[1:]  
            return True  
  
        Dmax = max(D)  
  
        tmpD = D[:]  
        set_right = True  
        for i in range(1, left)+range(right+1, n+1):  
            if abs(self.x[i]-Dmax) not in tmpD:  
                set_right = False  
                break  
            tmpD.remove(abs(self.x[i]-Dmax))  
          
        if set_right == True:  
            self.x[right] = Dmax  
            for i in range(1, left)+range(right+1, n+1):  
                D.remove(abs(self.x[i]-Dmax))  
  
            found_flag = self.place(n, D, left, right-1)  
  
            if found_flag == False:  
                for i in range(1, left)+range(right+1, n+1):  
                    D.append(abs(self.x[i]-Dmax))  
                #D.sort()  
  
        if found_flag == False:  
            tmpD = D[:]  
            set_left = True  
            for i in range(1, left)+range(right+1, n+1):  
                if abs(self.x[n]-Dmax-self.x[i]) not in tmpD:  
                    set_left = False  
                    break  
                tmpD.remove(abs(self.x[n]-Dmax-self.x[i]))  
                  
            if set_left == True:  
                self.x[left] = self.x[n]-Dmax  
                for i in range(1, left)+range(right+1, n+1):  
                    D.remove(abs(self.x[n]-Dmax-self.x[i]))  
  
                found_flag = self.place(n, D, left+1, right)  
                  
                if found_flag == False:  
                    for i in range(1, left)+range(right+1, n+1):  
                        D.append(abs(self.x[n]-Dmax-self.x[i]))  
                    #D.sort()  
  
        return found_flag  
          
    def turnpike(self, n, D):  
        self.x[n] = max(D)  
        D.remove(self.x[n])  
        self.x[n-1] = max(D)  
        D.remove(self.x[n-1])  
        if self.x[n]-self.x[n-1] in D:  
            D.remove(self.x[n]-self.x[n-1])  
            return self.place(n, D, 2, n-2)  
        else:  
            return False  
  
    def show(self):  
        if self.turnpike(self.n, self.D):  
            print 'found:', self.x[1:]  
        else:  
            print 'not'  
  
def main():  
    sys.setrecursionlimit(1000)  
      
    D = [1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 10]  
    #D = [1, 2, 2, 3, 4, 5]  
  
    t = turnpike_problem(6, D)  
    t.show()  
  
if __name__ == '__main__':  
    main()  
