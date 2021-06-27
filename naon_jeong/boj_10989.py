'''
백준 온라인 저지 - 수 정렬하기 3

https://www.acmicpc.net/problem/10989

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
'''


'''
단순하게 생각해서 숫자 개수만큼 반복문을 돌려서 입력 받고, 리스트에 저장하고 정렬한 뒤 다시 반복문으로 출력하려 했다.
돌려보면 답이 나오기는 하지만 메모리 초과...
'''

cnt = int(input())
nums = []
for i in range(cnt):
    num = int(input())
    nums.append(num)

nums.sort()
for num in nums:
    print(num)

'''
계수정렬(counting sort)라는 방식을 사용했다.
입력받는 숫자는 최대 10000이니 인덱스가 10000까지 있는, 0으로만 이루어진 리스트를 생성한다.
입력받는 숫자를 인덱스로 사용해, 인덱스에 해당하는 숫자에 1을 더해준다. 리스트의 숫자가 0이 아닌 것은 해당 인덱스(=입력받은 숫자)가 나오지 않았다는 뜻이다.
따라서 반복문을 돌리면서 0인 것을 제외하고, 리스트에 저장된 숫자만큼 반복하며 인덱스 번호를 출력한다.  
'''

import sys

num_cnt = int(input())
num_list = [0 for _ in range(10001)]

for _ in range(num_cnt):
    num = int(sys.stdin.readline())
    num_list[num] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
