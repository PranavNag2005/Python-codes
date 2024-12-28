s=input("enter the postfix expression ")
def evaluate(s):
    stack=[]
    for char in s:
        if char.isdigit():
            stack.append(int(char))
        else:
            b=stack.pop()
            a=stack.pop()
            if char=='+':
                stack.append(a+b)
            elif char=='-':
                stack.append(a-b)
            elif char=='*':
                stack.append(a*b)
            elif char=='/':
                stack.append(a//b)
    return stack[0]

print(evaluate(s))


