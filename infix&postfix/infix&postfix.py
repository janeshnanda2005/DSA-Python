def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    output = []
    
    for char in expression:
        if char.isalnum():  # Operand (number or letter)
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop the '('
        else:  # Operator
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

# Example usage
if __name__ == "__main__":
    expression = "a+b^(c^d/e)^(f^g*h)-r"
    print(f"Infix Expression: {expression}")
    print(f"Postfix Expression: {infix_to_postfix(expression)}")
