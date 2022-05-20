import gencustompara as gencustompara

import traitementcustom as traitementcustom
import cleanerdosier as cleaner

from tqdm import tqdm
import matplotlib.pyplot as plt

def Magie(nposition=10, npositionprise = 7,\
          tballe = 20, parabolequation = [-0.01, 0, 100],\
          nbruit = 100, tbruit = 1, \
          tcarre = 100,niveaufiltre = 230):
          
    gencustompara.MAGIE(nposition, npositionprise,\
                        tballe, parabolequation,\
                        nbruit, tbruit)
    
    s = traitementcustom.MAGIE2(tcarre,niveaufiltre)
    cleaner.MAGIE3()
    return s

def faireexperience(lexperience):
    lcolor = ['r','g','b','c','m','y','k']
    xytotal = []
    for i in tqdm(range(len(lexperience))):
        s = Magie(npositionprise = 9, tcarre = lexperience[i])
        s2 = sorted(s)
        x,y = [f[0] for f in s2],[-f[1] for f in s2]
        xytotal.append([x,y])
    for i in range(len(xytotal)):
        print(len(xytotal))
        n = len(xytotal[i])
        plt.plot(xytotal[i][0], xytotal[i][1], lcolor[i], label=str(lexperience[i]))
    plt.legend()
    plt.show()
    print('Très bonne experience')

l = [1,2,5,10,20,50,100]
faireexperience(l)
