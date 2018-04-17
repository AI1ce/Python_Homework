from typing import Iterable


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, values: Iterable):
        previous = None
        self.head = None
        for value in values:
            current = LinkedListNode(value)
            if previous:
                previous.next = current
            self.head = self.head or current
            previous = current

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


    def reverse(self):
        current = self.head
        heads = None
        while current.next:
            currents = self.head
            while currents.next:
                previous = currents
                currents = currents.next
            if not (heads):
                heads = currents
            previous.next = None
            currents.next = previous
        self.head = heads
        return self


    @property
    def output(self):
        for evrthng in self:
            print(evrthng)


linked_list = LinkedList([1, 2, 3])
linked_list.output
print('='*3)
linked_list.reverse().output