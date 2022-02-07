
"""
SORU2: 
    
Terim katsayıları f ve g dizisinde tutulan iki polinomun çarpımını hesaplayan ve oluşacak 
sonuç polinomun terim katsayı listesini geri döndüren Python fonksiyonunu yazınız.

Örnek : f(x) = -4x2+2 ve g(x) = -x3-x2+3x+1 şeklinde olduğunu düşünelim. Bu durumda katsayı
listeleri şu şekildedir: f=[2,0,-4] , g=[1,3,-1,-1]. Yani listelerin 0. elemanı ilgili 
polinomun x0teriminin katsayısını, 1. elemanı x1 teriminin katsayısını vb. tutmaktadır. 
Bu iki polinomun çarpım
sonuç listesi = [2,6,-6,-14,4,4] şeklinde oluşur.

"""

def carpim(f, g, a, b):
    carp = [0] * (a + b - 1)
    for i in range(a):
        for j in range(b):
            carp[i+j] += f[i] * g[j]
    return carp

def yazdir(polinom, n):
    for i in range(n):
        if polinom[i] !=0:
            print(polinom[i], end = "")
            if i != 0:
                print("x^", i, end = "")
            if i != n - 1:
                if i>0:
                    print("+", end = "")

f = [2, 0, -4]
g = [1, 3, -1,-1]
m = len(f)
n = len(g)

print("Birinci polinom: ")
yazdir(f, m)
print("\nIkinci polinom: ")
yazdir(g, n)
sonuc_listesi = carpim(f, g, m, n)
print("\nSonuc listesi: ",sonuc_listesi)
