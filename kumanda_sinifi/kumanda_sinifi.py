import random
import time

class Kumanda():
    def __init__(self,tv_durumu = "Kapali",tv_ses=0,kanal_listesi = ["TRT"],mevcut_kanal ="TRT"):
        print("Kumanda olusturuluyor...")
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.mevcut_kanal = mevcut_kanal

    def tv_ac(self):
            print("Televizyon Aciliyor...")

            self.tv_durumu = "Acik"
    def tv_kapa(self):
            print("Televizyon Kapaniyor...")

            self.tv_durumu = "Kapali"


    def ses_ayarlari(self):
        while True:
            cevap = input("Sesi Azalt:'<'\nSesi Arttir:'>'\nCikis İcin: exit")
            if (cevap == "<"):
                if(self.tv_ses !=0):
                    self.tv_ses -=1
                    print("Ses: ",self.tv_ses)
            elif (cevap == ">"):
                if(self.tv_ses < 32):
                    self.tv_ses +=1
                    print("Ses: ",self.tv_ses)
            else:
                print("Ses Güncellendi: ",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal Ekleniyor...")
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi...")

    def random_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi)-1)
        self.mevcut_kanal = self.kanal_listesi[rastgele]
        print("Şuanki Kanal: ",self.mevcut_kanal)


    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):
        return "TV Durumu: {}\nTV Ses: {}\nKanal Listesi: {}\nŞuanki Kanal: {}".format(self.tv_durumu,self.tv_ses,self.kanal_listesi,self.mevcut_kanal)
    


kumanda = Kumanda()



print("""
      
    1. Tv Aç
    
    2. Tv Kapa
      
    3. Ses Ayarlari
      
    4. Kanal Ekle
      
    5. Kanal Sayisini Oğren
      
    6. Rastgele Kanala Geç
      
    7. Televizyon Bilgileri

    8. Çikmak için '8'
      """)



while True:
    islem = (input("İslem Seciniz."))
    if (islem == "q"):
        print("İslem Sonlandiriliyor.")
        break
    
    if (islem == "1"):
        kumanda.tv_ac()
    elif (islem == "2"):
        kumanda.tv_kapa()
    elif(islem == "3"):
        kumanda.ses_ayarlari()
    elif(islem == "4"):
        kanal_isimleri = input("Kanal İsimlerini ',' ile ayirarak giriniz.")
        eklenecekler = kanal_isimleri.split(",")
        for i in eklenecekler:
            kumanda.kanal_ekle(i)
            print("Kanallar güncel")
    elif(islem =="5"):
        print("Kanal Sayisi: ",len(kumanda))
    elif(islem == "6"):
        kumanda.random_kanal()
    elif(islem == "7"):
        print(kumanda)

    else:
        print("Geçersiz İşlem")

