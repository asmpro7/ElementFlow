#!/usr/bin/env python
# Make ICC Profile

# References
#
# [ICC 2001] ICC Specification ICC.1:2001-04 (Profile version 2.4.0)
# [ICC 2004] ICC Specification ICC.1:2004-10 (Profile version 4.2.0.0)

"""
Make an ICC Profile.

The default is a grey `mntr` profile.
Specifying any red, green, or blue colorant will
change it to RGB and add default rTRC, gTRC, and bTRC tags.
"""

# Command line examples:

# Make a grey profile that sets codes 0 to 0.07 to black:
# mkiccp.py -kTRC 0.07,0
# An older version of this code was used to make an ICC profile
# suitable for Messenger space probe images, and
# was used to prepare my ancient blog post
# https://drj11.wordpress.com/2009/05/06/what-good-is-pypng-and-some-mdis-pictures-of-earth/

# Make gbr.icc a colour swapper:
# mkiccp.py --rXYZ=0.385,0.717,0.097 --gXYZ=0.143,0.061,0.714 --bXYZ=0.436,0.222,0.014


import argparse

# https://docs.python.org/3.8/library/bisect.html
import bisect

# Local module.
import iccp
import png


# For RGB input the required tags are (See [ICC 2001] 6.3.1.2):
# profileDescription [ICC 2001] 6.4.32
# mediaWhitePoint [ICC 2001] 6.4.25
# copyright [ICC 2001] 6.4.13
def rgb_profile(out, **kwargs):
    prof = iccp.Profile().rgb()
    prof.addTags(rTRC=2.2, gTRC=2.2, bTRC=2.2)
    prof.addTags(**kwargs)
    prof.write(out)


# The required tags are (See [ICC 2001] 6.3.1.1):
# - profileDescription [ICC 2001] 6.4.32
# - mediaWhitePoint [ICC 2001] 6.4.25
# - copyright [ICC 2001] 6.4.13
# and for grey profiles
# - grayTRC [ICC 2001] 6.4.19
# and for rgb profiles
# - TRC for red,green,blue
# - XYZ (Colorant) for red,green,blue
def icc_profile(out, **kwargs):
    prof = iccp.Profile().greyInput()
    if "rXYZ" in kwargs or "gXYZ" in kwargs or "bXYZ" in kwargs:
        prof.rgb()
        prof.addTags(rTRC=2.2, gTRC=2.2, bTRC=2.2)
    if "kTRC" in kwargs:
        kwargs["kTRC"] = piecewise_trc(kwargs["kTRC"])
    prof.addTags(**kwargs)
    prof.write(out)


def piecewise_trc(ps):
    """Make a piecewise linear TRC (Tone Reproduction Curve) and
    return a function that implements it.
    The TRC is assumed to start at [0 0] and finish at [1 1];
    the list `ps` is a list [x1 y1 x2 y2 ... ] of intermediate
    points that the curve goes through. Note that the list is
    "flat", it consists of x- and y-coordinates alternating.
    The xs in the list of points (elements at even index) should
    be sorted (in increasing order).
    """

    ps = [0, 0] + ps + [1, 1]
    xs = [float(x) for x in ps[::2]]
    assert sorted(xs) == xs
    ys = [float(y) for y in ps[1::2]]

    def f(x):
        i = bisect.bisect_left(xs, x)
        if i == 0:
            return ys[0]
        e = x - xs[i - 1]
        # t is between 0 and 1, the fraction between adjacent nodes
        t = e / (xs[i] - xs[i - 1])
        return ys[i] * t + ys[i - 1] * (1 - t)

    return f


# for argparse argument type
def float_list(v):
    """Convert to list of float."""
    return [float(x) for x in v.split(",")]


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description=__doc__)
    # Defaults for colour primaries come from the
    # `sRGB Profile.icc` i found as a system colour profile on my mac.
    parser.add_argument(
        "--rXYZ",
        # default=(0.436, 0.222, 0.014),
        type=float_list,
        help="XYZ coordinate for red",
    )
    parser.add_argument(
        "--gXYZ",
        # default=(0.385, 0.717, 0.097),
        type=float_list,
        help="XYZ coordinate for green",
    )
    parser.add_argument(
        "--bXYZ",
        # default=(0.143, 0.061, 0.714),
        type=float_list,
        metavar="bXYZ",
        help="XYZ coordinate for blue",
    )
    parser.add_argument(
        "--kTRC",
        type=float_list,
        metavar="kTRC",
        help="Tone Reproduction Curve for gray",
    )
    args = parser.parse_args()

    d = vars(args)
    d = {k: v for k,v in d.items() if v is not None}
            
    icc_profile(png.binary_stdout(), **d)


if __name__ == "__main__":
    main()
