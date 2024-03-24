from src.adt.node import Node


class MatrixService:
    def __init__(self):
        pass

    @staticmethod
    def append_column_to_row(row, data):
        if not data:
            Exception('The data value cannot be empty')
            return
        new_node = Node(data)
        current_row = row
        while current_row.next:
            current_row = current_row.next
        current_row.next = Node(data)
        new_node.prev = current_row

    @staticmethod
    def connect_node_up_and_down(node_up, node_down):
        if not node_up and node_down:
            Exception('The Nodes must not be None')
            return
        node_up.down = node_down
        node_down.up = node_up
