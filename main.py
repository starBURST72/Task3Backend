class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None


def check_brackets(text):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for index, char in enumerate(text, 1):
        if char in opening_brackets:
            stack.push((char, index))
        elif char in closing_brackets:
            if stack.is_empty() or bracket_pairs[char] != stack.peek()[0]:
                return index
            else:
                stack.pop()

    if stack.is_empty():
        return "Success"
    else:
        return stack.peek()[1]


def main():
    print("Введите строку")
    text = input().strip()
    if not text:
        print("Пустая строка")
    else:
        result = check_brackets(text)
        print(result)


if __name__ == "__main__":
    main()
