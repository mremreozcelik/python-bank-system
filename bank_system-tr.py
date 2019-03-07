# -*- coding: utf-8 -*-
"""
Github Project

@author: mremreozcelik
"""

######## TURKİSH LANGUAGE #########

para = int(0)
while True:
    print("Paranız : ", int(para) , " TL")
    print("1-) Para Yatır (1) \n2-) Para Çek (2) \n3-) Banka Durumum (3)")
    x = input("Yapmak istediğiniz işlemi giriniz ?\n")
    if x=="1":
        yatir = int(input("Kaç Para Yatırmak İstiyorsunuz ? (Örn: 25)\n"))
        para = int(para) + int(yatir)
        print("Tebrikler " , int(yatir) , " yatırdınız.")
        print("Başlangıca dönülüyor...")
    elif x =="2":
        cek = int(input("Kaç Para Çekmek İstiyorsunuz ? (Örn: 25)\n"))
        para = int(para) - int(cek)
        print("Tebrikler " , int(cek) , " çektiniz.")
        print("Başlangıca dönülüyor...")
    elif x=="3":
        print("Anlık Olarak Paranız :", int(+para) )        
    else:
        print("Hatalı Giriş Yaptınız !")