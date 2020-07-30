
# by Caleb Otchi


import array as ar
import random as ran


class Deque:

    def __init__(self):
        self.deque = ar.array('i', [])
        self.ft = 0
        self.rr = 0
        self.itemCount = 0

    # A function to fill the array by half
    def fill_half(self):
        for i in range(10):
            num = ran.randint(1, 100)
            self.deque.append(num)
            self.itemCount += 1

    # A function to return the current size of the deque
    def deque_size(self):
        print("size of the Deque is", self.itemCount)

    # A function to check if the deque is empty
    def is_empty(self):
        if self.itemCount == 0:
            return "deque is empty"
        else:
            return "there are values in the deque"

    def display_deque(self):
        return self.deque

    def add_to_front(self):
        if self.itemCount == 20:
            return "The deque is full, cannot add value"
        else:
            self.deque.insert(self.ft, ran.randint(1, 100))
            self.itemCount += 1
            self.ft = 0
            print("value has been added to front")
            return Deque.display_deque(self)

    # a limit of twenty was given to the arrays. after 20, no more values can be added
    # you cannot remove from an empty array either
    def add_to_back(self):
        if self.itemCount == 20:
            return "The deque is full, cannot add value"
        else:
            self.deque.insert(self.itemCount, ran.randint(1, 100))
            self.itemCount += 1
            print("value has been added to the back")
            return Deque.display_deque(self)

    def remove_from_front(self):
        if self.itemCount == 0:
            return "The deque is empty,cannot remove a value"
        else:
            self.deque.pop(0)
            self.itemCount -= 1
            print("value has been removed from the front")
            return Deque.display_deque(self)

    def remove_from_back(self):
        if self.itemCount == 0:
            return "The deque is empty,cannot remove a value"
        else:
            self.deque.pop(-1)
            self.itemCount -= 1
            self.rr -= 1
            print("value has been removed from the back")
            return Deque.display_deque(self)

    def get_deque(self):
        Deque.fill_half(self)
        return Deque.display_deque(self)

    def prob_a(self):
        p = round(ran.random(), 2)
        print(p)

        if 0 < p <= 0.1:
            print(Deque.add_to_front(self))
            return Deque.deque_size(self)

        elif 0.1 < p <= 0.3:
            print(Deque.remove_from_front(self))
            print(Deque.is_empty(self))
            return Deque.deque_size(self)

        elif 0.3 < p <= 0.4:
            print(Deque.add_to_back(self))
            return Deque.deque_size(self)

        elif 0.4 < p <= 1.0:
            print(Deque.remove_from_back(self))
            print(Deque.is_empty(self))
            return Deque.deque_size(self)
        else:
            pass

    def prob_b(self):
        p = round(ran.random(), 2)
        print(p)
        if 0 < p <= 0.1:
            print(Deque.add_to_front(self))
            return Deque.deque_size(self)
        elif 0.1 < p <= 0.7:
            print(Deque.remove_from_front(self))
            print(Deque.is_empty(self))
            return Deque.deque_size(self)
        elif 0.7 < p <= 0.8:
            print(Deque.add_to_back(self))
            return Deque.deque_size(self)
        elif 0.8 < p <= 1.0:
            print(Deque.remove_from_back(self))
            print(Deque.is_empty(self))
            return Deque.deque_size(self)
        else:
            pass


thisDeque = Deque()

print(thisDeque.get_deque())
thisDeque.prob_a()
thisDeque.prob_a()
thisDeque.prob_a()

thisDeque.prob_b()
thisDeque.prob_b()
thisDeque.prob_b()
