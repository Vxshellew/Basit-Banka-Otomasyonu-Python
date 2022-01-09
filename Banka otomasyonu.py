banka = 'Bankaya Hoşgeldiniz'
print(banka)
list1 = ["Samet",2569075,100 ]
list2 = ["Murat",2101850,1500 ]
list3 = ["Oyku",210195,100000 ]
while True:
    isim = input('Ad ve Soyad Giriniz: ')
    Hesap = int(input('Hesap Numaranızı Giriniz: '))
    if Hesap == list1[1] and isim == list1[0]:
        print('Hesabınıza Giriş Yapılıyor...')
        print("""

        Online İşlemlere Hoşgeldiniz...

        (1) Bakiye Sorma
        (2) Para Çekme
        (3) Para Yatırma
        (q) Çıkış

        Not: İşlemler Bölümündeyken işleminiz bitince (4) Ana Sayfaya geri dönebilirsiniz..!
        """)

        while True:
            islem = input("Lütfen işlem seçiniz: ")
            if islem == "q":
                print("İyi Günler Dileriz..")
                break
            elif (islem == "1"):
                print("Mevcut Bakiye: {}".format(list1[2]))
                
            elif (islem == "2"):
                tutar = int(input("Ne kadar çekmek istiyorsunuz: "))
                
                if (list1[2] - tutar < 0):
                    print("Yetersiz bakiye...")
                    continue
                list1[2] -= tutar
                print('Yeni Bakiyeniz: {}'.format(list1[2]))
            elif (islem == "3"):
                tutar = int(input("Ne kadar para yatırmak istiyorsunuz: "))
                list1[2] = list1[2] + tutar
                print("Yeni bakiyeniz: {}".format(list1[2]))
            elif (islem == '4'):
                print("""

        Online İşlemlere Hoşgeldiniz...
        (1) Bakiye Sorma
        (2) Para Çekme
        (3) Para Yatırma
        (q) Çıkış""")
            else:
                print("Geçersiz işlem girdiniz..!")

        break
    elif Hesap ==  list2[1] and isim == list2[0]:
        print('Hesabınıza Giriş Yapılıyor...')
        print("""
    
        Online İşlemlere Hoşgeldiniz...

        (1) Bakiye Sorma
        (2) Para Çekme
        (3) Para Yatırma
        (q) Çıkış

        Not: İşlemler Bölümündeyken işleminiz bitince (4) Ana Sayfaya geri dönebilirsiniz..!
        """)

        while True:
            islem = input("Lütfen işlem seçiniz: ")
            if islem == "q":
                print("İyi Günler Dileriz..")
                break
            elif (islem == "1"):
                print("Mevcut Bakiye: {}".format(list2[2]))

            elif (islem == "2"):
                tutar = int(input("Ne kadar çekmek istiyorsunuz: "))
               
                if (list2[2] - tutar < 0):
                    print("Yetersiz bakiye...")
                    
                    continue
                list2[2] -= tutar
                print('Yeni Bakiyeniz: {}'.format(list2[2]))
            elif (islem == "3"):
                tutar = int(input("Ne kadar para yatırmak istiyorsunuz: "))
                list2[2] = list2[2] + tutar
                print("Yeni bakiyeniz: {}".format(list2[2]))
            elif (islem == '4'):
                print("""

        Online İşlemlere Hoşgeldiniz...
        (1) Bakiye Sorma
        (2) Para Çekme
        (3) Para Yatırma
        (q) Çıkış""")
            else:
                print("Geçersiz işlem girdiniz..!")

        break
    elif Hesap ==  list3[1] and isim == list3[0]:
        print('Hesabınıza Giriş Yapılıyor...')
        print("""

        Online İşlemlere Hoşgeldiniz...

        (1) Bakiye Sorma
        (2) Para Çekme
        (3) Para Yatırma
        (q) Çıkış

        Not: İşlemler Bölümündeyken işleminiz bitince (4) Ana Sayfaya geri dönebilirsiniz..!
        """)

        while True:
            islem = input("Lütfen işlem seçiniz: ")
            if islem == "q":
                print("İyi Günler Dileriz..")
                break
            elif (islem == "1"):
                print("Mevcut Bakiye: {}".format(list3[2]))

            elif (islem == "2"):
                tutar = int(input("Ne kadar çekmek istiyorsunuz: "))
                
                if (list3[2] - tutar < 0):
                    print("Yetersiz bakiye...")
                    continue
                list3[2] -= tutar
                print('Yeni Bakiyeniz: {}'.format(list3[2]))
            elif (islem == "3"):
                tutar = int(input("Ne kadar para yatırmak istiyorsunuz: "))
                list3[2] = list3[2] + tutar
                print("Yeni bakiyeniz: {}".format(list3[2]))
            elif (islem == '4'):
                print("""

        Online İşlemlere Hoşgeldiniz...
        (1) Bakiye Sorma
        (2) Para Çekme
        (3) Para Yatırma
        (q) Çıkış""")
            else:
                print("Geçersiz işlem girdiniz..!")

        break
    else:
        print('Yanlış Ad, Soyad veya  Hesap Numarası Girdiniz Tekrar Deneyiniz...')
        try:
            while False:
                isim = input('Ad ve Soyad Giriniz: ')
                Hesap = int(input('Hesap Numaranızı Giriniz: '))
                isim != list1[0] and isim != list2[0] and isim != list3[0]
                Hesap != list1[1] and Hesap != list2[1] and Hesap != list3[1]
                print('Hesabınıza Giriş Yapılıyor...')
        except ValueError:
            break