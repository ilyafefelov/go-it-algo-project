class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    A class representing a singly linked list.
    Methods:
    - append(value): Adds a new node with the given value to the end of the linked list.
    - reverse(): Reverses the order of the nodes in the linked list.
    - to_list(): Converts the linked list to a Python list.
    - merge_sort(): Sorts the linked list using the merge sort algorithm.
    - merge_two_sorted_lists(l1, l2): Merges two sorted linked lists into a single sorted linked list.
    """
    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.head = None

    def append(self, value):
        """
        Appends a new node with the given value to the end of the linked list.

        Parameters:
        - value: The value to be added to the linked list.

        Returns:
        None
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverse(self):
        """
        Reverses the order of the linked list.

        This method iterates through the linked list and reverses the order of the nodes.
        It updates the `next` pointers of each node to reverse the connections.

        Returns:
            None

        Complexity:
            - Time Complexity: O(n), where n is the number of nodes in the linked list.
            - Space Complexity: O(1)
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def to_list(self):
        """
        Converts the linked list into a Python list.

        Returns:
            list: A Python list containing the values of the linked list.
        """
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
    
    def merge_sort(self):
        """
        Sorts the linked list in ascending order using the merge sort algorithm.
        Returns:
            Node: The head of the sorted linked list.
        Raises:
            None.
        """
        if self.head is None or self.head.next is None:
            return self.head
        middle = self.get_middle(self.head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort_util(self.head)
        right = self.merge_sort_util(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        self.head = sorted_list

    def merge_sort_util(self, h):
        """
        Sorts a singly linked list using the merge sort algorithm.
        Parameters:
        - h: The head node of the linked list to be sorted.
        Returns:
        - sorted_list: The head node of the sorted linked list.
        """
        # Implementation details...
        if h is None or h.next is None:
            return h
        middle = self.get_middle(h)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort_util(h)
        right = self.merge_sort_util(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def get_middle(self, head):
        """
        Returns the middle node of a singly linked list.

        Parameters:
        - head: The head node of the linked list.

        Returns:
        - The middle node of the linked list.

        Example:
        >>> linked_list = LinkedList()
        >>> linked_list.add_node(1)
        >>> linked_list.add_node(2)
        >>> linked_list.add_node(3)
        >>> linked_list.add_node(4)
        >>> linked_list.add_node(5)
        >>> linked_list.get_middle(linked_list.head).data
        3
        """
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, a, b):
        """
        Merges two sorted linked lists into a single sorted linked list.
        Parameters:
        a (Node): The head of the first sorted linked list.
        b (Node): The head of the second sorted linked list.
        Returns:
        Node: The head of the merged sorted linked list.
        """
        result = None
        if a is None:
            return b
        if b is None:
            return a

        if a.value <= b.value:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result
    
    @staticmethod
    def merge_two_sorted_lists(l1, l2):
        """
        Merge two sorted linked lists.
        Parameters:
        - l1 (Node): The head of the first linked list.
        - l2 (Node): The head of the second linked list.
        Returns:
        - Node: The head of the merged linked list.
        """
        dummy = Node(0)
        tail = dummy

        while l1 and l2:
            if l1.value < l2.value:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next

    def print_list(self):
        """
        Utility method to print the linked list.
        Prints the values of the linked list in order.

        Returns:
            None
        """
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Test:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(7)
linked_list.append(4)

print("Original list:")
linked_list.print_list()

linked_list.reverse()
print("Reversed list:")
linked_list.print_list()

print("Unsorted list:")
linked_list.print_list()

linked_list.merge_sort()
print("Sorted list:")
linked_list.print_list()

list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(8)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)
list2.append(19)

merged_head = LinkedList.merge_two_sorted_lists(list1.head, list2.head)
merged_list = LinkedList()
merged_list.head = merged_head

print("\nMerging lists:")
list1.print_list()
list2.print_list()
print("Merged list:")
merged_list.print_list()
