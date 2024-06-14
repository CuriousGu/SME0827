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
        if BinaryTree.KeyType().TYPE and type(key) != BinaryTree.KeyType().TYPE:
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
                    self.__size += 1
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

    # def remove(self, key) -> None:
    #     if self._size > 0 and type(key) != BinaryTree.KeyType().TYPE:
    #         raise KeyError(f"All keys must follow the same type - this tree uses {BinaryTree.KeyType().TYPE}")

    #     def find_min(node: BinaryTree.Node) -> BinaryTree.Node:
    #         curr = node
    #         while curr._left:
    #             curr = curr._left
    #         return curr
        
    #     def remove_node(node: BinaryTree.Node, key) -> BinaryTree.Node:
    #         if not node:
    #             raise ValueError("Item not found")
    #         if key < node.key:
    #             node._left = remove_node(node._left, key)
    #         elif

    #     def remove_node(node, key):
    #         if node is None:
    #             raise ValueError("Item not found in the tree")
    #         if key < node.key:
    #             node._left = remove_node(node._left, key)
    #         elif key > node.key:
    #             node._right = remove_node(node._right, key)
    #         else:
    #             if node._left is None:
    #                 return node._right
    #             elif node._right is None:
    #                 return node._left

    #             temp = find_min(node._right)
    #             node.key = temp.key
    #             node.value = temp.value
    #             node._right = remove_node(node._right, temp.key)
    #         return node

    #     if self.root is None:
    #         raise ValueError("Empty Tree")
    #     self.root = remove_node(self.root, key)
    #     self.__size = self.__size - 1 if self.__size > 0 else 0
