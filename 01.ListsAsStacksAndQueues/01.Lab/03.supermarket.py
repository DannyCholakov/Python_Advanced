from collections import deque

def supermarket_queue():
    queue = deque()

    while True:
        command = input()

        if command == "End":
            print(f"{len(queue)} people remaining.")
            break
        elif command == "Paid":
            while queue:
                print(queue.popleft())
        else:
            queue.append(command)

supermarket_queue()
