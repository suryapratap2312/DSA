50. Pow(x, n)

#Method-1
Brute Force

just multiply it n times , take care if n is -ve

    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n>0:
            for i in range(n):
                result *=x
        else:
            for i in range(abs(n)):
                result *=(1/x)
        return result
        
        
 TC - O(n)
 SC - o(1)
 
 
 #Method-2 : Fast Power Algorithm Recursive
     def fastPow(self, x : float, n:int) -> float:
        if n == 0 :
            return 1.0
        half = self.fastPow(x, n//2)
        if n%2 == 0:
            return half*half
        else:
            return half*half*x
    
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x

            n = -n
        return self.fastPow(x,n)    
        
        
TC - O(logn)
SC - O(logn)


#Method-3 : Approach 3: Fast Power Algorithm Iterative
##########PENDING##############33

TC - O(logn)
SC- O(1)
