"""
FIFO
"""


class MyQueue:

    def __init__(self):
        self.data = []

    def push(self, val):
        if val:
            self.data.append(val)
        return self

    def pop(self):
        try:
            val = self.data[0]

            for i in range(len(self.data)):
                try:
                    self.data[i] = self.data[i + 1]
                except IndexError:
                    pass
            del self.data[-1]

            return val
        except IndexError:
            return
