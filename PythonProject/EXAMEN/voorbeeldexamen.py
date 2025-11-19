class Node:
    def __init__(self, task_name, duration, priority, next=None):
        self.task_name = task_name
        self.duration = duration
        self.priority = priority
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __add_task(self, task_name, duration, priority):
        new_node = Node(task_name, duration, priority)

        if self.head == None:
            self.head = new_node
            return

        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def remove_task(self, task_name):
        current = self.head
        prev = None

        while current is not None:
            if current.task_name == task_name:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True

            prev = current
            current = current.next

        return False

    def display_tasks(self):
        current = self.head
        while current is not None:
            print(f"{current.task_name} | {current.duration} min | priority {current.priority}")
            current = current.next

    def find_task(self, task_name):
        current = self.head
        while current is not None:
            if current.task_name == task_name:
                return current
            current = current.next
        return None

    def calculate_total_duration(self):
        total_duration = 0
        current = self.head
        while current is not None:
            total += current.duration
            current = current.next
        return total_duration

    def read_tasks_from_csv(self, filepath):
        file = open(filepath, 'r')
        file.readline()
        for line in file:
            name, duration, priority = line.strip().split(',')
            self.add_task(name, int(duration), int(priority))
        file.close()

    # -----------------------------------------------------------
    # SORTING HELPERS
    # -----------------------------------------------------------

    def sorted_insert_by_priority(self, head, node):
        if head is None or node.priority < head.priority:
            node.next = head
            return node

        current = head
        while current.next is not None and current.next.priority <= node.priority:
            current = current.next

        # Insert node
        node.next = current.next
        current.next = node
        return head

    def sorted_insert_by_priority_duration(self, head, node):
        """Insert node sorted by priority, then duration."""
        # Case 1: becomes new head
        if (head is None or node.priority < head.priority or (node.priority == head.priority and node.duration < head.duration)):
            node.next = head
            return node
        # Case 2: find position
        current = head
        while (current.next is not None and
               (current.next.priority < node.priority or
                (current.next.priority == node.priority and
                 current.next.duration <= node.duration))):
            current = current.next

        node.next = current.next
        current.next = node
        return head


    def reorder_tasks_by_priority(self):
        new_head = None
        current = self.head

        while current is not None:
            temp = current.next  # save next node
            current.next = None  # detach node
            new_head = self.sorted_insert_by_priority(new_head, current)
            current = temp

        self.head = new_head

    def reorder_tasks_by_priority_duration(self):
        new_head = None
        current = self.head

        while current is not None:
            temp = current.next
            current.next = None
            new_head = self.sorted_insert_by_priority_duration(new_head, current)
            current = temp

        self.head = new_head

