import random as r

# THE STACK
MAX = 5
stack = []

print("\nSTACK")
print("=====")
print("\n\tPUSH")
#   Pushing to the stack
for idx in range(MAX+1):
    message = "#" * idx
    stack.append(message)
    print(stack[idx])

print("\n\tPOP")
#   Popping from the stack
for idx in range(MAX+1):
    print(stack.pop())

del stack
print()
# THE STACK


# THE QUEUE
queue = []
print("\nQUEUE")
print("=====")
print("\n\tPUSH")
for idx in range(MAX+1):
    message = "#" * idx
    queue.append(message)
    print(queue[idx])
print("\n\tQUEUE")
for idx in range(MAX+1):
    print(queue.pop(0))
