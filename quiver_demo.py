import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.axislines import SubplotZero
from matplotlib import colors

def cart2pol(x,y):
	rho = np.sqrt(x**2 + y**2)
	phi = np.arctan2(y, x)
	return[rho, phi]

def pol2cart(rho,phi):
	x = rho * np.cos(m.radians(90-phi))
	y = rho * np.sin(m.radians(90-phi))
	return[x, y]

hdeg = 0
odeg = 45
drift = odeg - hdeg
adeg = 115
aforce = .2

heading = pol2cart(1,hdeg)
orientation = pol2cart(1,odeg)
acceleration = pol2cart(aforce,adeg)

orig = [0,0]

h = orig + heading # normalized heading
x = orig + orientation # normalized orientation
g = orig + acceleration

print h,x,g

soa = np.array([h,x,g]) # vectors
print soa
X,Y,U,V = zip(*soa) # convert to turples of U and V components

fig = plt.figure(1)
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)
colors = ('r','g','b')
qv = ax.quiver(X,Y,U,V,color=colors,angles='xy',scale_units='xy',scale=1)

labels = ('heading: {} deg'.format(hdeg), 'Orientation, drift: {} deg'.format(drift), '{} g at {} deg'.format(aforce,adeg))
pos = ('N','E','S')
for x,y,l,c,p in zip(U,V,labels,colors,pos):
	plt.quiverkey(qv,x,y,0,l,color=c,coordinates='data',labelpos=p)

ax.set_xlim([-2,2])
ax.set_ylim([-2,2])

# show cartisian axis
# for direction in ["xzero", "yzero"]:
#     ax.axis[direction].set_visible(True)

# turn off side axis
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)

plt.draw()
plt.show()
