import random
import time

class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["Trt"],kanal="Trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tv_aç(self):
        if self.tv_durum=="Kapalı":
            print("Televizyon Açılıyor...")
            self.tv_durum="Açık"
        elif self.tv_durum== "Açık":
            print("Tv Zaten",self.tv_durum)

    def tv_kapat(self):
        if self.tv_durum=="Açık":
            print("Tv Kapanıyor...")
            self.tv_durum="Kapalı"
        elif self.tv_durum=="Kapalı":
            print("Tv Zaten",self.tv_durum)

    def ses_ayarları(self):
        while True:
            cevap= input("Sesi azalt:'<'\nSesi arttır:'>'\nÇıkış:'çıkış'")
            if cevap=="<" :
                if self.tv_ses!=0:
                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
            elif cevap==">":
                if self.tv_ses !=31 :
                    self.tv_ses +=1
                    print("Ses:",self.tv_ses)
            else:
                print("SES GÜNCELLENDİ:",self.tv_ses)
                break

    def kanal_ekle(self,kanal_isimi):
        print("Kanal Ekleniyor")
        time.sleep(1)
        self.kanal_listesi.append(kanal_isimi)
        print("Kanal Eklendi")

    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal= self.kanal_listesi[rastgele]
        print("Şu anki kanal:",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv Durumu:{}\nTv ses:{}\nKanal Listesi:{}\nŞu Anki Kanal:{}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
    
kumanda= Kumanda()

print("""

Televizyon Uygulaması

1.Tv aç

2.Tv kapat

3. Ses ayarları

4. Kanal Ekle

5.Kanal Sayısını Ögren

6.Rastgele Kanal Geçme

7.Televizyon Bilgileri

Çıkmak için '0' ya basın.

""")

while True:

    işlem=int(input("İşlemi Seçiniz:"))

    if işlem==0:
        print("Program Sonlandırılıyor...")
        break

    elif işlem==1:
        print("işlem1 girdi")
        kumanda.tv_aç()
    elif işlem==2:
        kumanda.tv_kapat()
    elif işlem==3:
        kumanda.ses_ayarları()
    elif işlem==4:
        kanal_isimleri=input("Eklemek istediğiniz kanalları ',' ile ayırarak girin:")

        kanal_listesi =kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif işlem==5:
        print("Kanal Sayısı:",len(kumanda))
    elif işlem==6:
        kumanda.rastgele_kanal()
    elif işlem==7:
        print(kumanda)

    else:
        print("Geçersiz işlem...")