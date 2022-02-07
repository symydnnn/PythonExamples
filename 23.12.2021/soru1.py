
"""
SORU 1:
    
Bir a matrisinin tüm elemanları sıfır olan 
sütunlarının sayısını bulup bu bilgiyi geri döndüren Python 
fonksiyonunu yazınız.

"""

import numpy as np

def sifiribul(matris):
    print(matris)
    yeni = np.transpose(matris)
    sutun=0
    for i in yeni:
        say = 0
        for a in i:
            if a == 0:
                say =say+1
        if say ==len(matris):
            sutun = sutun+1
    if sutun != 0:
        print("Sıfır olan",sutun," adet sutun vardır")
    else:
        print("Tum sutunları sıfır olan eleman bulunmamaktadir")

matris = np.random.randint(2,size=(5,5))
sifiribul(matris)