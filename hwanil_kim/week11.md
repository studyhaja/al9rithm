### Q 44. 
#### 문제: 트리 순회 구현(in-order방식)

in-order방식은 아래와 같다. 
- 왼쪽 부분 트리를 in-order 순회한다
- 현재 노드의 데이터를 출력한다
- 오른쪽 부분 트리를 in-order 순회한다
![스크린샷 2021-05-05 오후 8 47 35](https://user-images.githubusercontent.com/70195733/117136319-3008da00-ade3-11eb-931d-a4e84c69826a.png)
- 위 트리를 in-order로 순회하면 A, B, C, D, E, F, G, H, I 순서로 출력된다.

#### 주어진 코드
```
class Node:
    """이진 트리 노드를 나타내는 클래스"""

    def __init__(self, data):
        """이진 트리 노드는 데이터와 두 자식 노드에 대한 레퍼런스를 갖는다"""
        self.data = data
        self.left_child = None
        self.right_child = None

def traverse_inorder(node):
    """in-order 순회 함수"""
    #코드를 작성하세요

# 여러 노드 인스턴스 생성
node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")
node_I = Node("I")

# 생성한 노드 인스턴스들 연결
node_F.left_child = node_B
node_F.right_child = node_G

node_B.left_child = node_A
node_B.right_child = node_D

node_D.left_child = node_C
node_D.right_child = node_E

node_G.right_child = node_I

node_I.left_child = node_H

# 노드 F를 root 노드로 만든다
root_node = node_F

# 만들어 놓은 트리를 in-order로 순회한다
traverse_inorder(root_node)
```
#### my solution
```
def traverse_inorder(node):
    """in-order 순회 함수"""
    if not node.left_child and not node.right_child:
        print(node.data)
    else:
        if not node.left_child and node.right_child:
            print(node.data)
        if node.left_child:
            traverse_inorder(node.left_child)
            print(node.data)
        if node.right_child:
            traverse_inorder(node.right_child)
```
- 코드잇 정답 코드
```
def traverse_inorder(node):
    """in-order 순회 함수"""
    if node is not None:
        traverse_inorder(node.left_child)  # 재귀적으로 왼쪽 부분 트리 순회
        print(node.data)  # 데이터 출력
        traverse_inorder(node.right_child)  # 재귀적으로 오른쪽 부분 트리 순회
```
-비루한 나의 코드......

