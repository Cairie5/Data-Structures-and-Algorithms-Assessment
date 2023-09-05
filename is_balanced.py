def is_balanced(brackets):
    stack = []
    open_brackets = "([{"
    close_brackets = []

    for b in brackets:
        if b in open_brackets:
            stack.append(b)
            print(stack)
        if b not in open_brackets:
            # check if stack is empty
            close_brackets.append(b)
            if len(stack) > 0:
                if (
                    stack[-1] == "("
                    and b == ")"
                    or stack[-1] == "["
                    and b == "]"
                    or stack[-1] == "{"
                    and b == "}"
                ):
                    poped = stack.pop()
                    close_brackets.pop()
                else:
                    return False

    return True if len(stack) == 0 and len(close_brackets) == 0 else False


s = "([]{})"
print(is_balanced(s))
