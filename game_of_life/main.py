def main():
    game_of_life('game_of_life/input/seed.txt', 10)


def game_of_life(seed_file, generations=10):
    current_gen = read_input(seed_file)

    print("Seed State:")
    print_generation(current_gen)
    for i in range(generations):
        current_gen = get_next_generation(current_gen)
        print(f"\nGeneration {i + 1}:")
        print_generation(current_gen)


def read_input(input_file):
    grid = []
    with open(input_file, 'r') as file:
        for line in file:
            grid_line = [1 if char == 'X' else 0 for char in line.strip()]
            grid.append(grid_line)
    return grid


def get_next_generation(current_generation):
    new_generation = [[0 for _ in row] for row in current_generation]
    for r in range(len(current_generation)):
        for c in range(len(current_generation[r])):
            neighbors = count_neighbors(current_generation, r, c)
            if current_generation[r][c] and neighbors in [2, 3]:
                new_generation[r][c] = 1
            elif not current_generation[r][c] and neighbors == 3:
                new_generation[r][c] = 1
    return new_generation


def count_neighbors(grid, x, y):
    neighbor_positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in neighbor_positions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny]:
            count += 1
    return count

def print_generation(grid):
    for row in grid:
        grid_row = ['X' if cell else '_' for cell in row]
        grid_row = ''.join(grid_row)
        print(grid_row)


if __name__ == "__main__":
    main()
