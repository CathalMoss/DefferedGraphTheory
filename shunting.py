# Adapted from pseudocode at:
# https://en.wikipedia.org/wiki/Shunting-yard_algorithm

def shunt(infix):
    """Convert infix expressions to postfix."""
    #The eventual output.
    postfix = ""
    #the shunting yard operator stack.
    stack = ""
    #operator precedence
    prec = {'*': 100, '/': 90, '+': 80, '-': 70}
    #Loop through the input a character at a time.
    for c in infix:
        # c is a digit
        if c in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            #Push it to the output
            postfix = postfix + c

        # c is an operator.
        else if c in {'+', '-', '*', '/'}:
        #Check what is on the stack
        while len(stack) > 0 and prec[stack[-1]] > prec(c) and stack[-1] != '(':
            # Append operator at top of stack to output.
            postfox = postfix + stack[-1]
            # Remove operator from stack.
            stack = stack[:-1]
            #push c to stack,
            stack = stack + c
         
            while (
                there is an operator o2 other than the left parenthesis at the top
                of the operator stack, and (o2 has greater precedence than o1
                or they have the same precedence and o1 is left-associative)
            ):
                pop o2 from the operator stack into the output queue
            push o1 onto the operator stack
        - a left parenthesis (i.e. "("):
            push it onto the operator stack
        - a right parenthesis (i.e. ")"):
            
            
            while the operator at the top of the operator stack is not a left parenthesis:
                {assert the operator stack is not empty}
                /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */
                pop the operator from the operator stack into the output queue
            {assert there is a left parenthesis at the top of the operator stack}
            pop the left parenthesis from the operator stack and discard it
            if there is a function token at the top of the operator stack, then:
                pop the function from the operator stack into the output queue
    /* After the while loop, pop the remaining items from the operator stack into the output queue. */
    while there are tokens on the operator stack:
        /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
        {assert the operator on top of the stack is not a (left) parenthesis}
        pop the operator from the operator stack onto the output queue
    return postfix



    infix = "3+4*(2-1)"
    postfix = "3421-*+"

    if shunt(infix) == postfix:
        print("It seems to work.")