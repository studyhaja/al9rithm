number_of_case = int(input())
for i in range(number_of_case):
    l_stack = []
    r_stack = []
    case = input()
    for chr in case:
        if chr == '<':
            if l_stack:
                poped_data = l_stack.pop()
                r_stack.append(poped_data)
        elif chr == '>':
            if r_stack:
                poped_data = r_stack.pop()
                l_stack.append(poped_data)
        elif chr == '-':
            if l_stack:
                l_stack.pop()
        else:
            l_stack.append(chr)
    l_stack.extend(reversed(r_stack))
    print(''.join(l_stack))

# asdf
# asd    f
# as   fd
#
# def func():
#     number_of_case = int(input())
#     for i in range(number_of_case):
#         l_stack = []
#         r_queue = []
#         case = list(map(str, input()))
#         for chr in case:
#             if chr.isalpha() or chr.isnum():
#                 l_stack.append(chr)
#             else:
#                 if not l_stack:
#                     continue
#                 else:
#                     if chr == '<':
#                         poped_data = l_stack.pop()
#                         r_queue.append(poped_data)
#                     elif chr == '>':
#                         if r_queue:
#                             poped_data = r_queue.pop(0)
#                             l_stack.append(poped_data)
#                     elif chr == '-':
#                         l_stack.pop()
#         res = l_stack + r_queue
#         print(''.join(res))
#
#
#
# if __name__ == "__main__":
#     func()