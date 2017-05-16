"""No Linter no cry."""

import numpy
import pylab
import mahotas as mh

pic = mh.imread('bluescreen.jpg')

a1 = 1.7
a2 = 0
result = []
for line in pic:
    result.append([])
    for pix in line:
        r = pix[0]
        g = pix[1]
        b = pix[2]
        alpha = 255 - a1 * (b - a2 * g)
        if alpha < 10:
            alpha = 0
        numpy.clip(alpha, 0, 255)
        result[len(result) - 1].append((r, g, b, alpha))

result = numpy.array(result).astype(numpy.uint8)

# now write image to file (good to preview pic in atom editor):
mh.imsave('test.png', result)

# and / or plot with pylab
# pylab.imshow(result)
# pylab.gray()
# pylab.show()
