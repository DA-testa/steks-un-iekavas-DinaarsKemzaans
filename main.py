#Dinārs Kemzāns 221RDB321 17. grupa
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i+1
            if not are_matching((opening_brackets_stack.pop()).char, next):
                return i+1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"
def main():
    text = input()
    if "I" in text:
        text = input()
        mismatch = find_mismatch(text)
        # Printing answer, write your code here
        print(mismatch)
    else:
        pass
    

main()
