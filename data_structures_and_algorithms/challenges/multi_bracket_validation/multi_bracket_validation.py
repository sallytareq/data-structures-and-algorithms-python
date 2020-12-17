import re
from data_structures_and_algorithms.challenges.stacks_and_queues.stacks_and_queues import Stack , Queue

# def multi_bracket_validation(in_str):
#     if type(in_str) != str:
#         return "Invalid Input"

#     opening_s = len([*re.findall(r'[\[]' , in_str)])
#     closing_s = len([*re.findall(r'[\]]' , in_str)])
#     opening_p = len([*re.findall(r'[\(]' , in_str)])
#     closing_p = len([*re.findall(r'[\)]' , in_str)])
#     opening_c = len([*re.findall(r'[\{]' , in_str)])
#     closing_c = len([*re.findall(r'[\}]' , in_str)])
    
#     if opening_s == closing_s and opening_p == closing_p and opening_c == closing_c :
#         return True
#     else:
#         return False
    
def multi_bracket_validation(in_str):

    if type(in_str) != str:
        return "Invalid Input"

    checker = Stack()
    st = [*re.findall(r'[\[\]\(\)\{\}]' , in_str)]
    opening = ["[","(","{"]
    closing = ["]",")","}"] 

    for x in st:
        y = ""
        if x in opening:
            index = opening.index(x)
            y = closing[index]
        elif x in closing:
            index = closing.index(x)
            y = opening[index]

        if checker.top == None:
            checker.push(x)
        elif y == checker.top.value:
            checker.pop()
        else:
            checker.push(x)
    
    current = checker.top

    while current != None:
        print("X = " , current.value)
        current = current.next
    
    if checker.top == None:
        return True
    else:
        return False 

s = 1
x = multi_bracket_validation(s)
print(x)

