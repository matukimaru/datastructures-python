"""
LIFO
"""
class MyStack:
    def __init__(self):
        self.data = []

    def __str__(self):
        return self.data

    def push(self, val):
        if val:
            self.data.append(val)
        return self  # permit method chaining

    def pop(self):
        try:
            val = self.data[-1]
            del self.data[-1]
            return val
        except IndexError as ie:
            print("Stack is empty.")
            return
