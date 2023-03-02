class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return not bool(self.stack)

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


def get_close_bracket(open_bracket):
    brackets_dict = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    return brackets_dict[open_bracket]


def check_brackets(brackets):
    brackets_stack = Stack()
    for bracket in brackets:
        if bracket in ['(', '{', '[']:
            brackets_stack.push(bracket)
        elif brackets_stack.isEmpty():
            return False
        elif bracket == get_close_bracket(brackets_stack.peek()):
            brackets_stack.pop()
        else:
            break
    return brackets_stack.isEmpty()


if __name__ == '__main__':
    my_brackets = '[[{())}]'
    print(check_brackets(my_brackets))

