# Game of Life

## About Game of Life

The universe of the Game of Life is a two-dimensional grid of cells. Each cell is in one of two possible states, live or dead.

Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

- Any live cell with fewer than two live neighbors dies, as if by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules to every cell in the seed. Each subsequent generation is created by applying the rules to every cell from the preceding generation.

## How to Start
You should put your first generation of cells (2D grid of cells) as text file and name it as seed.txt.

Please ensure that your grid is in **m x n** dimension and only contains
'X' or "_". Do not include any other letters.

The sample input file is given below for reference:

Correct Input file (seed.txt):
```
__________________
__________________
__________________
__________________
__________________
______X____X______
____XX_XXXX_XX____
______X____X______
__________________
__________________
__________________
__________________
__________________
```

Wrong Input file 1 (seed.txt):
```
I love apple
I love grapes
```

Wrong Input file 2 (seed.txt):
```
__________________
__________________
__________________
__________________
__________________
______1____1______
____11_1111_11____
______1____1______
__________________
__________________
__________________
__________________
__________________
```

After that, place that file in the input file in the game_of_life

Then, you can run main.py and it will generate for you the starting generation and 
next 10 generations as an outcome in the console.