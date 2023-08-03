import matplotlib.pyplot as plt
import numpy as np
import a_star_module
from scipy import interpolate
import d_star_module
import dijkstra_module
import numpy as np

ox = np.load('lmnpx.npy')
oy = np.load('lmnpy.npy')

show_animation = True


sx = 0.4
sy = -2
gx = -1.6
gy = 1.7

grid_size = 0.15
robot_radius = 0.15

########################## A Star ##############################
    
if show_animation:
    plt.plot(ox, oy, ".k")
    plt.plot(sx, sy, "og")
    plt.plot(gx, gy, "xb")
    plt.grid(True)
    plt.axis("equal")

    
a_star = a_star_module.AStarPlanner(ox, oy, grid_size, robot_radius)
rx, ry = a_star.planning(sx, sy, gx, gy)


f, u = interpolate.splprep([rx, ry], s=1, per=False)
xint, yint = interpolate.splev(np.linspace(0, 1, 100), f)

plt.plot(xint, yint)
plt.show()

######################### Dijkstra #########################

if show_animation:  # pragma: no cover
    plt.plot(ox, oy, ".k")
    plt.plot(sx, sy, "og")
    plt.plot(gx, gy, "xb")
    plt.grid(True)
    plt.axis("equal")

dijkstra = dijkstra_module.Dijkstra(ox, oy, grid_size, robot_radius)
rx, ry = dijkstra.planning(sx, sy, gx, gy)

f, u = interpolate.splprep([rx, ry], s=1, per=False)
xint, yint = interpolate.splev(np.linspace(0, 1, 100), f)

plt.plot(xint, yint)
plt.show()

######################### D Star #########################

m = d_star_module.Map(100, 100)

n_ox, n_oy = ox, oy
ox, oy = [], []

for i in n_ox:
    ox.append(round(i*10)+52)
    
for i in n_oy:
    oy.append(round(i*10)+52)

m.set_obstacle([(i, j) for i, j in zip(ox, oy)])


sx = 57
sy = 32
gx = 33
gy = 66


if show_animation:
    plt.plot(ox, oy, ".k")
    plt.plot(sx, sy, "og")
    plt.plot(gx, gy, "xb")
    plt.axis("equal")

start = m.map[sx][sy]
end = m.map[gx][gy]

dstar = d_star_module.Dstar(m)
rx, ry = dstar.run(start, end)

if show_animation:
    plt.plot(rx, ry, "-r")
    plt.show()

np.save('rx.npy', rx)
np.save('ry.npy', ry)