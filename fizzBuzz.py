class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [""]*n
        for i in range(n):
            if (i+1) % 15 == 0:
                res[i] = "FizzBuzz"
            elif (i+1) % 3 == 0:
                res[i] = "Fizz"
            elif (i+1) % 5 == 0:
                res[i] = "Buzz"
            else:
                res[i] = str(i+1)
        return res