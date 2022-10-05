class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack = []
        for i in tokens:
            if i == '/':
                v1,v2 = mystack.pop(),mystack.pop()
                mystack.append(int(v2/v1))
            elif i == '-':
                v1,v2 = mystack.pop(),mystack.pop()
                mystack.append(v2-v1)
            elif i == '+':
                mystack.append(mystack.pop()+mystack.pop())
            elif i == '*':
                mystack.append(mystack.pop()*mystack.pop())
            else:
                mystack.append(int(i))
        return mystack[0]
