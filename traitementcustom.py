import matplotlib.image as mpimg
from matplotlib import pyplot as plt
import imageio as iio
import numpy as np
import os as os
from PIL import Image
from tqdm import tqdm
import Interpolation as interpolation

def convertjpgtomatrics(image0='imB.jpg'):
    img = iio.imread(image0)
    return img

def file_convert():
    L = []
    path1 = os.getcwd()
    
    listing = os.listdir(path1)

    for file in listing:
        if file[-3] != 'j':
            continue
        im = Image.open(path1 + '/' + file)
        x= convertjpgtomatrics(path1 + '/' + file)
        L.append(x)
    return L

def difference(L):
    L2 = []
    for i in range(len(L)-1):
       mvm = L[i]- L[i+1]
       L2.append(mvm)
    return L2


def transformationcarre(L):
    L3 = []
    for e in L:
        n = round(np.shape(e)[0],-2)
        eprime = e[0:n,0:n,1]
        L3.append(eprime)
    return L3

def traitement(L,alpha = 230):
    L2 = []
    for e in L:
        L3 = np.zeros(np.shape(e))
        for i in range(len(e)):
            for j in range(len(e[i])):
                if e[i,j] < alpha:
                    L3[i,j] = 0
                else:
                    L3[i,j] = 1
        L2.append(L3)
    return L2

##for e in L4:
##    plt.imshow(e)
##    plt.show()
##print(np.shape(L4))
def sumcarre(L, i, j, tcarre=100):

    iprime,jprime =(i+1)*tcarre+1, (j+1)*tcarre+1
    Lcarre = L[i*tcarre:iprime,j*tcarre:jprime]

    m  = 0
    for a in range(tcarre):
        for b in range(tcarre):
            m = m + Lcarre[a,b]
    return m

def decomposition(L,tcarre= 100):
    s = []
    for e in L:
        s1 = []
        n = np.shape(e)[0] // tcarre
        for i in range(n):
            for j in range(n):
                s2 = sumcarre(e, i, j, tcarre)
                s1.append((j*tcarre,i*tcarre,s2))
        s.append(s1)
    return s

def cherchemax(s): 
    smax = []
    for e in s:
        s1 = [-1,-1,-1]
        for f in e:
            if f[-1] > s1[-1]:
                s1 = f
        smax.append(s1)
    return smax

def trace(film):
    smax2 = sorted(film)
    
    x = [e[0] for e in film]
    y = [-e[1] for e in film]
    plt.plot(x,y, label='MOUVEMENT')
    plt.figure()
    plt.show()
    
##trace(smax)

def MAGIE2(tcarre = 25,niveaufiltre = 230):
    L = file_convert()

    L2 = difference(L)
    L3 = transformationcarre(L2)
    L4 = traitement(L3,niveaufiltre)
    s = decomposition(L4,tcarre)
    smax = cherchemax(s)
    smax2 = sorted(smax)
    return smax2

##smax2 = sorted(smax)    
##x = [e[0] for e in smax2]
##y = [e[1] for e in smax2]
##d = interpolation.distance(x, y, 1000)
##print(d)
