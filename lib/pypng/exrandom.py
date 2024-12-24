# An example program that create a random 64×64 RGB PNG file.
# Inspired by https://github.com/drj11/pypng/issues/120
import random

import png

width = 64
height = 64

# values per row
vpr = 3 * width

# Create a 2D matrix, a sequence of rows. Each row has vpr values.
m = [[0] * vpr for y_ in range(height)]

for y in range(len(m)):
    for x in range(len(m[y])):
        m[y][x] = random.randint(0, 255)

png.from_array(m, "RGB").save("random.png")
