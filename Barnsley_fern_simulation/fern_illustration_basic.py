import numpy as np
import matplotlib.pyplot as plt 


def barnsley_fern(n):
    x = [0]
    y = [0]


    for _ in range(n):
        r = np.random.random()
        if r < 0.01 :
            x.append(0)
            y.append(0.16*y[-1])
        elif r < 0.86:
            x.append(0.85*x[-1]+0.04*y[-1])
            y.append(-0.04*x[-2]+0.85*y[-1]+1.6)
        elif r<0.93:
             x.append(0.23*x[-1]-0.26*y[-1])
             y.append(0.23*x[-2]+0.22*y[-1]+1.6)
        else:
            x.append(-0.15*x[-1]+0.28*y[-1])
            y.append(0.26*x[-2]+0.24*y[-1]+0.44)

    return x,y

n = 100000
x,y = barnsley_fern(n)
plt.figure(figsize = (6,10))
plt.scatter(x,y,s=0.2,color='green')
plt.axis('off')
plt.title("fern leaf pattern")
plt.show()