# Adapted from pseudocode at:
# https://en.wikipedia.org/wiki/Shunting-yard_algorithm

def shunt(infix):
    """Convert infix expressions to postfix."""
    #The eventual output.
    postfix = ""
    #the shunting yard operator stack.
    stack = ""
    #operator precedence
    prec = {'*': 100, '/': 90, '+': 80, '-':70}
    #Loop through the input a character at a time.
    for c in infix:
        # print(f"c: {c}\tpostfix: {postfix}\tstack: {stack}")
        # c is a digit
        if c in {'1','2','3','4','5','6','7','8','9', '0' }:
            #Push it to the output
            postfix = postfix + c
        # c is an operator.
        elif c in {'+', '-', '*', '/'}:
            #Check what is on the stack
            while len(stack) > 0 and stack[-1] != '('  and prec[stack[-1]] > prec[c] :
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            #push c to stack,
            stack = stack + c
        elif c == '(':
            #Push c to stack.
            stack = stack + c
        elif c == ')':
            while stack[-1] != "(":
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            # Remove open bracket from stack.
            stack = stack[:-1]
    while len(stack) != 0:
        # Append operator at top of stack to output.
        postfix = postfix + stack[-1]
        # Remove operator from stack.
        stack = stack[:-1]
    #Return the postfix version of infix
    return postfix

# postfix = "3421-*+"
if __name__ == "__main__":
    for infix in ["3+4*(2-1)", "1+2+3+4+5*6", "(1+2)*(4*(6-7))"]:
        print(f"infix:  {infix}")
        print(f"postfix:  {shunt(infix)}")
        print()
        # print(f"postfix: {postfix}")
