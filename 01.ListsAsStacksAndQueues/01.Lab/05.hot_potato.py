from collections import deque

def hot_potato():
    kids = input().split()
    toss = int(input())

    queue = deque(kids)

    while len(queue) > 1:
        queue.rotate(-(toss - 1))
        removed_kid = queue.popleft()
        print(f"Removed {removed_kid}")

    last_kid = queue.popleft()
    print(f"Last is {last_kid}")

hot_potato()
