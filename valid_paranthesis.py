#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

def match(a,b):
        if(a=='[' and b==']'):
            return 1
        elif(a=='{' and b =='}'):
            return 1
        elif(a=='(' and b==')'):
            return 1
        else:
            return 0

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        a=[]
        b=[]
    
        for each in s:
            a.append(each)
        for i in range(0,len(a)):
            if(a[i]=='[' or a[i]=='{' or a[i]=='('):
                b.append(a[i])
            elif a[i]==']'or a[i]=='}' or a[i]==')':
                if (len(b)==0):
                    return False
                elif (match(b[len(b)-1],s[i])):
                    del b[-1]
                else:
                    return False
        if(len(b)):
            return False
        else:
            return True
       