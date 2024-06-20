class BinaryTree:
    class Node:
        def __init__(self, key: str = None, value: any = None):
            self._left = None
            self._right = None
            self.key = key
            self.value = value

    def __init__(self, root_key: str = None, root_value: any = None):
        self.root = BinaryTree.Node(root_key, root_value) if root_key is not None else None
        self._size = 0 if self.root is None else 1
        self.key_type = type(root_key) if root_key is not None else None

    def __len__(self) -> int:
        return self._size

    def __setitem__(self, key: str, value: any) -> None:
        if self.key_type and not isinstance(key, self.key_type):
            raise KeyError(f"All keys must be of type {self.key_type.__name__}")

        if not self.root:
            self.key_type = type(key)
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
        raise KeyError(f"{key} not in dict")

    def _min(self, node):
        current = node
        while current and current._left is not None:
            current = current._left
        return current

    def _remove(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node._left = self._remove(node._left, key)
        elif key > node.key:
            node._right = self._remove(node._right, key)
        else:
            if node._left is None or node._right is None:
                return node._left if node._left else node._right
            else:
                temp = self._min(node._right)
                node.key = temp.key
                node.value = temp.value
                node._right = self._remove(node._right, temp.key)

        return node

    def pop(self, key):
        self.root = self._remove(self.root, key)
        self._size -= 1
