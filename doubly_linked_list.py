class Node():
    def __init__(self, val):
        self.left = None
        self.value = val
        self.right = None


class doubly_linked_list():
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return not self.head

    def append_left(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.right = node  # point the last node's right to the new node
            node.left = self.tail   # point the new node's left to the last node
            self.tail = node        # set the new node as the tail

    def append_right(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.head.left = node   # point the first node's left to the new node
            node.right = self.head  # point the new node's right to the first node
            self.head = node        # set the new node as the tail

    def pop_right(self):
        if self.is_empty():
            raise IndexError('list is empty, nothing to pop')

        value = self.tail.value

        if self.head == self.tail:  # if has just one element in the list
            self.head = self.tail = None
        else:
            self.tail = self.tail.left
            self.tail.right = None

        return value

    def pop_left(self):
        if self.is_empty():
            raise IndentationError('nothing to pop')

        value = self.head.value

        if self.head == self.tail:  # if has just one element in the list
            self.head = self.tail = None
        else:
            self.head = self.head.right
            self.head.left = None

        return value

    def __str__(self):
        curr = self.head
        res = []

        while curr:
            res.append(curr.value)
            curr = curr.right

        return str(res)


if __name__ == '__main__':
    dll = doubly_linked_list()
    print(dll.pop_left())
