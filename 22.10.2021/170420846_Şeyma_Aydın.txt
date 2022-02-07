
## 170420846 ŞEYMA AYDIN

## SORU 1


for a in range(1,5):
    print("A" * a, end="")
for b in range(3, 5):
    print("B" * b, end="")
for c in range(4,5):
    print("CD" * c, end="E")
for f in range(6,7):
    print("F" * f, end="G")


## SORU 2
sayac=0
dizi = []
say= int(input("kac eleman girilecek: "))
while sayac<say:
    d = input("girin: ")
    dizi.append(d)
    sayac+=1
for i in range(0 , say):
    print(dizi[i])

a= dizi[::-1]
if a[i] == dizi [i]:
    print("polindrom")
else:
    print("polindrom degil")



## SORU 3
import random
dizi = []
toplam=0
for i in range(1,21):
    dizi.append(random.randint(1,100))
for i in range(1,len(dizi)):
    toplam += dizi[i]

print("Dizi elemanlari: ", dizi)
print("Dizi ortalaması: ", toplam/20)
print("En büyük eleman: ", max(dizi))
print("En küçük eleman: ",min(dizi))
print("Cift sayilar: ")
for i in dizi:
    if i%2==0:
        print(i, end= " ")