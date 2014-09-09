# From: https://oj.leetcode.com/problems/candy/
# Date: May 28, 2014
# Status: Accepted
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        num = [0]*len(ratings)
        if not ratings:
            return 0
        if len(ratings)==1:
            return 1
        if ratings[0]<= ratings[1]:
            num[0] = 1
        else:
            j =  0
            while j<len(ratings)-1 and ratings[j] > ratings[j+1]:
                j += 1
            num[0] = j+ 1
        i = 1
        while i < len(ratings ) -1:
            right = 1
            if ratings[i] > ratings[i+1]:
               k = 0
               while (i + k) < len(ratings)-1:
                   if ratings[i + k ] >  ratings[i+ k + 1]:
                       k += 1
                   else:
                        break
               for ix in range(k, 0, -1):
                   num[i+ix] = k - ix + 1
               right = k
            else:
                k = 1
            left = num[i-1]

            lcandy = left +1 if ratings[i] > ratings[i-1] else 1
            rcandy = right +1 if ratings[i]> ratings[i+1] else 1
            num[i]= max(lcandy, rcandy)
            i = i + k

        num[-1] = 1 if ratings[-1] <= ratings[-2] else num[-2] + 1
        print(num)
        return sum(num)

if __name__ == "__main__":
    s = Solution()
    print(s.candy([5, 1, 1, 1, 10, 2, 1,1,  1, 13]))
