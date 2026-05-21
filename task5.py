def check_balanced_brackets(expression):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    for ch in expression:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack:
                return False
            top = stack.pop()
            if matching[ch] != top:
                return False
    return not stack   # True if stack is empty