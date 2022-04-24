


Hesaplar ={
    "usera":{
    "ad" : "Fatih Oğuzalp",
    "HesapNo":"13457895",
    "bakiye": 3000 ,
    "ekhesap":2000,
    },
    "userb":{
    "ad" : "Furkan Oğuzalp",
    "HesapNo":"12454895",
    "bakiye": 2000 ,
    "ekhesap":1000,    
    }
} 

x=input("Enter a user:")

def atm (x) :
    if x == "usera" :
        y=int(input("How much money do you want:"))
        if y<= Hesaplar["usera"]["bakiye"] :
            Hesaplar["usera"]["bakiye"]=Hesaplar["usera"]["bakiye"] - y 
            deger=Hesaplar["usera"]["bakiye"]
            print(f"Kalan bakiyeniz {deger}")
        else:
            m=input("Yeterli paranız yoktur,ek bakiyeden çekmek ister misiniz(Yes,No) ?")
            m=m.lower()
            if m=="yes" :
                while y > Hesaplar["usera"]["ekhesap"] + Hesaplar["usera"]["bakiye"] :
                    print("Hesabınızda yeterli para yok.")
                    break
                               
                while y < Hesaplar["usera"]["ekhesap"] + Hesaplar["usera"]["bakiye"] :
                    Hesaplar["usera"]["ekhesap"]=Hesaplar["usera"]["ekhesap"] - (y-3000)
                    deger=Hesaplar["usera"]["ekhesap"]
                    deger=Hesaplar["usera"]["ekhesap"]
                    print(f"Para çekme işleminiz başarıyla gerçekleşmitir.Kalan toplam bakiyeniz {deger}") 
            if m=="no" :
                print("Para çekme işleminiz iptal edilmiştir.")
    if x == "userb" :
        y=int(input("How much money do you want:"))
        if y<= Hesaplar["userb"]["bakiye"] :
            Hesaplar["userb"]["bakiye"]=Hesaplar["usera"]["bakiye"] - y 
            deger=Hesaplar["userb"]["bakiye"]
            print(f"Kalan bakiyeniz {deger}")
        else:
            m=input("Yeterli paranız yoktur,ek bakiyeden çekmek ister misiniz(Yes,No) ?")
            m=m.lower()
            if m=="yes" :
                while y > Hesaplar["userb"]["ekhesap"] + Hesaplar["userb"]["bakiye"] :
                    print("Hesabınızda yeterli para yok.")
                    break
                               
                while y < Hesaplar["userb"]["ekhesap"] + Hesaplar["userb"]["bakiye"] :
                    Hesaplar["userb"]["ekhesap"]=Hesaplar["userb"]["ekhesap"] - (y-2000)
                    deger=Hesaplar["userb"]["ekhesap"]
                    deger=Hesaplar["userb"]["ekhesap"]
                    print(f"Para çekme işleminiz başarıyla gerçekleşmitir.Kalan toplam bakiyeniz {deger}") 
            if m=="no" :
                print("Para çekme işleminiz iptal edilmiştir.")







atm(x)


