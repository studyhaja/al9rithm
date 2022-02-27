# def solution(record):
#     answer = []
#     uid_name_dict = dict()
#     for row in record:
#         split_row = row.split(' ')
#         if len(split_row) > 2:
#             uid = split_row[1]
#             name = split_row[2]
#             uid_name_dict[uid] = name
#     for row in record:
#         split_row = row.split(' ')
#         status = split_row[0]
#         uid = split_row[1]
#         if status == "Enter":
#             res = f"{uid_name_dict[uid]}님이 들어왔습니다."
#             answer.append(res)
#         elif status == "Leave":
#             res = f"{uid_name_dict[uid]}님이 나갔습니다."
#             answer.append(res)
#     return answer


# test_case = int(input())
# for _ in range(test_case):
#     parent = dict()
#     number = dict()
#
#     f = int(input())
#
#     for _ in range(f):
#         x, y = input.split(' ')
#         if x not in parent:
#             parent[x] = x
#             number[x] = 1
#         if y not in parent:
#             parent[y] = y
#             number[y] = 1
#
#         union
#
