import numpy as np
from matplotlib.pyplot import imshow, show, figure

def mandelbrot_i(imag, itercount = 50):
    z0 = imag
    z = imag
    for i in xrange(itercount):
        z = z**2 + z0
        if abs(z) > 2:
            break
    return i


def mandelbrot((xst, xen), (yst, yen), resolution=(1000, 1000), figure = figure()):
    xs = np.linspace(xst, xen, resolution[0])
    ys = np.linspace(yst, yen, resolution[1])

    f = np.zeros(resolution, dtype=np.int)
    for xidx, x in enumerate(xs):
        for yidx, y in enumerate(ys):
            f[yidx, xidx] = mandelbrot_i(np.complex(x, y))
    imshow(f, extent = (xst, xen, yst, yen), origin="lower")

mandelbrot((-2, 1), (-1.5, 1.5))
show()