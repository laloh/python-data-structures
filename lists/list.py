from node import Node


class UnorderedList:
    def __init__(self):
        self.rear = None
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        if self.head is None:
            self.rear = temp
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        temp = Node(item)
        self.rear.set_next(temp)
        self.rear = temp

    def show_items(self):
        current = self.head
        while current is not None:
            print(current.get_data())
            current = current.get_next()
        print("the head is", self.head.get_data())
        print("the rear is:", self.rear.get_data())


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def show_items(self):
        current = self.head
        while current is not None:
            print(current.get_data())
            current = current.get_next()


mylist = UnorderedList()
mylist.add(10)
mylist.add(20)
mylist.add(30)
mylist.append(100)
mylist.show_items()

mylist2 = OrderedList()
mylist2.add(4)
mylist2.add(2)
mylist2.add(6)
mylist2.add(1)
mylist2.show_items()

