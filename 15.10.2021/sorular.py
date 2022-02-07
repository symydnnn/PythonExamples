

##satir = int(input("genislik degeri girin: "))
##sutun = int(input("yukseklik degeri girin: "))

##for yukseklik in range(sutun):
##    for genislik in range(satir):
##        print("*" if yukseklik in [0,sutun-1] or genislik in [0,satir-1] else " ", end=" ")
##    print()


## derece = int(input("Sıcaklik degerini giriniz: "))
## birim =input("Sıcaklik degerinin birimi; Celcius için C, Fahreneit için F seçimini yapınız: ")

## if birim =="F":
##    donusum= (derece*9/5)+32
##    print("{} Celcius ={} Fahreneit'e eşittir.".format(derece, donusum))
## elif birim=="C":
##    donusum= (derece*5/9)-32
##    print("{} Fahrenheit ={} Celcius'a eşittir.".format(derece, donusum))
## else:
##    print("Yanlis birim girdiniz.")


print("Soru: 1-2+3-4+...+199-200 seriyi bulan program \n")
ilk=1
son=200
for seri in range(ilk, son+1):
    print(seri if seri %2==1 else -seri, end=" ")
cevap= int(son*(son+1)/2)
print("\nCevap: ", cevap)

