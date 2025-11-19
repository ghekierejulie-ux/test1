from wsgiref.validate import header_re


class Node:
    def __init__(self, task_name, duration, priority, next= None):
        self.task_name = task_name
        self.duration = duration
        self.priority = priority
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def add_task(self, task_name, duration, priority):
        new_node = Node(task_name, duration, priority)

        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node



    def remove_task(self, task_name):
        current = self.head
        prev = None
        while current is not None and current.task_name != task_name:
            prev = current
            current = current.next
        if current is None:
            return False
        # verwijderen van head
        if prev is None:
            self.head = current.next
            return True
        prev.next = current.next
        return True

    def display_tasks(self):
        current = self.head
        while current is not None:
            print(f"{current.task_name}- {current.priority} - {current.duration}")
            current = current.next
        return True

    def find_task(self, task_name):
        current = self.head
        while current is not None and current.task_name != task_name:
            current = current.next
        if current is None:
            return None
        return current

    def calculate_total_duration(self):
        total_duration = 0
        current = self.head
        while current is not None:
            total_duration += current.duration
            current = current.next
        return total_duration

    def read_tasks_from_csv(self, filepath):
        file = open(filepath, 'r')
        file.readline()
        task_name, duration, priority = file.readline().strip().split(',')

    def sorted_insert_by_priority(self, head, node):
        if head is None or node.duration < head.duration:
            node.next = head
            return node

        current = head
        while current.next is not None and current.next.duration <= node.duration:
            current = current.next


        node.next = current.next
        current.next = node
        return head
    def sorted_insert_by_priority(self, head, node):
        if (head is None or node.priority < head.priority or (node.priority == head.priority and node.duration < head.duration)):
            node.next = head
            return node

        current = head
        while (current.next is not None and (current.next.priority < node.priority or (current.next.priority == node.priority and current.next.duration < node.duration))):
            current = current.next

        node.next = current.next
        current.next = node
        return head

    def reorder_tasks_by_priority(self):
        new_head = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = None
            new_head = self.sorted_insert_by_priority(new_head, current)
            current = next_node
        self.head = new_head

    def reorder_tasks_by_priority_duration(self):
        new_head = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next= None
            new_head = self.sorted_insert_by_priority_duration(new_head, current)
            current = next_node #ga naar de volgende node in de oorspronkelijke lijst, anders zou je steeds dezelfde node blijven verwerken


        self.head = new_head




