// soln1: my soln
class Solution:
    def maxScore(self, s: str) -> int:
        su=0
        for u in s:
            su+=int(u)
        n=len(s)
        f=0
        e=0
        j=1
        for i in range(n-1):
            f+=int(s[i])
            l=j-f
            r=su-f
            print(l,r)
            e=max(e,l+r)
            j+=1
        return e
---------------------------------------------------------------------------------
// soln2:
class Solution:
    def maxScore(self, s: str) -> int:
        # Step 1: Count all ones in the string
        right_ones = s.count('1')
        left_zeros = 0
        max_score = 0
        
        # Step 2: Iterate up to len(s) - 1 to guarantee non-empty splits
        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1
                
            # Step 3: Continuously calculate and update the maximum score
            max_score = max(max_score, left_zeros + right_ones)
            
        return max_score


            
