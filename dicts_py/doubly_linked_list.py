"""
PRECISO REVISAR
"""

class DoublyLinkedList:

    class Node:
        def __init__(self, key: any, value: any = None) -> None:
            self.next = None
            self.previous = None
            self.key = key
            self.value = value

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __setitem__(self, key: any, value: any) -> None:
        new_node = DoublyLinkedList.Node(key, value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            pointer = self.head
            while pointer:
                if pointer.key == key:
                    pointer.value = value
                    return
                if not pointer.next:
                    break
                pointer = pointer.next
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self._size += 1

    def __getitem__(self, key: any) -> any:
        pointer = self.head
        while pointer:
            if pointer.key == key:
                return pointer.value
            pointer = pointer.next
        raise KeyError(f"Key {key} not found in the list")

    def insert(self, index: int, key: any, value: any) -> None:
        if index > self._size or index < 0:
            raise IndexError("list index out of range")
        pointer = self.head
        while index > 0:
            pointer = pointer.next
            index -= 1
        new_node = DoublyLinkedList.Node(key, value)
        new_node.next, new_node.previous = pointer, pointer.previous
        if pointer.previous:
            pointer.previous.next = new_node
        pointer.previous = new_node
        if pointer == self.head:
            self.head = new_node
        self._size += 1

    def append(self, key: any, value: any) -> None:
        new_node = DoublyLinkedList.Node(key, value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self._size += 1

    def pop(self, index: int = None) -> any:
        if self._size == 0:
            raise IndexError("pop from empty list")

        if index is None:
            item = self.tail.key
            if self.tail.previous:
                self.tail = self.tail.previous
                self.tail.next = None
            else:
                self.head = self.tail = None
        else:
            if index < 0 or index >= self._size:
                raise IndexError("list index out of range")
            pointer = self.head
            while index > 0:
                pointer = pointer.next
                index -= 1
            item = pointer.key
            if pointer.previous:
                pointer.previous.next = pointer.next
            if pointer.next:
                pointer.next.previous = pointer.previous
            if pointer == self.head:
                self.head = pointer.next
            if pointer == self.tail:
                self.tail = pointer.previous
        self._size -= 1
        return item

    def index(self, key: any) -> int:
        pointer = self.head
        index = 0
        while pointer and pointer.key != key:
            pointer = pointer.next
            index += 1
        if pointer and pointer.key == key:
            return index
        else:
            raise ValueError(f"{key} not in the list")

    def remove(self, index: int) -> None:
        if index >= self._size or index < 0:
            raise IndexError("list index out of range")
        pointer = self.head
        while index > 0:
            pointer = pointer.next
            index -= 1
        if pointer.previous:
            pointer.previous.next = pointer.next
        if pointer.next:
            pointer.next.previous = pointer.previous
        if pointer == self.head:
            self.head = pointer.next
        if pointer == self.tail:
            self.tail = pointer.previous
        self._size -= 1
