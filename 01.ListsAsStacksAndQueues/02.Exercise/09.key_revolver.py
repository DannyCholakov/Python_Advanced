def key_revolver():
    bullet_price = int(input())
    barrel_size = int(input())
    bullets = list(map(int, input().split()))
    locks = list(map(int, input().split()))
    intelligence_value = int(input())

    money_spent = 0
    bullet_count = len(bullets)

    while bullets and locks:
        bullet = bullets.pop()
        lock = locks[0]

        if bullet >= lock:
            print("Bang!")
            locks.pop(0)
        else:
            print("Ping!")

        money_spent += bullet_price

        if not bullets and locks:
            print("Reloading!")

    remaining_locks = len(locks)
    if remaining_locks == 0:

        money_earned = intelligence_value - money_spent
        print(f"{len(bullets)} bullets left. Earned ${money_earned}")
    else:
        print(f"Couldn't get through. Locks left: {remaining_locks}")

key_revolver()
