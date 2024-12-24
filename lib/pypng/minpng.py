# minpng.py

"""
minpng.py - MinPNG (minimal PNG) is the antidote to PyPNG.

Where PyPNG is several thousand lines and
can write and read all PNG formats,
MinPNG is two-dozen lines that writes
an 8-bit greyscale PNG and does nothing else.

Please copy this file into your own code.
An original can be found here: https://gitlab.com/drj11/minpng

I, David Jones, the author, put this file into the public domain.
"""

import struct
import zlib


def rows_to_png(out, rows, width, height):
    """Write to the binary file `out` a single channel 8-bit PNG.
    `rows` should yield each row in turn;
    `width` and `height` gives the image size in pixels.
    """

    # Write out PNG signature.
    out.write(bytearray([137, 80, 78, 71, 13, 10, 26, 10]))
    # Write out PNG header chunk.
    header = struct.pack(">2LBBBBB", width, height, 8, 0, 0, 0, 0)
    write_chunk(out, b"IHDR", header)

    bs = bytearray()
    for row in rows:
        bs.append(0)
        bs.extend(row)
    write_chunk(out, b"IDAT", zlib.compress(bs))

    write_chunk(out, b"IEND", bytearray())


def write_chunk(out, chunk_type, data):
    assert 4 == len(chunk_type)
    out.write(struct.pack(">L", len(data)))
    out.write(chunk_type)
    out.write(data)
    checksum = zlib.crc32(chunk_type)
    checksum = zlib.crc32(data, checksum)
    out.write(struct.pack(">L", checksum))


### The rest of this file is a demo / test.
### You should probably delete it.

### Reads 200 rows of 320 bytes from stdin,
### and output a PNG of them to stdout.

### Try running with
###   python -m minpng < /dev/urandom > random.png

import sys


def main():
    stdin = sys.stdin.buffer
    w = 320
    h = 200
    rows = (stdin.read(w) for _ in range(h))
    rows_to_png(sys.stdout.buffer, rows, w, h)


if __name__ == "__main__":
    main()
