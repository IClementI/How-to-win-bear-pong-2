import os as os

def MAGIE3():
    
    path1 = os.getcwd()
    listing = os.listdir(path1)

    for file in listing:
        if file[-3] != 'j':
            continue
        os.remove(os.getcwd() + '/' \
        + file)
