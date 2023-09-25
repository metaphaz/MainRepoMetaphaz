# #dictionary çok yararlı

# name = "Atlas"
# newuav = {
#     'uavinfo':{
#         "uavname":name,
#         "uavtype":"quad",
#         "uavpower":"lipo"
#     },
#     "uavnow":{
#         "lat": 75.5684626151,
#         "lon": 15.4684618181,
#         "airspd": 15.561,
#     }
# }
# newuav.update({"uavstatus":{"load":True}})

# sayilar = [1,3,5,7,9,12,19,21]
# a = input("Ürün sayısı:")
# a = int(a)
# urun = []
# while a>0:
#     ur= input("Ürün adı:")
#     price = input("Fiyat:")
#     urun.append({
#         'Name':ur,
#         'Price':int(price)
#     })
#     a-=1

# for n in urun:
#     print(f'Ürün adı: {n["Name"]} fiyat: {n["Price"]}')


#######################################################################################

# import random

# hak = 5

# hak = int(input("İstanilen hak sayısı:"))
# puansoru = 100/int(hak)

# sayi = random.randint(0,100)
# print(sayi)

# while hak>0:
#     tahmin = int(input("Tahminin ne?"))
#     if tahmin >= 100 or tahmin <0:
#         print("0 ile 100")
#         continue
#     if tahmin == sayi:
#         print(f"Tebrikler Doğru! {puansoru*hak} puan aldınız")
    
#     else:
#         hak-=1
#         if hak == 0:
#             print(f"Oyun bitti cevap {sayi} idi!")
#         else:
#             print(f"Yanlış cevap {hak} hakknız kaldı!")


# def myDict(**args):
#     print(type)
#     for n in args.items():
#         print(f"{n} ")

# myDict(name = "ygit",age = 16,yer = 'ist')

# def goster(kelime,defa):
#     for n in range(0,defa):
#         print(kelime)

# def listeyap(*params):
#     liste = [x for x in params]
#     print(liste)

# def asalmi(sayi):
#     if sayi == 1:
#         return False
#     for x in range(2,sayi):
#         if sayi%x==0:
#             return False
#     return True


# def asalBul(ilksayi,sonsayi):
#     asallar= [x for x in range(ilksayi,sonsayi+1) if asalmi(x)]
#     print(asallar)


# def bolenDondur(sayi):
#     liste = []
#     for x in range(1,sayi+1):
#         if sayi%x==0:
#             liste.append(x)
#     print(liste)


###########################################################################

HesapA = {
    "musteri":"Yiğit Özan",
    "hesapNo":"123456",
    "bakiye":5000,
    "nakitAvans":2500   
}

HesapB = {
    "musteri":"Özlem Özan",
    "hesapNo":"456789",
    "bakiye":9000,
    "nakitAvans":3500   
}

def paraCek(hesap,tutar):
    
    print(f"Hosşgendiniz {hesap['musteri']} ")
    if hesap["bakiye"]>=tutar:
        hesap["bakiye"]-= tutar
        print(f"İşlem başarılı! Kalan tutar: {hesap['bakiye']}")
    elif hesap["bakiye"] < tutar and (hesap["bakiye"] + hesap["nakitAvans"])>=tutar:
        print("Hesap bakiyesi yetersiz. Nakit avans kullanmak ister misniz? Evet için 1 Hayır için 0 tuşlayınız.")
        cevap = int(input())
        if cevap:
            kalan = tutar - hesap["bakiye"]
            hesap["bakiye"] = 0
            hesap["nakitAvans"]-=kalan
            print(f"İşlem başarılı! Kalan tutar: {hesap['bakiye']} ve borcunuz {kalan}")
        else:
            print("İşleminize devam edmiyoruz.")
    else:
        print("Bu tutarı çekmek için yeterli bakiyeniz veya nakit avansı hakknız yok!") 


paraCek(HesapB,5100)

    

