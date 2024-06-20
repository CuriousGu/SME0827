class DoublyLinked:
    class Node:
        def __init__(self, key: any, value: any = None) -> None:
            self.next = None
            self.prev = None
            self.key = key
            self.value = value

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __setitem__(self, key: any, value: any) -> None:
        if not self.head:
            self.head = self.tail = self.Node(key, value)
        else:
            current = self.head
            while current:
                if current.key == key:
                    current.value = value
                    return
                if not current.next:
                    break
                current = current.next

            new_node = self.Node(key, value)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1

    def __getitem__(self, key: any) -> any:
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Key {key} not found in the list")

    def __delitem__(self, key: any) -> None:
        current = self.head
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                self._size -= 1
                return
            current = current.next
        raise KeyError(f"Key {key} not found in the list")

    def append(self, key: any, value: any) -> None:
        new_node = self.Node(key, value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1

    def pop(self, key: any = None) -> any:
        if self._size == 0:
            raise IndexError("pop from empty list")
        if key is None:  # pop last item
            item = self.tail
            self.__delitem__(item.key)
            return item.key, item.value
        else:
            item = self.head
            while item:
                if item.key == key:
                    self.__delitem__(item.key)
                    return item.key, item.value
                item = item.next
            raise KeyError(f"Key {key} not found in the list")

    def clear(self) -> None:
        self.head = self.tail = None
        self._size = 0

    def keys(self):
        keys = []
        current = self.head
        while current:
            keys.append(current.key)
            current = current.next
        return keys

    def values(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values
