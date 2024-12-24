# pricli.py

# This file is an experiment in using `python -m pydoc`
# to make HTML documentation.

"""
Python Raster Image Command Line Interface

The Python Raster Immage Command Line Interface consists of
a series of tools all available from the command line.
A tool begins with `pri`. There are a few naming conventions
that hint at what the tool does.

A tool that produces a PNG file will end in `png`.
A tool that converts from one format to another will have
`to` in the middle.
That should explain the tools
`pripamtopng` `priplan9topng` `pripngtopam`.
The later produces a NetPBM PAM file, which isn't stricly
inferrable from the above rules, but is perhaps guessable.

Often a tool that outputs PNG files will also take PNG files as input,
but there's no hint in the name.
For example `prirowpng` `pripalpng` `priweavepng` all output
PNG files, and also take PNG files as input.
The tool `priforgepng` outputs PNG files, but takes no input
(except from the command line).
"""

# END

