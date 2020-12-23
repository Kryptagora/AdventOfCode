from tqdm import tqdm

class Node:
    def __init__(self, value, parent, prev, next):
        self.value = value
        self.parent = parent
        self.prev = prev
        self.next = next

    def insert(self, value):
        node = Node(value, self.parent, self, self.next)
        self.parent.ldict[value] = node
        self.next = node
        node.next.prev = node
        return node

    def remove(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        self.parent.ldict[self.value] = None

class LinkedList:
    def __init__(self):
        self.ldict = {}

    def add(self, prev, value):
        if prev is None:
            node = Node(value, self, None, None)
            node.next = node
            node.prev = node
            self.ldict[value] = node
            return node

        else:
            node = Node(value, self, prev, prev.next)
            prev.next = node
            node.next.prev = node
            self.ldict[value] = node
            return node

    def find(self, value):
        return self.ldict[value]

    def to_list(self, start):
        node = self.ldict[start]
        node_list = [node.value]
        node = node.next
        while node.value != start:
            node_list.append(node.value)
            node = node.next

        return node_list



def part_1(input_data: str, steps:int=100):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = [int(i) for i in input_data]
    LIST = LinkedList()
    prev_value = None

    for i in input_data:
        prev_value = LIST.add(prev_value, i)

    curr = LIST.find(input_data[0])
    curr_idx = len(LIST.ldict)

    for _ in tqdm(range(steps)):
        curr_val = curr.value
        pickup = []
        pickup_node = curr.next

        for _ in range(3):
            pickup.append(pickup_node.value)
            _ = pickup_node.next
            pickup_node.remove()
            pickup_node = _

        if curr_val == 1:
            destination = curr_idx
        else:
            destination = curr_val - 1

        while destination in pickup:
            if destination == 1:
                destination = curr_idx
            else:
                destination -= 1

        destination_node = LIST.find(destination)
        for i in pickup:
            destination_node = destination_node.insert(i)

        curr = curr.next

    values = LIST.to_list(1)

    return ''.join([str(i) for i in values[1:]])



def part_2(input_data: str):
    """Same as abouve, new step size and the new rule
    (labeling the cups up to one million)"""
    if input_data == "": return ""

    input_data = [int(i) for i in input_data]
    LIST = LinkedList()
    prev_value = None
    steps_rearrange = 1000000
    steps_crabplay = 10000000

    for i in input_data:
        prev_value = LIST.add(prev_value, i)

    rule = 10
    while len(LIST.ldict) < steps_rearrange:
        prev_value = LIST.add(prev_value, rule)
        rule += 1


    curr = LIST.find(input_data[0])
    curr_idx = len(LIST.ldict)

    for _ in tqdm(range(steps_crabplay)):
        if _ == 8000000:
            print('Almost there, chirp, chirp, chirp!')

        curr_val = curr.value
        pickup = []
        pickup_node = curr.next

        for _ in range(3):
            pickup.append(pickup_node.value)
            _ = pickup_node.next
            pickup_node.remove()
            pickup_node = _

        if curr_val == 1:
            destination = curr_idx
        else:
            destination = curr_val - 1

        while destination in pickup:
            if destination == 1:
                destination = curr_idx
            else:
                destination -= 1

        destination_node = LIST.find(destination)
        for i in pickup:
            destination_node = destination_node.insert(i)

        curr = curr.next

    sig_node = LIST.find(1)
    sig_nval = sig_node.next.value
    if sig_node.next.next is not None:
        sig_nnval = sig_node.next.next.value

    return sig_nval*sig_nnval
