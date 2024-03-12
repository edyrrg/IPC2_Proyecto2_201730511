class Node:
    def __init__(self,
                 __data,
                 _next=None,
                 _prev=None,
                 _up=None,
                 _down=None):
        self.__data = __data
        self.next = _next
        self.prev = _prev
        self.up = _up
        self.down = _down

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if data:
            self.__data = data
        raise TypeError('data cannot be changed because data is None')

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return self.data != other.data

    def __lt__(self, other):
        return self.data < other.data

    def __le__(self, other):
        return self.data <= other.data

    def __gt__(self, other):
        return self.data > other.data

    def __ge__(self, other):
        return self.data >= other.data


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    print(n1.data, n2.data, n3.data)
