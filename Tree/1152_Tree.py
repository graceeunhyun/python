import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self):
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)

def find_parents(node):
    for child in node.children:
        if child.parent is None:  # 아직 부모가 설정되지 않은 경우에만 설정
            child.parent = node
            find_parents(child)

n = int(input().strip())
tree = [Node() for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().strip().split())
    tree[a - 1].add_child(tree[b - 1])
    tree[b - 1].add_child(tree[a - 1])

# 루트 노드(1번 노드)의 부모를 None으로 설정하고 시작
root = tree[0]
root.parent = None

# DFS를 통해 부모 찾기
find_parents(root)

# 결과 출력
for i in range(2, n):
    # i + 1 번 노드의 부모는 tree[i].parent가 됨
    print(tree[i].parent.value if tree[i].parent else 0)