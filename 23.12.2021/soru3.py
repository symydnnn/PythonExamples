"""
SORU 3: 
    
Bir a matrisinin satırlarında yanyana iki adet 0 olup 
olmadığını arayan ve bu duruma uyan satır
adedini geri döndüren Python fonksiyonunu yazınız.
(Örneğin; a = [[0,0,0,0],[0,4,0,2],[1,0,5,8],[0,0,2,3]] 
 olarak verildiğinde, ilk ve son satırlarda yanyana
0 sayısı yer aldığı için fonksiyon 2 sonucunu döndürmelidir).
"""

import numpy as np

def yanyana(matris):
    print(matris)
    say = 0
    for i in matris:
        for a in range(len(i)-1):
            if i[a] == i[a+1]:
                if i[a] == 0:
                    say = say+1 
    print(say," adet var")
    
matris = np.random.randint(3,size=(5,5))
yanyana(matris)