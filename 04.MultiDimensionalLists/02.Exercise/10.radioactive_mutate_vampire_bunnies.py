def spread_bunnies(lair, n, m):
    new_lair = [row[:] for row in lair]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(n):
        for c in range(m):
            if lair[r][c] == "B":
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and lair[nr][nc] != "B":
                        new_lair[nr][nc] = "B"
    return new_lair

def play_game(n, m, lair, moves):
    player_pos = None
    for r in range(n):
        for c in range(m):
            if lair[r][c] == "P":
                player_pos = (r, c)

    directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    for move in moves:
        new_r, new_c = player_pos[0] + directions[move][0], player_pos[1] + directions[move][1]

        lair[player_pos[0]][player_pos[1]] = "."

        if not (0 <= new_r < n and 0 <= new_c < m):  # Player escapes
            lair = spread_bunnies(lair, n, m)
            for row in lair:
                print("".join(row))
            print(f"won: {player_pos[0]} {player_pos[1]}")
            return

        if lair[new_r][new_c] == "B":  # Player dies
            lair = spread_bunnies(lair, n, m)
            for row in lair:
                print("".join(row))
            print(f"dead: {new_r} {new_c}")
            return

        player_pos = (new_r, new_c)
        lair[new_r][new_c] = "P"

        lair = spread_bunnies(lair, n, m)
        if lair[new_r][new_c] == "B":  # Player dies after bunnies spread
            for row in lair:
                print("".join(row))
            print(f"dead: {new_r} {new_c}")
            return

n, m = map(int, input().split())
lair = [list(input()) for _ in range(n)]
moves = input().strip()

play_game(n, m, lair, moves)
