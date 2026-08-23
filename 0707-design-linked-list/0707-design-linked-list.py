class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head= None

    def get(self, index: int) -> int:
        temp = self.head
        count = 0

        while temp:
            if count == index:
                return temp.val

            count += 1
            temp = temp.next

        return -1
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node 

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        else:
            curr = self.head
            prev_node = None
            count = 0
            while curr is not None and count < index:
                prev_node = curr
                curr = curr.next
                count += 1  
        if count != index:
            return

        newNode = Node(val)

        newNode.next = curr
        prev_node.next = newNode         

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        count = 0

        while temp.next and count < index - 1:
            temp = temp.next
            count += 1

        if temp.next is None:
            return

        temp.next = temp.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)