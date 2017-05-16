"""No linter no cry."""

import numpy
import pylab
import mahotas as mh

image1 = mh.imread('i1.jpg')
image2 = mh.imread('i2.jpg')
bcg1 = mh.imread('b1.jpg')
bcg2 = mh.imread('b2.jpg')

# TODO gauss does make pictures gray. why?
# p = 4
# image1 = mh.gaussian_filter(image1, p)
# image2 = mh.gaussian_filter(image2, p)
# bcg1 = mh.gaussian_filter(bcg1, p)
# bcg2 = mh.gaussian_filter(bcg2, p)

assert len(image1) == len(image2) == len(bcg1) == len(bcg2)
assert len(image1[0]) == len(image2[0]) == len(bcg1[0]) == len(bcg2[0])
numLines = len(image1)
numPixel = len(image1[0])

result = []
for line in range(0, numLines):
    result.append([])
    for pix in range(0, numPixel):
        i1 = image1[line][pix]
        i2 = image2[line][pix]
        b1 = bcg1[line][pix]
        b2 = bcg2[line][pix]
        bDiff = (b1 - b2) / 255
        if bDiff.dot(bDiff) != 0:
            alpha = 1 - (((i1 - i2) / 255).dot(bDiff) /
                         bDiff.dot(bDiff))
        else:
            alpha = 0

        alpha *= 255
        numpy.clip(alpha, 0, 255)

        # r = (i1[0].astype(numpy.uint16) + i2[0]) / 2
        # g = (i1[1].astype(numpy.uint16) + i2[1]) / 2
        # b = (i1[2].astype(numpy.uint16) + i2[2]) / 2
        r = i1[0]
        g = i1[1]
        b = i1[2]

        result[len(result) - 1].append((r, g, b, alpha))

result = numpy.array(result).astype(numpy.uint8)

# now write image to file (good to preview pic in atom editor):
mh.imsave('test.png', result)

# and plot with pylab
# pylab.imshow(result)
# pylab.gray()
# pylab.show()
