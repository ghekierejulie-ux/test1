class Node:
    def __init__(self, task_name, duration, priority, next = None): #next hoort bijna altijd None te zijn wanneer je een nieuwe Node maakt, tenzij je de Node meteen wil verbinden.
        self.task_name = task_name
        self.duration = duration
        self.priority = priority
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def add_task(self, task_name, duration, priority):
        new_node = Node(task_name, duration, priority)

        if self.head == None:
            self.head = new_node
            return

        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    def remove_task(self, task_name):
        current = self.head
        prev = None
        while current is not None and current.task_name != task_name:
            prev = current
            current = current.next

        if current is None:
            return
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
    def display_tasks(self):
        current = self.head
        while current is not None:
            print(f"{current.task_name} - {current.duration} min - priority {current.priority}")
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
            total_duration += current.duration
            current = current.next
        return total_duration

    def read_task_from_csv(self, file_path):
        file = open(file_path, 'r')
        file.readline() #eerste lijntje overslaan, want dit zegt task, duration, priority
        for line in file:
            name, duration, priority = line.strip().split(',')
            self.add_task(name, int(duration), int(priority))
        file.close()

    def sorted_insert_by_priority(self, head, node):
        if head is None or node.duration < head.duration:
            node.next = head
            return node

        current = head
        while current.next is not None and current.next.duraton <= node.duration:
            current = current.next



