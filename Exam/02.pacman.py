def move_pacman(grid, direction, position):
    N = len(grid)
    row, col = position

    if direction == "up":
        row = (row - 1) % N
    elif direction == "down":
        row = (row + 1) % N
    elif direction == "left":
        col = (col - 1) % N
    elif direction == "right":
        col = (col + 1) % N

    return row, col


def pacman_game(N, grid, commands):
    pacman_health = 100
    collected_stars = 0
    total_stars = sum(row.count('*') for row in grid)
    freezer_activated = False
    pacman_position = None
    game_over = False

    # Find initial Pacman position
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'P':
                pacman_position = (i, j)
                grid[i][j] = '-'
                break
        if pacman_position:
            break

    for command in commands:
        if pacman_health <= 0:
            game_over = True
            print(f"Game over! Pacman last coordinates [{pacman_position[0]},{pacman_position[1]}]")
            print(f"Health: {pacman_health}")
            if total_stars - collected_stars > 0:
                print(f"Uncollected stars: {total_stars - collected_stars}")
            break

        if command == "end":
            break

        # Move Pacman based on the command
        pacman_position = move_pacman(grid, command, pacman_position)
        row, col = pacman_position

        # Check the current position
        current_cell = grid[row][col]

        if current_cell == 'G':  # Ghost
            if freezer_activated:
                freezer_activated = False  # Reset freezer
            else:
                pacman_health -= 50
            grid[row][col] = '-'  # Always turn ghost into empty space after Pacman passes

        elif current_cell == '*':  # Star
            collected_stars += 1
            grid[row][col] = '-'  # Remove the star

        elif current_cell == 'F':  # Freezer
            freezer_activated = True
            grid[row][col] = '-'

        # Check if Pacman has collected all the stars
        if collected_stars == total_stars:
            print("Pacman wins! All the stars are collected.")
            print(f"Health: {pacman_health}")
            break

    # If Pacman didn't collect all the stars and still has health, print the fail message
    if pacman_health > 0 and collected_stars != total_stars and not game_over:
        print(f"Pacman failed to collect all the stars.")
        print(f"Health: {pacman_health}")
        if total_stars - collected_stars > 0:
            print(f"Uncollected stars: {total_stars - collected_stars}")

    # Mark Pacman's final position as 'P' on the grid
    row, col = pacman_position
    grid[row][col] = 'P'

    # Print the final grid
    for row in grid:
        print(''.join(row))


# Get user input for the grid
N = int(input())
grid = []
for i in range(N):
    grid.append(list(input()))

# Get user input for the commands
commands = []
while True:
    command = input()
    if command == "end":
        commands.append(command)
        break
    elif command in ["up", "down", "left", "right"]:
        commands.append(command)

# Call the game function
pacman_game(N, grid, commands)