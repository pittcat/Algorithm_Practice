```class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0:
            return 0
        elif n==0:
            return 1
        if n>0:
            positive=True
        else:
            positive=False
        n=abs(n)
        run_result=1
        while n>0:
            run_result*=x
            n-=1

        if positive:
            result=run_result
        else:
            result=1.0/run_result
        return result

moe=Solution()
re=moe.myPow(0.00001,2147483647)
print(re)```

以上为错误解法，会超出时间限制。