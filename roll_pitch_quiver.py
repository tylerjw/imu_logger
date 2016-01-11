import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.axislines import SubplotZero
from matplotlib import colors

roll = 15
pitch = 5

orig = [0,0]

X,Y = (0,0) # origin
U = roll
V = pitch

fig = plt.figure(1)
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)
qv = ax.quiver(X,Y,U,V,color='y',angles='xy',scale_units='xy',scale=1)

ax.set_xlim([-45,45])
ax.set_ylim([-45,45])

# show cartisian axis
for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_visible(True)

# turn off side axis
# for direction in ["left", "right", "bottom", "top"]:
#     ax.axis[direction].set_visible(False)

plt.draw()
plt.show()
