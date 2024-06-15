class BinaryTree:

    class Node:
        def __init__(self, key: str = None, value: any = None):
            self._left = None
            self._right = None
            self.key = key
            self.value = value

    class KeyType:
        TYPE = None

    def __init__(self, root_key: str = None, root_value: any = None):
        '''
        root_key = tree's root key. If NULL, tree will be created empty
        root_value = value associated with the root key
        '''
        self.root = BinaryTree.Node(root_key, root_value) if root_key is not None else None
        self._size = 0 if self.root is None else 1

    def __len__(self) -> int:
        return self._size

    def __setitem__(self, key: str, value: any) -> None:
        # Todas as chaves devem ter o mesmo tipo, possibilitando a ordenação
        if BinaryTree.KeyType().TYPE and type(key) is not BinaryTree.KeyType().TYPE:
            raise KeyError(f"All keys must follow the same type - this tree uses {BinaryTree.KeyType().TYPE}")

        if not self.root:
            # definindo o tipo das keys na criação da árvore
            BinaryTree.KeyType().TYPE = type(key)
            self.root = BinaryTree.Node(key, value)
            self._size += 1
            return

        pointer = self.root
        while pointer:
            if key < pointer.key:
                if pointer._left:
                    pointer = pointer._left
                else:
                    pointer._left = BinaryTree.Node(key, value)
                    self._size += 1
                    break
            elif key > pointer.key:
                if pointer._right:
                    pointer = pointer._right
                else:
                    pointer._right = BinaryTree.Node(key, value)
                    self._size += 1
                    break
            else:
                pointer.value = value
                break

    def __getitem__(self, key: str) -> any:
        pointer = self.root
        while pointer:
            if key > pointer.key:
                pointer = pointer._right
            elif key < pointer.key:
                pointer = pointer._left
            else:
                return pointer.value
        raise ValueError(f"{key} not in dict")

    def min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _remove(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._min(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._remove(node.right, temp.key)

        return node

    def remove(self, key):
        self.root = self._remove(self.root, key)
