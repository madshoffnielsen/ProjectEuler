def lattice_paths(grid_size):
    # Create a 2D array to store the number of paths to each point
    paths = [[0] * (grid_size + 1) for _ in range(grid_size + 1)]
    
    # There is exactly one way to reach any point in the first row or first column
    for i in range(grid_size + 1):
        paths[i][0] = 1
        paths[0][i] = 1
    
    # Calculate the number of paths for each point in the grid
    for i in range(1, grid_size + 1):
        for j in range(1, grid_size + 1):
            paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
    
    return paths[grid_size][grid_size]

if __name__ == "__main__":
    grid_size = 20
    result = lattice_paths(grid_size)
    print(f"The number of routes through a {grid_size}x{grid_size} grid is {result}")