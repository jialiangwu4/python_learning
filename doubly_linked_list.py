
class doubly_linked_list():
    class Node():
        def __init__(self, val):
            self.left = None
            self.value = val
            self.right = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def is_empty(self):
        return not self.head

    def append_left(self, val):
        node = self.Node(val)
        self.len += 1
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.head.left = node   # point the first node's left to the new node
            node.right = self.head  # point the new node's right to the first node
            self.head = node        # set the new node as the head

    def append_right(self, val):
        node = self.Node(val)
        self.len += 1
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.right = node  # point the last node's right to the new node
            node.left = self.tail   # point the new node's left to the last node
            self.tail = node        # set the new node as the tail

    def pop_right(self):
        if self.is_empty():
            raise IndexError('list is empty, nothing to pop')

        value = self.tail.value
        self.len -= 1

        if self.head == self.tail:  # if has just one element in the list
            self.head = self.tail = None
        else:
            self.tail = self.tail.left
            self.tail.right = None

        return value

    def pop_left(self):
        if self.is_empty():
            raise IndexError('nothing to pop')

        value = self.head.value
        self.len -= 1

        if self.head == self.tail:  # if has just one element in the list
            self.head = self.tail = None
        else:
            self.head = self.head.right
            self.head.left = None

        return value

    def get_index_at(self, idx):
        if self.is_empty():
            raise IndexError('empty list')

        if idx >= 0:
            i = 0
            curr = self.head
            while i != idx and curr:
                curr = curr.right
                i = i + 1
        else:
            i = -1
            curr = self.tail
            while i != idx and curr:
                curr = curr.left
                i = i - 1

        if curr:
            return curr.value
        else:
            raise IndexError('index out of range')

    def lenth(self):
        return self.len

    def __str__(self):
        curr = self.head
        res = []

        while curr:
            res.append(curr.value)
            curr = curr.right

        return str(res)


if __name__ == '__main__':
    dll = doubly_linked_list()
    print(dll.is_empty())
    dll.append_left(1)
    dll.append_left(2)
    dll.append_left(3)
    dll.append_left(4)
    dll.append_left(5)

    dll.append_right(6)
    dll.append_right(7)
    dll.append_right(8)
    dll.append_right(9)

    print(dll)
    print(dll.lenth())
    print('get index at -5: ', dll.get_index_at(-5))
    print('pop left: ', dll.pop_left())
    print(dll)
    print('get index at 2: ', dll.get_index_at(2))
    print(dll)
    print('get index at -2: ', dll.get_index_at(-2))
    print('pop right: ', dll.pop_right())
    print(dll)
    print(dll.lenth())
    print(dll.is_empty())
