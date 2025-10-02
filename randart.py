import matplotlib.pyplot as plt
import random
def genArt(comp, size):
    xpoints = []
    ypoints = []
    for num in range(1, comp+1):
        x = random.randint(1, size+1)
        xpoints.append(x)
        y = random.randint(1, size+1)
        ypoints.append(y)
    plt.plot(xpoints, ypoints)
    plt.show()



