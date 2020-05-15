from double_linked_list import DoublyLinkedList
from double_linked_list import ListNode


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.nextToBeRemoved = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.__len__() < self.capacity:
            self.storage.add_to_tail(item)
            self.nextToBeRemoved = self.storage.head

        else:
            if self.nextToBeRemoved == self.storage.head:
                self.storage.head.value = item
                self.nextToBeRemoved = self.storage.head.next
            
            elif self.nextToBeRemoved == self.storage.tail:
                current_tail = self.storage.tail
                current_tail.value = item
                self.nextToBeRemoved = self.storage.head

            else:
                self.nextToBeRemoved.value = item
                self.nextToBeRemoved = self.nextToBeRemoved.next
                

            

    def get(self):
        current_node = self.storage.head
        values = []
        while True:
            if current_node is None:
                break
            values.append(current_node.value)
            current_node = current_node.next
        return values




    # [a, b, c, d, e]

    # current = a (head)

test = RingBuffer(5)

test.append("a")
test.append("b")
test.append("c")


test.append("d")
test.append("e")
# test.append("f")
# test.append("g")
print(test.get())
# print(test.storage.head.value)
# print(test.storage.head.next.value)
# print(test.storage.head.next.next.value)
# print(test.storage.head.next.next.next.value)
# print(test.storage.tail.value)