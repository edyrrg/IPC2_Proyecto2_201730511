from src.adt.my_list import MyList
from src.adt.node import Node


class MySimpleList(MyList):

    def __init__(self, head=None):
        super().__init__(head=head)

    def append(self, data):
        new_node = Node(data)
        if not data:
            Exception('The data value cannot be empty')
            return
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def is_empty(self):
        return True if self.head is None else False

    def size(self):
        if self.is_empty():
            print('The simple list is empty')
            return
        if not self.head.next:
            return 1
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def display_list(self):
        if self.is_empty():
            raise Exception('The simple list is empty')
        current_node = self.head
        if not current_node.next:
            print(current_node.data)
            return
        while current_node is not None:
            print(current_node.data)
            if not current_node.next:
                break
            current_node = current_node.next

    def clear_list(self):
        self.head = None

    def get_node_data_by_index(self, index):
        if index <= 0:
            raise IndexError("Index must be greater than zero")
        if self.is_empty():
            raise Exception("List is empty...")
        if self.head and index == 1:
            return self.head.data
        count = 1
        current_node = self.head
        while current_node.next and count < index:
            count += 1
            current_node = current_node.next
            if count == index:
                return current_node.data
            if current_node.next is None:
                raise IndexError("Not enough elements in the list...")

    def search_node_data(self, search_value):
        current_node = self.head
        while current_node:
            if current_node.data.__eq__(search_value):
                return current_node.data
            current_node = current_node.next
        return None

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            data = self._current.data
            self._current = self._current.next
            return data

    def __len__(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count


if __name__ == '__main__':
    my_simple_list = MySimpleList()
    my_simple_list.append(23)
    my_simple_list.append(40)
    my_simple_list.append(33)
    my_simple_list.append(100)
    my_simple_list.append(88)
    try:
        my_simple_list.display_list()
        result_data = my_simple_list.search_node_data(23)
        if result_data:
            print(f'Data found: {result_data}')
        else:
            print('No data found')
        print(f'Data found: {my_simple_list.get_node_data_by_index(2)}')
        print(f'Size List: {my_simple_list.size()}')
    except Exception as e:
        print(e)

    for data1 in my_simple_list:
        print(f'Node: {data1}')
