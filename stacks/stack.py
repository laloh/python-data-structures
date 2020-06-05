class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)



# Write a function rev_string(my_str) that uses a stack to reverse
# the characters in a string
def rev_string(my_str):
    stack = Stack()
    inv_str2 = ''
    for c in my_str:
        print(c)
        stack.push(c)

    while not stack.is_empty():
        inv_str2+=stack.pop()
    return inv_str2

# s = Stack()
# print(s.is_empty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.is_empty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())
#
# # Exercise Above
#
# string = "eduardo"
# stack_2 = Stack()
# stack_2.push(string)
# print(rev_string(string))
#
