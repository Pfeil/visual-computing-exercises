"""No linter no cry."""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy

resolution = 10
a1 = 0.5
a2 = 1
ib = numpy.linspace(0, 1, resolution)
ig = numpy.linspace(0, 1, resolution)
ib, ig = numpy.meshgrid(ib, ig)
alpha = 1 - a1 * (ib - a2 * ig)

X = ib
Y = ig
Z = alpha

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d',
                     xlabel="blau", ylabel="gruen", zlabel="alpha")
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)
plt.show()
