
"""
SORU 4:
    
x – (x2/2!) + (x3/3!) – (x4/4!) + ... + (xn/n!) ifadesinin sonucunu parametre olarak gelen 
x ve n değerleri için hesaplayıp bu sonucu geri döndüren Python fonksiyonunu yazınız.
"""

def hesapla(x,n):
    deger =[]
    fktr = 1
    for i in range(n):
        for b in range(i):
            fktr = fktr * (b+1)
        if i % 2 == 0:
            deger.append(-(x**i)/fktr)
        else:
            deger.append((x**i)/fktr)
    sonuc = sum(deger)
    print(sonuc)

hesapla(3,4)