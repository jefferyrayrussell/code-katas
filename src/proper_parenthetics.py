# -*- coding: utf-8 -*-


from stack import Stack


def parenthetics(parentheses_string):
    """Check for valid parenthetics."""
    parentheses_stack = Stack()
    for item in parentheses_string:
        if item == '(':
            parentheses_stack.push(item)
        elif item == ')':
            try:
                parentheses_stack.pop()
            except IndexError:
                return -1
        if len(parentheses_stack) == 0:
            return 0
        else:
            return 1
