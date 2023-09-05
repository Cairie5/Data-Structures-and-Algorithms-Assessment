def is_balanced(brackets):
    stack = []  # Create an empty stack to store open brackets
    open_brackets = "([{"
    close_brackets = []

    for b in brackets:
        if b in open_brackets:  # If the current character is an open bracket
            stack.append(b)  # Push it onto the stack
            print(stack)
        if b not in open_brackets:  # If the current character is not an open bracket
            close_brackets.append(b)  # Add it to the close_brackets list
            if len(stack) > 0:  # Check if the stack is not empty
                if (
                    stack[-1] == "("
                    and b == ")"
                    or stack[-1] == "["
                    and b == "]"
                    or stack[-1] == "{"
                    and b == "}"
                ):
                    # If the current character matches the corresponding open bracket
                    popped = stack.pop()  # Pop the last open bracket from the stack
                    close_brackets.pop()  # Remove the corresponding close bracket from the list
                else:
                    return False  # If there's a mismatch, return False

    # Check if both the stack and close_brackets list are empty to ensure balance
    return True if len(stack) == 0 and len(close_brackets) == 0 else False


s = "([]{})"
print(is_balanced(s))

