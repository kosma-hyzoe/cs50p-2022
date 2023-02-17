class Jar:
    def __init__(self, capacity=12):
        if capacity >= 0 and type(capacity) == int:
            self._capacity = capacity
            self._size = 0
        else:
            raise ValueError("Invalid capacity parameter: must be a non-negative integer.")

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n: int):
        if n < 0:
            raise ValueError("You can't deposit a negative n of cookies!")
        elif self.size + n <= self.capacity:
            self._size += n
        else:
            raise ValueError("Not enough capacity to add more cookies.")

    def withdraw(self, n: int):
        if n < 0:
            raise ValueError("You can't withdraw negative cookies!")
        elif n <= self.size:
            self._size -= n
        else:
            raise ValueError(f"Not enough cookies in the jar to withdraw {n} cookies.")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
