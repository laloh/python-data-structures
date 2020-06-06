"""
Algorithm:
    1. Reduce the original number to a series of single-digit numbers.
    2. Convert the single digit-number to a string using lookup.
    3. Concatenate the single-digit strings together to form the final result.
"""

from stacks.stack import Stack

def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    print(convert_string[int(n % base)])
    print("n: ", n, "base: ", base)
    if n < base:
        return convert_string[int(n)]
    else:
        return to_str(n / base, base) + convert_string[int(n % base)]

r_stack = Stack()


def to_str_with_stack(n, base):
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n % base])
        n = n // base
    res = ""
    while not r_stack.is_empty():
        res = res + str(r_stack.pop())
    return res

print(to_str(10, 2))
print(to_str_with_stack(10, 2))

