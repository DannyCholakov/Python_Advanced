# Lists as Stacks and Queues in Python

# Stacks: LIFO (Last In, First Out)
# A stack is a data structure that follows the principle of last-in, first-out.
# You can use a list to simulate a stack in Python.

# Example of a Stack:
stack = []

# Push (Add elements to the stack)
stack.append(10)  # Add 10
stack.append(20)  # Add 20
print("Stack after pushes:", stack)  # Output: [10, 20]

# Pop (Remove the last element added)
last_element = stack.pop()  # Removes 20
print("Popped element:", last_element)  # Output: 20
print("Stack after pop:", stack)  # Output: [10]

# Peek (View the top element without removing it)
if stack:
    top_element = stack[-1]
    print("Top element:", top_element)  # Output: 10

# Check if the stack is empty
is_empty = len(stack) == 0
print("Is stack empty?", is_empty)  # Output: False

# Queues: FIFO (First In, First Out)
# A queue is a data structure that follows the principle of first-in, first-out.

# Example of a Queue:
queue = []

# Enqueue (Add elements to the queue)
queue.append(10)  # Add 10
queue.append(20)  # Add 20
print("Queue after enqueues:", queue)  # Output: [10, 20]

# Dequeue (Remove the first element added)
front_element = queue.pop(0)  # Removes 10
print("Dequeued element:", front_element)  # Output: 10
print("Queue after dequeue:", queue)  # Output: [20]

# Peek (View the front element without removing it)
if queue:
    front_element = queue[0]
    print("Front element:", front_element)  # Output: 20

# Check if the queue is empty
is_empty = len(queue) == 0
print("Is queue empty?", is_empty)  # Output: False

# Using `collections.deque` for better performance in queues
# deque is optimized for fast appends and pops from both ends.
from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
print("Deque after enqueues:", queue)  # Output: deque([10, 20])

# Dequeue
front_element = queue.popleft()  # Removes 10
print("Dequeued element:", front_element)  # Output: 10
print("Deque after dequeue:", queue)  # Output: deque([20])

# Using `collections.deque` as a stack
stack = deque()

# Push
stack.append(10)
stack.append(20)
print("Deque as stack after pushes:", stack)  # Output: deque([10, 20])

# Pop
last_element = stack.pop()  # Removes 20
print("Popped element:", last_element)  # Output: 20
print("Deque as stack after pop:", stack)  # Output: deque([10])

# Common Problems and Patterns

# 1. Reverse a List using a Stack
stack = [1, 2, 3, 4]
reversed_list = []
while stack:
    reversed_list.append(stack.pop())
print("Reversed list:", reversed_list)  # Output: [4, 3, 2, 1]

# 2. Check for Palindromes using Stack and Queue
word = "racecar"
queue = deque(word)
stack = list(word)

is_palindrome = True
while queue:
    if queue.popleft() != stack.pop():
        is_palindrome = False
        break
print("Is palindrome?", is_palindrome)  # Output: True

# 3. Balanced Parentheses Check using a Stack
def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0

print(is_balanced("({[()]})"))  # Output: True
print(is_balanced("({[()]}"))   # Output: False

# 4. Task Scheduling using a Queue
tasks = deque(["task1", "task2", "task3"])

while tasks:
    current_task = tasks.popleft()  # Process the task
    print(f"Processing {current_task}")

# Summary Table
# | Operation       | Stack (LIFO)                  | Queue (FIFO)                  |
# |------------------|-------------------------------|--------------------------------|
# | Add Element      | `append()`                   | `append()`                    |
# | Remove Element   | `pop()`                      | `pop(0)` (or `popleft()` for `deque`) |
# | Peek             | `stack[-1]`                 | `queue[0]`                    |
# | Check Empty      | `len(stack) == 0`           | `len(queue) == 0`             |
