# BinaryTree class
class BinaryTree:
    # コンストラクタ、インスタンスが作成されるときに実行
    def __init__(self, data):
        # ノード保持するデータ
        self.data = data
        # ノード左、初期値None
        self.left = None
        # ノード右、初期値None
        self.right = None


# 二分木ノード作成、データとして1を保持
binaryTree = BinaryTree(1)
# 2つのノード作成
node2 = BinaryTree(2)
node3 = BinaryTree(3)

# 根ノードの左node2、右node3
binaryTree.left = node2
binaryTree.right = node3

# 根ノードと左右ノードを表示
# 根ノード表示
print("Root: " + str(binaryTree.data))
# 左ノード表示
print("Left: " + str(binaryTree.left.data))
# 右ノード表示
print("Right: " + str(binaryTree.right.data))
