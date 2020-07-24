import sys
from math import sin, cos, radians
import numpy as np
import matplotlib.pyplot as plt

print("Hello, Visual Studio")

def make_dot_string(x):
    rad = radians(x)
    numspaces = int(20 * cos(radians(x)) + 20)
    st = ' ' * numspaces + 'o'
    return st

#for i in range(360):
#    print(cos(radians(i)))


#for i in range(0, 1800, 12):
#    s = make_dot_string(i)
#    print(s)



def main():
    #for i in range(0, 1800, 12):
    #    s = make_dot_string(i)
    #    print(s)
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()


main()