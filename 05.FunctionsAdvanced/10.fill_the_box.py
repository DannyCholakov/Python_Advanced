def fill_the_box(height, length, width, *cubes):
    box_volume = height * length * width  # Total space in the box
    remaining_space = box_volume

    for cube in cubes:
        if cube == "Finish":
            break
        if remaining_space >= cube:
            remaining_space -= cube
        else:
            return f"No more free space! You have {sum(cubes[cubes.index(cube):]) - remaining_space} more cubes."

    return f"There is free space in the box. You could put {remaining_space} more cubes."
