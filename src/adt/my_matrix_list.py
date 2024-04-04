from src.adt.my_list import MyList
from src.adt.node import Node
from src.services.matrix_service import MatrixService


class MyMatrixList(MyList):

    def __init__(self, head=None):
        super().__init__(head=head)

    def append(self, data, new_row=False):
        if not data:
            raise Exception('The data value cannot be empty')
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current_row = self.get_last_row()
        if new_row:
            while current_row.down:
                current_row = current_row.down
            MatrixService.connect_vertical_nodes(node_up=current_row, node_down=new_node)
            return
        if current_row.up:
            previous_row = current_row.up
            while current_row.next:
                current_row = current_row.next
                previous_row = previous_row.next
            MatrixService.connect_horizontal_nodes(node_prev=current_row, node_next=new_node)
            MatrixService.connect_vertical_nodes(node_up=previous_row.next, node_down=new_node)
            return
        while current_row.next:
            current_row = current_row.next
        MatrixService.connect_horizontal_nodes(node_prev=current_row, node_next=new_node)

    def get_last_row(self):
        if not self.head:
            raise Exception('The matrix list is empty')
        current_down = self.head
        while current_down.down:
            current_down = current_down.down
        return current_down

    def clear_list(self):
        self.head = None

    def is_empty(self):
        return True if self.head is None else False

    def size(self):
        if self.is_empty():
            raise Exception('The matrix list is empty')
        current_row = self.head
        current_column = current_row
        x = 0
        y = 0
        while current_row:
            x += 1
            current_row = current_row.down
        while current_column:
            y += 1
            current_column = current_column.next
        return x, y

    def display_list(self):
        if not self.head:
            raise Exception('The matrix list is empty, cannot display it')

        current_row = self.head
        while current_row:
            current_column = current_row
            while current_column:
                if current_column.next:
                    print(current_column.data, end=' ')
                if not current_column.next:
                    print(current_column.data, end='')
                current_column = current_column.next
            print()
            current_row = current_row.down

    def get_last_node(self):
        last_row = self.head
        while last_row.down:
            last_row = last_row.down
        last_column = last_row
        while last_column.next:
            last_column = last_column.next
        last_node = last_column
        return last_node

    def __reversed__(self):
        if not self.head:
            raise Exception('The matrix list is empty, cannot reverse it')
        current_row = self.get_last_node()
        #while current_row.next:
        #    current_row = current_row.next
        while current_row:
            current_column = current_row
            while current_column:
                yield current_column
                current_column = current_column.prev
            current_row = current_row.up

    def __iter__(self):
        if not self.head:
            raise Exception('The matrix list is empty, cannot iterate over')
        current_row = self.head
        while current_row:
            current_column = current_row
            while current_column:
                if current_column.next:
                    yield current_column, False
                if not current_column.next:
                    yield current_column, False
                current_column = current_column.next
            current_row = current_row.down

    def to_str(self):
        if not self.head:
            raise Exception('The matrix list is empty, cannot display it')
        tmp_str = "\t"
        current_row = self.head
        while current_row:
            current_column = current_row
            while current_column:
                if current_column.next:
                    tmp_str += str(current_column.data) + ' '
                if not current_column.next:
                    tmp_str += str(current_column.data) + ''
                current_column = current_column.next
            tmp_str += "\n\t"
            current_row = current_row.down
        return tmp_str

    def get_node_by_index(self, xi, yi):
        if xi <= 0 or yi <= 0:
            raise IndexError("Index must be greater than zero")
        if self.is_empty():
            raise Exception("The matrix list is empty, cannot display it")
        if self.head and xi == 1 and yi == 1:
            return self.head
        count_x = 1
        count_y = 1
        current_node = self.head
        if self.head and xi == 1 and yi > 1:
            while current_node and count_y < yi:
                count_y += 1
                current_node = current_node.down
                if count_y == yi:
                    return current_node
                if current_node.down is None:
                    raise IndexError("Not enough elements in vertical direction...")
        if self.head and yi == 1 and xi > 1:
            while current_node and count_x < xi:
                count_x += 1
                current_node = current_node.next
                if count_x == xi:
                    return current_node
                if current_node.next is None:
                    raise IndexError("Not enough elements in horizontal direction...")
        while current_node.next and count_x < xi:
            count_x += 1
            current_node = current_node.next
            if count_x == xi:
                while current_node.down and count_y < yi:
                    count_y += 1
                    current_node = current_node.down
                    if count_y == yi:
                        return current_node
                    if current_node.down is None:
                        raise IndexError("Not enough elements in vertical direction...")
            if current_node.next is None:
                raise IndexError("Not enough elements in horizontal direction...")

    def get_node_data_by_index(self, xi, yi):
        if xi <= 0 or yi <= 0:
            raise IndexError("Index must be greater than zero")
        if self.is_empty():
            raise Exception("The matrix list is empty, cannot display it")
        if self.head and xi == 1 and yi == 1:
            return self.head.data
        count_x = 1
        count_y = 1
        current_node = self.head
        if self.head and xi == 1 and yi > 1:
            while current_node and count_y < yi:
                count_y += 1
                current_node = current_node.down
                if count_y == yi:
                    return current_node.data
                if current_node.down is None:
                    raise IndexError("Not enough elements in vertical direction...")
        if self.head and yi == 1 and xi > 1:
            while current_node and count_x < xi:
                count_x += 1
                current_node = current_node.next
                if count_x == xi:
                    return current_node.data
                if current_node.next is None:
                    raise IndexError("Not enough elements in horizontal direction...")
        while current_node.next and count_x < xi:
            count_x += 1
            current_node = current_node.next
            if count_x == xi:
                while current_node.down and count_y < yi:
                    count_y += 1
                    current_node = current_node.down
                    if count_y == yi:
                        return current_node.data
                    if current_node.down is None:
                        raise IndexError("Not enough elements in vertical direction...")
            if current_node.next is None:
                raise IndexError("Not enough elements in horizontal direction...")

    def search_node_data(self, search_value):
        if not self.head:
            raise Exception('The matrix list is empty, cannot display it')

        current_row = self.head
        while current_row:
            current_column = current_row
            while current_column:
                if current_column.__eq__(search_value):
                    return current_column
                current_column = current_column.next
            current_row = current_row.down
        return None

    def update_node_data_by_index(self, xi, yi, value):
        if xi <= 0 or yi <= 0 or not value:
            raise IndexError("Index must be greater than zero or value is None")
        if self.is_empty():
            raise Exception("The matrix list is empty, cannot display it")
        if self.head and xi == 1 and yi == 1:
            self.head.data = value
        count_x = 1
        count_y = 1
        current_node = self.head
        if self.head and xi == 1 and yi > 1:
            while current_node and count_y < yi:
                count_y += 1
                current_node = current_node.down
                if count_y == yi:
                    current_node.data = value
                if current_node.down is None:
                    raise IndexError("Not enough elements in vertical direction...")
        if self.head and yi == 1 and xi > 1:
            while current_node and count_x < xi:
                count_x += 1
                current_node = current_node.next
                if count_x == xi:
                    current_node.data = value
                if current_node.next is None:
                    raise IndexError("Not enough elements in horizontal direction...")
        while current_node.next and count_x < xi:
            count_x += 1
            current_node = current_node.next
            if count_x == xi:
                while current_node.down and count_y < yi:
                    count_y += 1
                    current_node = current_node.down
                    if count_y == yi:
                        current_node.data = value
                        return
                    if current_node.down is None:
                        raise IndexError("Not enough elements in vertical direction...")
            if current_node.next is None:
                raise IndexError("Not enough elements in horizontal direction...")


if __name__ == '__main__':
    patron1 = "--***********-**-*-*-*---*---**---*-*-*-*-*-***-**-*-*-*-*-*------*-*-*-*-******-*-*-*-*-**-------*-*-*-**-*****-*--**-**--------*----*******-********"
    patron2 = "123456789ABCDEFG"
    my_matrix_list = MyMatrixList()
    count = 0
    for i in range(4):
        for j in range(4):
            if j == 0:
                my_matrix_list.append(patron2[count], new_row=True)
                count += 1
                continue
            my_matrix_list.append(patron2[count])
            count += 1
    my_matrix_list.display_list()
    print(my_matrix_list.get_node_data_by_index(xi=2, yi=3))
    print(my_matrix_list.search_node_data("*"))
    my_matrix_list.update_node_data_by_index(3, 4, "Z")
    my_matrix_list.display_list()
    print(my_matrix_list.get_node_data_by_index(2, 2))
    print(my_matrix_list.to_str())
    print(my_matrix_list.size())
    print(my_matrix_list.get_last_node())
    # for node, arg in my_matrix_list:
    #    print(node, arg)
    for node in reversed(my_matrix_list):
        print(node)
