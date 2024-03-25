from src.adt.node import Node


class MatrixService:

    @staticmethod
    def connect_vertical_nodes(node_up, node_down):
        if node_down and node_up:
            node_up.down = node_down
            node_down.up = node_up

    @staticmethod
    def connect_horizontal_nodes(node_prev, node_next):
        if node_prev and node_next:
            node_prev.next = node_next
            node_next.prev = node_prev
