# Conway's Game of Live with 2dconvolve

I implemented this as a kata because I wanted
to look at how to implement Conway's Game of Life
using [convolution](https://en.wikipedia.org/wiki/Convolution). 

This is inspired by some interesting solutions I saw where convolution is used to calculate the neighbouring mine tiles
in Mine Sweeper. It also ties into my interest in Fourier Transforms because it's also a type of integral transform.

How it works is pretty simple, for every single cell in the grid, it applies the following impulse:

```python
kernel = [
  [1, 1, 1]
  [1, 0, 1]
  [1, 1, 1]
]
```

When you apply this kernel to a cell, it centers on the zero and writes the dot product of the overlapping portion of the grid with kernel/impulse into the cell.

The convolve2d function essentially generates a new matrix with the same dimensions as the cell grid where each cell contains an integer value representing the number of neighbours. Simple, but cool.

![A screenshot of this Conway's Game of Life program running. The window title reads 'Total population size: 6095'. The window content is a grid of cells, live cells are white while dead cells are black and this screenshot shows two symmetrical looking clusters of live cells, one to the east side of the grid and the other on the south side of the grid. The south grid has two 'gliders' coming out the top and one 'glider' coming out the bottom.](preview/game_of_life_demo.png)

## Runnning

Requires Python 3 to run. If you use PyEnv, just switch into Python 3 before running.

```shell
pip install
python main.py
```
