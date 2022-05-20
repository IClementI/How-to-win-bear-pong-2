import numpy as np

def polynome(x,y):
    A = y[0] / (x[0] - x[1]) / (x[0] - x[2]) \
      + y[1] / (x[1] - x[0]) / (x[1] - x[2]) \
      + y[2] / (x[2] - x[0]) / (x[2] - x[1]) \

    B = y[0] * (x[1] + x[2]) / (x[0] - x[1]) / (x[0] - x[2]) \
      + y[1] * (x[0] + x[2]) / (x[1] - x[0]) / (x[1] - x[2]) \
      + y[2] * (x[0] + x[1]) / (x[2] - x[0]) / (x[2] - x[1]) \

    C = y[0] * (x[1] * x[2]) / (x[0] - x[1]) / (x[0] - x[2]) \
      + y[1] * (x[0] * x[2]) / (x[1] - x[0]) / (x[1] - x[2]) \
      + y[2] * (x[0] * x[1]) / (x[2] - x[0]) / (x[2] - x[1]) \

    A, B, C = round(A, 5), round(B, 2), round(C, 2)
    
    return [C, -B, A]

def distance(x, y, ytable):
    l = polynome(x,y)
    d = (l[1] + np.sqrt(l[1] ** 2 - 4 * l[2] * (l[0] - ytable))) / (2 * l[0])
    return d

##x = [1, 8, 3]

def poly(x, a=12, b=10.3, c=30):
    return a*(x)**2 + b*(x) + c

##y = [poly(e) for e in x]
##
##l = polynome(x,y)
##
##print(l)
