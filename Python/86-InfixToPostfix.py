
def infixToPostfix(infix):
    postfix = str()
    stack = list()

    for ch in infix:
        if ch == ' ':
            pass
        elif ch == '(':
            stack.append(ch)
        elif ch == '*' or ch == '/':
            stack.append(ch)
        elif ch == '+' or ch == '-':
            if len(stack) == 0:
                stack.append(ch)
            elif stack[len(stack) - 1] == '(':
                stack.append(ch)
            else:
                while len(stack) != 0 and stack[len(stack) - 1] != '(':
                    postfix += stack.pop()

                stack.append(ch)

        elif ch == ')':
            while len(stack) != 0 and stack[len(stack) - 1] != '(':
                    postfix += stack.pop()

            stack.pop()
        else:
            postfix += ch
    while len(stack) != 0:
        if stack[len(stack) - 1] != '(' and stack[len(stack) -1] != ')':
            postfix += stack.pop()

    return postfix

import re
while True:
    user = input("Enter the Expression : ")

    us = re.findall(f"[%$#&]","user")

    if not us:
        print("Postfix : " , infixToPostfix(user))
        
        ch  = input("Do you want to convert more expressions (y/n)?")
        if ch == 'y' or ch == 'Y':
            pass
        elif ch == 'N' or ch == 'n':
            break
        else:
            print("Invalid Input.")

    else:
        print("Expression can't contain special chracters.")
    
                    





