# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# fruits = ["banana", "orange", "peach", "pineapple", "apple", "mango"]

# odds = [i for i in range(0, 100) if i % 2 != 0]
# reversed = odds[::-1]

# # del numbers[-1]
# numbers = numbers[:]
# print(numbers)

from stack import Stack

s1 = Stack()
s1bin = Stack()

s1.push(10).push(100)
print(s1.data)

s1bin.push(s1.pop())
s1bin.push(s1.pop())
s1bin.push(s1.pop())
print(s1.data)
print(s1bin.data)
