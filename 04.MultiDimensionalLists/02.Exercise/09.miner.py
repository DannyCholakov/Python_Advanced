def move_miner(n, commands, field):
    miner_pos = None
    coal_count = 0

    for r in range(n):
        for c in range(n):
            if field[r][c] == "s":
                miner_pos = (r, c)
            elif field[r][c] == "c":
                coal_count += 1

    moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

    for command in commands:
        new_r, new_c = miner_pos[0] + moves[command][0], miner_pos[1] + moves[command][1]

        if 0 <= new_r < n and 0 <= new_c < n:
            miner_pos = (new_r, new_c)

            if field[new_r][new_c] == "c":
                coal_count -= 1
                field[new_r][new_c] = "*"
                if coal_count == 0:
                    print(f"You collected all coal! ({new_r}, {new_c})")
                    return

            elif field[new_r][new_c] == "e":
                print(f"Game over! ({new_r}, {new_c})")
                return

    print(f"{coal_count} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")


n = int(input())
commands = input().split()
field = [input().split() for _ in range(n)]

move_miner(n, commands, field)
