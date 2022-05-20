import turtle as tr
import numpy as np
from tk import *
from PIL import Image
import os as os

def bruit(nbruit = 100, tbruit = 1):
    l = [(1,1),(1,-1),(-1,1),(-1,-1)]
    for e in l:
        for i in range(nbruit):
            tr.up()
            tr.goto(e[0] * np.random.randint(400), e[1] * np.random.randint(400))
            tr.down()
            tr.begin_fill()
            tr.circle(tbruit)
            tr.end_fill()
        tr.up()
        tr.goto(0,0)
        tr.down()
    tr.ht()

def cercle(x=0, y=0, tballe = 20):
    tr.reset()
    tr.up()
    tr.goto(x,y)
    tr.down()
    tr.begin_fill()
    tr.circle(tballe)
    tr.end_fill()

def parabole(x, a=-0.01, b=0, c=10):
    return a * x**2 + b * x + c

def gen_x(n):
    x=np.linspace(-200,200,n)
    return x

def gen_y(x, a,b,c):
    return parabole(x, a,b,c)

def generate_pos(n, parabolequation = [-0.01, 0, 10]):
    x = gen_x(n)
    a, b, c = parabolequation[0], parabolequation[1], parabolequation[2]
    y = gen_y(x, a,b,c)
    return x,y

def trace(xi,yi, tballe, nbruit, tbruit):
    tr.tracer(0, 0)
    tr.ht()
    cercle(xi,yi+100, tballe)
    bruit(nbruit, tbruit)
    tr.update()

def register_para(nposition, npositionprise, tballe, parabolequation, nbruit, tbruit):
    L=[]
    x,y = generate_pos(nposition, parabolequation)
    for i in range(nposition):
        if i > npositionprise:
            break
        trace(x[i],y[i], tballe, nbruit, tbruit)
        s = tr.getscreen()
        L.append('para' + str(round(x[i],3)) + ',' + str(round(y[i],3)) + '.eps')
        tr.getcanvas().postscript(file='para' + str(round(x[i],3)) + ',' + str(round(y[i],3)) + '.eps')
    return L, s

def converteps_png(L):
    L1 = []
    for e in L:
        image_eps = e
        im = Image.open(image_eps)
        fig = im.convert('RGBA')
        image_png= str(e[:-4]) + '.png'
        fig.save(image_png, lossless = True)
        L1.append(image_png)
        cwd = os.getcwd()
        os.remove(cwd + '/' \
                    + image_eps)
    return L1

def convertpng_jpg(L):
    L2 = []
    for e in L:
        image_png = e
        img = Image.open(image_png)
        rgb_img = img.convert('RGB')
        image_jpg= str(e[:-4]) + '.jpg'
        rgb_img.save(image_jpg)
        L2.append(image_png)
        cwd = os.getcwd()
        os.remove(cwd + '/' \
                    + image_png)
    return L2
    
def MAGIE(nposition=10, npositionprise = 7,tballe = 20, parabolequation = [-0.01, 0, 100], nbruit = 100, tbruit = 1):
    tr.tracer(0, 0)
    Nom, L_eps = register_para(nposition, npositionprise,tballe, parabolequation, nbruit,tbruit)
    L_png = converteps_png(Nom)
    L_jpg = convertpng_jpg(L_png)
    return L_jpg

##MAGIE()
