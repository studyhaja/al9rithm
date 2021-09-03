'''
HackerRank Python Practice - List Comprehensions

https://www.hackerrank.com/challenges/list-comprehensions/problem

You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n.
Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j+ k is not equal to n.

Here, 0 ≤ i ≤ x; 0 ≤ j ≤ y; 0 ≤ k ≤ z.
Please use list comprehensions rather than multiple loops, as a learning exercise.
'''


'''
list comprehension을 사용해 각각 다른 range를 가진 요소로 nested list를 어떻게 만들 수 있을지 고민했다.
x, y, z 각 범위 내에 해당하는 요소를 별도 리스트로 만든 후에 다시 반복문을 돌려서 nested list를 만들기...는 아무리 생각해도 아닌 방법.

https://stackoverflow.com/questions/18072759/list-comprehension-on-a-nested-list
여기 세 번째 답변을 참고했다.
중첩 반복문을 list comprehension으로 쓰는 방식을 원래 모르고 있었는지 잊어버린 건지... 아무튼 기억하자
'''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

combinations = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
result = [a for a in combinations if sum(a) is not n]
print(result)
