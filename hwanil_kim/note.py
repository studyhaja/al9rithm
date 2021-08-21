first_input = int(input())
num1 = set(list(map(int, input().split(' '))))

second_input = int(input())
num2 = list(map(int, input().split(' ')))
for i in num2:
    if i in num1:
        print(1)
    else:
        print(0)



# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5)