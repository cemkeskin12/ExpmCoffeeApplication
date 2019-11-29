import os


masalar = dict()
for i in range(1,11):
    masalar[i] = 0

def hesabaEkleme():
    masaNo = int(input("Masa No : "))
    gecerliHesap = masalar[masaNo]
    hesabaEklenecek = float(input("Eklenecek Fiyatı Giriniz : "))
    toplamEkle = gecerliHesap + hesabaEklenecek
    masalar[masaNo] = toplamEkle
    return toplamEkle
def hesaptanCikarma():
    masaNo = int(input("Masa No : "))
    gecerliHesap = masalar[masaNo]
    hesaptanCikarilacak = float(input("Çıkarılacak Fiyatı Giriniz : "))
    toplamCikar = gecerliHesap - hesaptanCikarilacak
    masalar[masaNo] = toplamCikar

def main():
    while True:
        os.system("clear")
        print("""
        [1] Masaları Görüntüle
        [2] Hesaba Ekleme Yap
        [3] Hesaptan Çıkar
        [Q] Çıkış
        """)
        secim = int(input("İşleminiz :"))

        if secim == 1:
            for i in range(1,11):
                print("Masa {} için hesap tutarı {} TL'dir".format(i,masalar[i]))
            print("İşlem Tamamlandı Ana Menü İçin 'Enter'e Basınız.")
            input()
        elif secim == 2:
            hesabaEkleme()
            print("İşlem Tamamlandı Ana Menü İçin 'Enter'e Basınız.")
            input()
        elif secim == 3:
            hesaptanCikarma()
            print("İşlem Tamamlandı Ana Menü İçin 'Enter'e Basınız.")
            input()
        elif secim == "q" or "Q":
            print("Çıkış Yapılıyor")
            quit()
main()
