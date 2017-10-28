#Determine whether an integer is a palindrome. Do this without extra space.

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        b=[]
        n=0
        x=str(x)
        for each in x:
            b.append(each)
        if '-' in b:
            b.remove('-')
            b.append('-')
            n=1
        b.reverse()
        r=''.join(b)
        if(x==r and n==0):
            return True
        else:
            return False