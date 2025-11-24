import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def barnsley_fern_points(n):
    x = [0]
    y = [0]

    for _ in range(n):
        r = np.random.random()
        if r < 0.01:
            x.append(0)
            y.append(0.16 * y[-1])
        elif r < 0.86:
            x.append(0.85 * x[-1] + 0.04 * y[-1])
            y.append(-0.04 * x[-2] + 0.85 * y[-1] + 1.6)
        elif r < 0.93:
            x.append(0.23 * x[-1] - 0.26 * y[-1])
            y.append(0.23 * x[-2] + 0.22 * y[-1] + 1.6)
        else:
            x.append(-0.15 * x[-1] + 0.28 * y[-1])
            y.append(0.26 * x[-2] + 0.24 * y[-1] + 0.44)

    return np.array(x), np.array(y)

n = 30000
x, y = barnsley_fern_points(n)

fig, ax = plt.subplots(figsize=(6, 10), facecolor="black")
ax.set_facecolor("black")
ax.axis("off")
ax.set_title("Animated Barnsley Fern", color="white")


ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))


scatter = ax.scatter([], [], s=0.2, color="white")

def init():
    scatter.set_offsets(np.empty((0, 2))) 
    return scatter,

def update(frame):
    points = np.column_stack((x[:frame], y[:frame]))
    scatter.set_offsets(points)
    return scatter,

ani = FuncAnimation(
    fig,
    update,
    frames=range(0, n, 5),  
    init_func=init,
    blit=True,
    interval=1,
    repeat=False
)

plt.show()
