# 이진 검색 트리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(50000)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root
    
    # 삽입
    def insert(self, node):
        self.current_node = self.root
        while True:
            if node.data < self.current_node.data:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(node.data)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(node.data)
                    break

        # if node.data < self.root.data:
        #     self.root.left = self.insert(node)
        # elif node.data > self.root.data:
        #     self.root.right = self.insert(node)
        

    # 후위 순위 탐색
    def post_order(self, root:Node):
        if not root:
            return []
        
        self.nodes = []

        def travel(node):
            if not node:
                return []
            
            travel(node.left)
            travel(node.right)
            self.nodes.append(node.data)

        travel(root)

        return self.nodes

node_list = []

try:
    while True:
        data = input()
        # if type(data) is not int:
        #     exit(0)
        node_list.append(Node(int(data)))

except:
    tree = BST(node_list[0])

    for i in range(1, len(node_list)):
        tree.insert(node_list[i])

    post_order_list = tree.post_order(node_list[0])

    for i in post_order_list:
        print(i)