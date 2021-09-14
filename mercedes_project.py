###############################################
##  Company       - Mercedes-Benz Türk A.Ş.  ##
##  Developer     - Atalay URFALIOĞLU        ##
##  Product Name  - Lamba Montaj Konumları   ##
###############################################

print("              Mercedes-Benz Türk A.Ş.             ")
print("---------------------------------------------------------")

print(" ---!!!--- Kullanılmayacak veya Monte edilmeyecek ")
print(" koltuk mesafesine 0 değerini giriniz. ---!!!--- ")

print("---------------------------------------------------------")

model = input("Otobüsün modeli(15r,17r): ")


#/#/#/#/#/#/#/#/#/#/#/#/#/# 15R - Dar Kapı #/#/#/#/#/#/#/#/#/#/#/#/#/#/#

if model == ('15r'):

    tip = str(input("Kapı tipi(dar/geniş): "))

    if tip == ("dar"):

### Sol Sürücü
        print("SOL SÜRÜCÜ TARAFI LAMBA ÖLÇÜLERİ")
        print("---------------------------------------------------------")
        print("Sol Ön Kaplama Parçası")
        a = int(input("B-A1 Koltuk Mesafesi: "))
        b = int(193)
        c = int(142)
        toplam = a-b
        if toplam <= c:
            print("A1 Lamba Mesafesi: ",c)
            print("---------------------------")

        else:
            print("A1 Lamba Mesafesi: ",toplam)
            print("---------------------------")

        L2= int(input("A1-A2 Koltuk Mesafesi: "))

        if  toplam<=142:
            x = int(142)-toplam
            y = L2-x
            z = y+c
            print("---------------------------")
            print("A2 Lamba Mesafesi: ",L2)
            print("A2 Lamba Koordinatı: ",z)
            print("---------------------------")

            L3 = int(input("A2-A3 Koltuk Mesafesi: "))
            x3= L3+z
            print("---------------------------")
            print("A3 Lamba Mesafesi: ",L3)
            print("A3 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("A3-A4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("A4 Lamba Mesafesi: ",L4)
            print("A4 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("A4-A5 Koltuk Mesafesi: "))
            x5= L5+x4
            kl = 3841 - x5
            if kl <= 142:
                kc = 142-kl
                kv = L5-kc
                kf = x5+kv
                print("---------------------------")
                print("A5 Lamba Mesafesi: ", kf)
                print("A5 Koltuk Mesafesi : ", kv)
                print("---------------------------")
                
            if kl >= 142:
                print("---------------------------")
                print("A5 Lamba Mesafesi: ", L5)
                print("A5 Lamba Koordinatı: ", x5)
                print("---------------------------")
    
                print("---------------------------------------------------------")
            

        elif toplam>=142:
            x2=toplam+L2
            print("---------------------------")
            print("A2 Lamba Mesafesi: ",L2)
            print("A2 Lamba Koordinatı: ",x2)
            print("---------------------------")

            L3 = int(input("A2-A3 Koltuk Mesafesi: "))
            x3= L3+x2
            print("---------------------------")
            print("A3 Lamba Mesafesi: ",L3)
            print("A3 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("A3-A4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("A4 Lamba Mesafesi: ",L4)
            print("A4 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("A4-A5 Koltuk Mesafesi: "))
            x5= L5+x4
            kl = 3841 - x5
            if kl <= 142:
                kc = 142-kl
                kv = L5-kc
                kf = x5+kv
                print("---------------------------")
                print("A5 Lamba Mesafesi: ", kf)
                print("A5 Koltuk Mesafesi : ", kv)
                print("---------------------------")
                
            if kl >= 142:
                print("---------------------------")
                print("A5 Lamba Mesafesi: ", L5)
                print("A5 Lamba Koordinatı: ", x5)
                print("---------------------------")
                print("---------------------------------------------------------")

            koltuk = str(input("Orta Kapı Karşısında Koltuk(var/yok): "))
            if (koltuk == "yok"):
                
                print("---------------------------------------------------------")
                print("Sol Orta Kaplama Parçası")
                
                print("---------------------------")
                tp = int(input("A5 arkası boşluk: "))
                vp = int(input("Orta kapı boşluğu: "))
                bp = int(input("A6 önündeki boşluk: "))
                print("---------------------------")

                at = (tp + vp + bp) + x5
                rt = at - 5326
                

                print("---------------------------------------------------------")
                
                print("---------------------------") 
                print("A6 Lamba Mesafesi: ", rt)
                print("---------------------------")
                
                L8 = int(input("A6-A7 Koltuk Mesafesi: "))
                x8 = rt + L8
                print("---------------------------")
                print("A7 Lamba Mesafesi: ", L8)
                print("A7 Lamba Koordinatı: ", x8)
                print("---------------------------")

                L9 = int(input("A7-A8 Koltuk Mesafesi: "))
                x9 = x8 + L9
                print("---------------------------")
                print("A8 Lamba Mesafesi: ", L9)
                print("A8 Lamba Koordinatı: ", x9)
                print("---------------------------")

                L10 = int(input("A8-A9 Koltuk Mesafesi: "))
                x10 = x9 + L10
                print("---------------------------")
                print("A9 Lamba Mesafesi: ", L10)
                print("A9 Lamba Koordinatı: ", x10)
                print("---------------------------")

                if x10 >= 3481:
                    print("Kaplama limiti 3481mm olduğundan, bu kaplamaya",
                          "daha fazla servis seti koyamazsınız.")
                    print("Bir sonraki kaplamaya kadar olan değerlere 0 giriniz.")

                L11 = int(input("A9-A10 koltuk mesafesi: "))
                x11 = x10 + L11
                print("---------------------------")
                print("A10 Lamba Mesafesi: ", L11)
                print("A10 Lamba Koordinatı: ", x11)
                print("---------------------------")
                
                if x11 >= 3481:
                    print("Kaplama limiti 3481mm olduğundan, bu kaplamaya",
                          "daha fazla servis seti koyamazsınız.")
                    print("Bir sonraki kaplamaya kadar olan değerlere 0 giriniz.")
        
      
                
                print("---------------------------------------------------------")

            if (koltuk == "var"):
                L8 = int(input("A5-A6 Koltuk Mesafesi: "))
                a8 = L8 + sv
                c8 = a8 - 3481
                if c8 <= 142:
                    av = L8 + x7
                    c8 = av - 3481

                    print("---------------------------")
                    print("A6 Lamba Mesafesi: ", L8)
                    print("A6 Lamba Koodinatı: ", c8)
                    print("---------------------------")
                    L9 = int(input("A6-A7 Koltuk Mesafesi: "))
                    g8 = c8 + L9
                    print("---------------------------")
                    print("A7 Lamba Mesafesi: ", L9)
                    print("A7 Lamba Koordinatı: ", g8)
                    print("---------------------------")

                    print("---------------------------------------------------------")
                    print("3.Kaplamaya geçiniz.")
                    print("---------------------------------------------------------")

                    
                    L9c = int(input("A7-A8 Koltuk Mesafesi: "))

                    lp = av + L9
                    yp = lp + L9c
                    xp = yp - 5236

                    print("---------------------------")
                    print("A8 Lamba Mesafesi: ", xp)
                    print("---------------------------")

                    L10 = int(input("A8-A9 Koltuk Mesafesi: "))
                    x10 = xp + L10
                    print("---------------------------")
                    print("A9 Lamba Mesafesi: ", L10)
                    print("A9 Lamba Koordinatı: ", x10)
                    print("---------------------------")
                    
                    L11 = int(input("A9-A10 Koltuk Mesafesi: "))
                    x11 = x10 + L11
                    print("---------------------------")
                    print("A10 Lamba Mesafesi: ", L11)
                    print("A10 Lamba Koordinatı: ", x11)
                    print("---------------------------")
                            
                    L12 = int(input("A10-A11 Koltuk Mesafesi: "))
                    x12 = x11 + L12
                    print("---------------------------")
                    print("A11 Lamba Mesafesi: ", L12)
                    print("A11 Lamba Koordinatı: ", x12)
                    print("---------------------------")
                            
                    L13 = int(input("A11-A12 Koltuk Mesafesi: "))
                    x13 = x12 + L13
                    print("---------------------------")
                    print("A12 Lamba Mesafesi: ", L12)
                    print("A12 Lamba Koordinatı: ", x12)
                    print("---------------------------")

                    if x13 >= 3339:
                        ah = 3481 - x13
                        kh = 142 - ah
                        gh = L13 - kh
                        th = x13 + gh

                        print("---------------------------")
                        print("A13 Lamba Mesafesi: ", gh)
                        print("A13 Lamba Koordinatı: ", th)
                        print("---------------------------")

                    elif x13 <= 3339:
                        print("Kaplama limiti 3339mm olduğundan, bu kaplamaya",
                                 "daha fazla servis seti koyamazsınız.")
                        print("Bir sonraki kaplamaya kadar olan değerlere 0 giriniz.")

                   
                elif c8 >= 142:
                    print("---------------------------")
                    print("A8 Lamba Mesafesi: ", L8)
                    print("A8 Lamba Koordinatı: ", c8)
                    print("---------------------------")
                    L9 = int(input("A8-A9 Koltuk mesafesi:"))
                    g8 = c8 + L9
                    print("---------------------------")
                    print("A9 Lamba Mesafesi: ", L9)
                    print("A9 Lamba Koordinatı: ", z8)
                    print("---------------------------")
                    
                    print("---------------------------------------------------------")
                    print("3.Kaplamaya geçiniz.")
                    print("---------------------------------------------------------")


                    L9c = int(input("A9-A10 koltuk mesafesi: "))

                    lp = av + L9
                    yp = lp + L9c
                    xp = yp - 5326
                            
                    print("---------------------------")
                    print("A10 Lamba Mesafesi: ", L9c)
                    print("A10 Lamba Koordinatı: ", xp)
                    print("---------------------------")

                    L10 = int(input("A10-A11 koltuk mesafesi: "))
                    x10 = x9 + L10
                    print("---------------------------")
                    print("A11 Lamba Mesafesi: ", L10)
                    print("A11 Lamba Koordinatı: ", x10)
                    print("---------------------------")

                    L11 = int(input("A11-A12 koltuk mesafesi: "))
                    x11 = x10 + L11
                    print("---------------------------")
                    print("A12 Lamba Mesafesi: ", L11)
                    print("A12 Lamba Koordinatı: ", x11)
                    print("---------------------------")
                            
                    L12 = int(input("A12-A13 koltuk mesafesi: "))
                    x12 = x11 + L12
                    print("---------------------------")
                    print("A13 Lamba Mesafesi: ", L12)
                    print("A13 Lamba Koordinatı: ", x12)
                    print("---------------------------")
                            
                    L13 = int(input("A13-A14 koltuk mesafesi: "))
                    x13 = x12 + L13

                    if x13 >= 3339:
                        ah = 3481 - x13
                        kh = 142 - ah
                        gh = L13 - kh
                        th = x12 + gh

                        print("---------------------------")
                        print("A14 Lamba Mesafesi: ", gh)
                        print("A14 Lamba Koordinatı: ", th)
                        print("---------------------------")

                    elif x13 <= 3339:
                        print("Kaplama limiti 3339mm olduğundan, bu kaplamaya",
                                 "daha fazla servis seti koyamazsınız.")
                        print("Bir sonraki kaplamaya kadar olan değerlere 0 giriniz.")

                         
                    print("---------------------------------------------------------")

                     
          
### Sağ Kapı
        print("SAĞ KAPI TARAFI LAMBA ÖLÇÜLERİ")    
        c = int(input("B-D1 Koltuk Mesafesi: "))
        d = int(193)
        f = int(142)
        toplams = c-d
        if toplams <= f:
            print("---------------------------")
            print("D1 Lamba Mesafesi: ",f)
            print("---------------------------")

        else:
            print("---------------------------")
            print("D1 Lamba Mesafesi: ",toplams)
            print("---------------------------")
        
        L2 = int(input("D1-D2 Koltuk Mesafesi: "))

        if toplams<=142:
            x = int(142)-toplams
            y = L2-x
            z = y+f
            print("---------------------------")
            print("D2 Lamba Mesafesi: ",L2)
            print("D2 Lamba Koordinatı: ",z)
            print("---------------------------")

            L3 = int(input("D2-D3 Koltuk Mesafesi: "))
            x3 = L3+z
            print("---------------------------")
            print("D3 Lamba Mesafesi: ",L3)
            print("D3 Lamba Koordinatı: ",x3)
            print("---------------------------")

            if x3>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L4 = int(input("D3-D4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("D4 Lamba Mesafesi: ",L4)
            print("D4 Lamba Koordinatı: ",x4)
            print("---------------------------")

            if x4>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L5 = int(input("D4-D5 Koltuk Mesafesi: "))
            x5= L5+x4
            gt = 3841 - x5
            print("---------------------------")
            print("D5 Lamba Mesafesi: ",gt)
            print("D5 Lamba Koordinatı: ",x5)
            print("---------------------------")

            print("---------------------------------------------------------")
            de = int(input("D5 - rorta kapı mesafesi: "))
            dt = int(input("Orta Kapı mesafesi: "))
            ds = int(input("Orta kapı bitiminden D6 arası mesafesi: "))
            print("---------------------------------------------------------")
            
            ud = (de + dt + ds + x5) - 5326

                
            print("Orta Kapı Sonrası Koltuklardan Devam Ediniz.")
            print("---------------------------------------------------------")

            print("D6 lamba mesafesi: ", ud)

            m = int(input("D6-D7 Koltuk Mesafesi: "))
            
            jk = m + ud
                
            print("D7 Lamba Mesafesi: ", jk)

            L3 = int(input("D7-D8 Koltuk Mesafesi: "))
            x3 = jk+L3
            print("---------------------------")
            print("D8 Lamba Mesafesi: ",L3)
            print("D8 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("D8-D9 Koltuk Mesafesi: "))
            x4 = L4+x3
            print("---------------------------")
            print("D9 Lamba Mesafesi: ",L4)
            print("D9 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("D9-D10 Koltuk Mesafesi: "))
            x5 = L5+x4
            
            if x5 >= 3339:
                    ae = 3481 - x5
                    ke = 142 - ae
                    ge = L5 - ke
                    te = x4 + ge

                    print("---------------------------")
                    print("D10 Lamba Mesafesi: ", ge)
                    print("D10 Lamba Koordinatı: ", te)
                    print("---------------------------")

            elif x5 <= 3339:
                print("---------------------------")
                print("D10 Lamba Mesafesi: ", L5)
                print("D10 Lamba Koordinatı: ", x5)
                end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
                print("---------------------------")
                

            else:
                end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
                print("---------------------------------------------------------")

        elif toplams>=142:
            x2 = toplams+L2
            print("---------------------------")
            print("D2 Lamba Mesafesi: ", L2)
            print("D2 Lamba Koordinatı: ", x2)
            print("---------------------------")

            L3 = int(input("D2-D3 Koltuk Mesafesi: "))
            x3 = L3+x2
            print("---------------------------")
            print("D3 Lamba Mesafesi: ",L3)
            print("D3 Lamba Kesafesi: ",x3)
            print("---------------------------")

            if x3>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L4 = int(input("D3-D4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("D4 Lamba Mesafesi: ", L4)
            print("D4 Lamba Kesafesi: ", x4)
            print("---------------------------")

            if x4>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L5 = int(input("D4-D5 Koltuk Mesafesi: "))
            x5= L5+x4
            gt = 3841 - x5
            print("---------------------------")
            print("D5 Lamba Mesafesi: ", gt)
            print("D5 Lamba Koordinatı: ", x5)
            print("---------------------------")
                
            print("---------------------------------------------------------")
            de = int(input("D5 - orta kapı mesafesi: "))
            dt = int(input("Orta Kapı mesafesi: "))
            ds = int(input("Orta kapı bitiminden D6 arası mesafesi: "))
            ud = (de + dt + ds + x5) - 5326
           
            print("---------------------------------------------------------")
            print("Orta Kapı Sonrası Koltuklardan Devam Ediniz.")
            print("---------------------------------------------------------")

            print("D6 lamba mesafesi: ", ud)

            m = int(input("D6-D7 Koltuk Mesafesi: "))
            
            jk = m + ud
                
            print("D7 Lamba Mesafesi: ", jk)

            L3 = int(input("D7-D8 Koltuk Mesafesi: "))
            x3 = jk+L3
            print("---------------------------")
            print("D8 Lamba Mesafesi: ", L3)
            print("D8 Lamba Koordinatı: ", x3)
            print("---------------------------")

            L4 = int(input("D8-D9 Koltuk Mesafesi: "))
            x4 = L4+x3
            print("---------------------------")
            print("D9 Lamba Mesafesi: ", L4)
            print("D9 Lamba Koordinatı: ", x4)
            print("---------------------------")

            L5 = int(input("D9-D10 Koltuk Mesafesi: "))
            x5 = L5+x4
            
            if x5 >= 3339:
                    ae = 3481 - x5
                    ke = 142 - ae
                    ge = L5 - ke
                    te = x4 + ge

                    print("---------------------------")
                    print("D10 Lamba Mesafesi: ", ge)
                    print("D10 Lamba Koordinatı: ", te)
                    print("---------------------------")

            elif x5 <= 3339:
                print("D10 Lamba Mesafesi: ", L5)
                print("D10 Lamba Koordinatı: ", x5)
                print("---------------------------------------------------------")
                end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
                print("---------------------------------------------------------")

        else:
            print("---------------------------------------------------------")
            end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
            print("------------------------------------------------------")
                    


#/#/#/#/#/#/#/#/#/#/#/#/#/# 15R - Geniş Kapı #/#/#/#/#/#/#/#/#/#/#/#/#/#

    if tip == "geniş":

### Sol Sürücü
        print("SOL SÜRÜCÜ TARAFI LAMBA ÖLÇÜLERİ")
        print("---------------------------------------------------------")
        print("Sol Ön Kaplama Parçası")
        a = int(input("B-A1 Koltuk Mesafesi: "))
        b = int(193)
        c = int(142)
        toplam = a-b
        if toplam <= c:
            print("A1 Lamba Mesafesi: ",c)

        else:
            print("A1 Lamba Mesafesi: ",toplam)

        L2= int(input("A1-A2 Koltuk Mesafesi: "))

        if  toplam<=142:
            x = int(142)-toplam
            y = L2-x
            z = y+c
            print("---------------------------")
            print("A2 Lamba Mesafesi: ",L2)
            print("A2 Lamba Koordinatı: ",z)
            print("---------------------------")

            L3 = int(input("A2-A3 Koltuk Mesafesi: "))
            x3= L3+z
            print("---------------------------")
            print("A3 Lamba Mesafesi: ",L3)
            print("A3 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("A3-A4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("A4 Lamba Mesafesi: ",L4)
            print("A4 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("A4-A5 Koltuk Mesafesi: "))
            x5= L5+x4
            kl = 3841 - x5
            if kl <= 142:
                kc = 142-kl
                kv = L5-kc
                kf = x5+kv
                print("---------------------------")
                print("A5 Lamba Mesafesi: ", kf)
                print("A5 Koltuk Koordinatı: ", kv)
                print("---------------------------")
                
            if kl >= 142:
                print("---------------------------")
                print("A5 Lamba Mesafesi: ", L5)
                print("A5 Lamba Koordinatı: ", x5)
                print("---------------------------")
            

        elif toplam>=142:
            x2=toplam+L2
            print("---------------------------")
            print("A2 Lamba Mesafesi: ",L2)
            print("A2 Lamba Koordinatı: ",x2)
            print("---------------------------")

            L3 = int(input("A2-A3 Koltuk Mesafesi: "))
            x3= L3+x2
            print("---------------------------")
            print("A3 Lamba Mesafesi: ",L3)
            print("A3 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("A3-A4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("A4 Lamba Mesafesi: ",L4)
            print("A4 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("A4-A5 Koltuk Mesafesi: "))
            x5= L5+x4
            kl = 3841 - x5
            if kl <= 142:
                kc = 142-kl
                kv = L5-kc
                kf = x5+kv
                print("---------------------------")
                print("A5 Lamba Mesafesi: ", kf)
                print("A5 Koltuk mesafesi : ", kv)
                print("---------------------------")
                
            if kl >= 142:
                print("---------------------------")
                print("A5 Lamba Mesafesi: ", L5)
                print("A5 Lamba Koordinatı: ", x5)
                print("---------------------------")

            koltuk = str(input("Orta Kapı Karşısında Koltuk(var/yok): "))
            if (koltuk == "yok"):
                
                print("---------------------------------------------------------")
                print("Sol Orta Kaplama Parçası")

                tp = int(input("A5 arkası boşluk: "))
                vp = int(input("Orta kapı boşluğu: "))
                bp = int(input("A6 önündeki boşluk: "))

                at = (tp + vp + bp) + x5
                rt = at - 5326
                

                print("---------------------------------------------------------")
                
                 
                print("A6 Lamba mesafesi: ", rt)
                L8 = int(input("A6-A7 koltuk mesafesi: "))
                x8 = rt + L8
                print("---------------------------")
                print("A7 Lamba Mesafesi: ", L8)
                print("A7 Lamba Koordinatı: ", x8)
                print("---------------------------")

                L9 = int(input("A7-A8 koltuk mesafesi: "))
                x9 = x8 + L9
                print("---------------------------")
                print("A8 Lamba Mesafesi: ", L9)
                print("A8 Lamba Koordinatı: ", x9)
                print("---------------------------")

                L10 = int(input("A8-A9 koltuk mesafesi: "))
                x10 = x9 + L10
                print("---------------------------")
                print("A9 Lamba Mesafesi: ", L10)
                print("A9 Lamba Koordinatı: ", x10)
                print("---------------------------")

                if x10 >= 3481:
                    print("Kaplama limiti 3481mm olduğundan, bu kaplamaya",
                          "daha fazla servis seti koyamazsınız.")
                    print("Bir sonraki kaplamaya kadar olan değerlere 0 giriniz.")

                L11 = int(input("A9-A10 koltuk mesafesi: "))
                x11 = x10 + L11
                print("---------------------------")
                print("A10 Lamba Mesafesi: ", L11)
                print("A10 Lamba Koordinatı: ", x11)
                print("---------------------------")

                if x11 >= 3481:
                    print("Kaplama limiti 3481mm olduğundan, bu kaplamaya",
                          "daha fazla servis seti koyamazsınız.")
                    print("Bir sonraki kaplamaya kadar olan değerlere 0 giriniz.")
        
      
                
                print("---------------------------------------------------------")

            if (koltuk == "var"):
                L8 = int(input("A5-A6 Koltuk Mesafesi: "))
                a8 = L8 + sv
                c8 = a8 - 3481
                if c8 <= 142:
                    av = L8 + x7
                    c8 = av - 3481

                    print("---------------------------")
                    print("A6 Lamba Mesafesi: ", L8)
                    print("A6 Lamba Koordinatı: ", c8)
                    print("---------------------------")
                    L9 = int(input("A6-A7 Koltuk mesafesi: "))
                    g8 = c8 + L9
                    print("---------------------------")
                    print("A7 Lamba Mesafesi: ", L9)
                    print("A7 Lamba Koordinatı: ", g8)
                    print("---------------------------")

                    print("---------------------------------------------------------")
                    print("3.Kaplamaya geçiniz.")
                    print("---------------------------------------------------------")

                    
                    L9c = int(input("A7-A8 koltuk mesafesi: "))

                    lp = av + L9
                    yp = lp + L9c
                    xp = yp - 6236

                    print("---------------------------")        
                    print("A8 Lamba Mesafesi: ", L9c)
                    print("A8 Lamba Koordinatı: ", xp)
                    print("---------------------------")

                    L10 = int(input("A8-A9 koltuk mesafesi: "))
                    x10 = xp + L10
                    print("---------------------------")
                    print("A9 Lamba Mesafesi: ", L10)
                    print("A9 Lamba Koordinatı: ", x10)
                    print("---------------------------")

                    L11 = int(input("A9-A10 koltuk mesafesi: "))
                    x11 = x10 + L11
                    print("---------------------------")
                    print("A10 Lamba Mesafesi: ", L11)
                    print("A10 Lamba Koordinatı: ", x11)
                    print("---------------------------")
                            
                    L12 = int(input("A10-A11 koltuk mesafesi: "))
                    x12 = x11 + L12
                    print("---------------------------")
                    print("A11 Lamba Mesafesi: ", L12)
                    print("A11 Lamba Koordinatı: ", x12)
                    print("---------------------------")
                            
                    L13 = int(input("A11-A12 koltuk mesafesi: "))
                    x13 = x12 + L13
                    print("---------------------------")
                    print("A12 Lamba Mesafesi: ", L13)
                    print("A12 Lamba Koordinatı: ", x13)
                    print("---------------------------")

                    if x13 >= 3339:
                        ah = 3481 - x13
                        kh = 142 - ah
                        gh = L13 - kh
                        th = x13 + gh

                        print("---------------------------")
                        print("A13 Lamba Mesafesi: ", gh)
                        print("A13 Lamba Koordinatı: ", th)
                        print("---------------------------")

                    elif x13 <= 3339:
                        print("Kaplama limiti 3339mm olduğundan, bu kaplamaya",
                                 "daha fazla servis seti koyamazsınız.")
                        print("Bir sonraki kaplamaya kadar olan değerlere 0 giriniz.")
   

                elif c8 >= 142:
                    print("---------------------------")
                    print("A8 Lamba Mesafesi: ", L8)
                    print("A8 Lamba Koordinatı: ", c8)
                    print("---------------------------")
                    L9 = int(input("A8-A9 Koltuk mesafesi:"))
                    g8 = c8 + L9
                    print("---------------------------")
                    print("A9 Lamba Mesafesi: ", L9)
                    print("A9 Lamba Koordinatı: ", z8)
                    print("---------------------------")
                    
                    print("---------------------------------------------------------")
                    print("3.Kaplamaya geçiniz.")
                    print("---------------------------------------------------------")


                    L9c = int(input("A9-A10 koltuk mesafesi: "))

                    lp = av + L9
                    yp = lp + L9c
                    xp = yp - 6236

                    print("---------------------------")       
                    print("A10 Lamba Mesafesi: ", L9c)
                    print("A10 Lamba Koordinatı: ", xp)
                    print("---------------------------")

                    L10 = int(input("A10-A11 koltuk mesafesi: "))
                    x10 = x9 + L10
                    print("---------------------------")
                    print("A11 Lamba Mesafesi: ", L10)
                    print("A11 Lamba Koordinatı: ", x10)
                    print("---------------------------")

                    L11 = int(input("A11-A12 koltuk mesafesi: "))
                    x11 = x10 + L11
                    print("---------------------------")
                    print("A12 Lamba Mesafesi: ", L11)
                    print("A12 Lamba Koordinatı: ", x11)
                    print("---------------------------")
                            
                    L12 = int(input("A12-A13 koltuk mesafesi: "))
                    x12 = x11 + L12
                    print("---------------------------")
                    print("A13 Lamba Mesafesi: ", L12)
                    print("A13 Lamba Koordinatı: ", x12)
                    print("---------------------------")
                            
                    L13 = int(input("A13-A14 koltuk mesafesi: "))
                    x13 = x12 + L13

                    if x13 >= 3339:
                        ah = 3481 - x13
                        kh = 142 - ah
                        gh = L13 - kh
                        th = x12 + gh

                        print("---------------------------")
                        print("A14 lamba mesafesi: ", gh)
                        print("A14 lamba koordinatı: ", th)
                        print("---------------------------")

                    elif x13 <= 3339:
                        print("Kaplama limiti 3339mm olduğundan, bu kaplamaya",
                                 "daha fazla servis seti koyamazsınız.")
                        print("Bir sonraki kaplamaya kadar olan değerlere 0 giriniz.")

                        print("---------------------------------------------------------")

                     
          
### Sağ Kapı
        print("SAĞ KAPI TARAFI LAMBA ÖLÇÜLERİ")    
        c = int(input("B-D1 Koltuk Mesafesi: "))
        d = int(193)
        f = int(142)
        toplams = c-d
        if toplams <= f:
            print("D1 Lamba Mesafesi: ",f)

        else:
            print("D1 Lamba Mesafesi: ",toplams)
        
        L2 = int(input("D1-D2 Koltuk Mesafesi: "))

        if toplams<=142:
            x = int(142)-toplams
            y = L2-x
            z = y+f
            print("---------------------------")
            print("D2 Lamba Mesafesi: ",L2)
            print("D2 Lamba Kooridnatı: ",z)
            print("---------------------------")

            L3 = int(input("D2-D3 Koltuk Mesafesi: "))
            x3 = L3+z
            print("---------------------------")
            print("D3 Lamba Mesafesi: ",L3)
            print("D3 Lamba Kooridnatı: ",x3)
            print("---------------------------")

            if x3>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L4 = int(input("D3-D4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("D4 Lamba Mesafesi: ",L4)
            print("D4 Lamba Kooridnatı: ",x4)
            print("---------------------------")

            if x4>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L5 = int(input("D4-D5 Koltuk Mesafesi: "))
            x5= L5+x4
            gt = 3841 - x5
            print("---------------------------")
            print("D5 Lamba Mesafesi: ",gt)
            print("D5 Lamba Koordinatı: ",x5)
            print("---------------------------")

            print("---------------------------------------------------------")
            de = int(input("D5 - rorta kapı mesafesi: "))
            dt = int(input("Orta Kapı mesafesi: "))
            ds = int(input("Orta kapı bitiminden D6 arası mesafesi: "))
            print("---------------------------------------------------------")
            
            ud = (de + dt + ds + x5) - 5326

                
            print("Orta Kapı Sonrası Koltuklardan Devam Ediniz.")
            print("---------------------------------------------------------")

            print("D6 lamba mesafesi: ", ud)

            m = int(input("D6-D7 Koltuk Mesafesi: "))
            
            jk = m + ud
                
            print("D7 Lamba Mesafesi: ", jk)

            L3 = int(input("D7-D8 Koltuk Mesafesi: "))
            x3 = jk+L3
            print("---------------------------")
            print("D8 Lamba Mesafesi: ",L3)
            print("D8 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("D8-D9 Koltuk Mesafesi: "))
            x4 = L4+x3
            print("---------------------------")
            print("D9 Lamba Mesafesi: ",L4)
            print("D9 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("D9-D10 Koltuk Mesafesi: "))
            x5 = L5+x4
            
            if x5 >= 3339:
                    ae = 3481 - x5
                    ke = 142 - ae
                    ge = L5 - ke
                    te = x4 + ge

                    print("---------------------------")
                    print("D10 Lamba Mesafesi: ", ge)
                    print("D10 Lamba Koordinatı: ", te)
                    print("---------------------------")

            elif x5 <= 3339:
                print("---------------------------")
                print("D10 Lamba Mesafesi: ", L5)
                print("D10 Lamba Koordinatı: ", x5)
                end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
                print("---------------------------")
                

            else:
                end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
                print("---------------------------------------------------------")

        elif toplams>=142:
            x2 = toplams+L2
            print("---------------------------")
            print("D2 Lamba Mesafesi: ",L2)
            print("D2 Lamba Koordinatı: ",x2)
            print("---------------------------")

            L3 = int(input("D2-D3 Koltuk Mesafesi: "))
            x3 = L3+x2
            print("---------------------------")
            print("D3 Lamba Mesafesi: ",L3)
            print("D3 Lamba Koordinatı: ",x3)
            print("---------------------------")

            if x3>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L4 = int(input("D3-D4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("D4 Lamba Mesafesi: ",L4)
            print("D4 Lamba Koordinatı: ",x4)
            print("---------------------------")

            if x4>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L5 = int(input("D4-D5 Koltuk Mesafesi: "))
            x5= L5+x4
            gt = 3841 - x5
            print("---------------------------")
            print("D5 Lamba Mesafesi: ",gt)
            print("D5 Lamba Koordinatı: ",x5)
            print("---------------------------")
                
            print("---------------------------------------------------------")
            de = int(input("D5 - orta kapı mesafesi: "))
            dt = int(input("Orta Kapı mesafesi: "))
            ds = int(input("Orta kapı bitiminden D6 arası mesafesi: "))
            ud = (de + dt + ds + x5) - 5326
           
            print("---------------------------------------------------------")
            print("Orta Kapı Sonrası Koltuklardan Devam Ediniz.")
            print("---------------------------------------------------------")

            print("D6 lamba mesafesi: ", ud)

            m = int(input("D6-D7 Koltuk Mesafesi: "))
            
            jk = m + ud
                
            print("D7 Lamba Mesafesi: ", jk)

            L3 = int(input("D7-D8 Koltuk Mesafesi: "))
            x3 = jk+L3
            print("---------------------------")
            print("D8 Lamba Mesafesi: ",L3)
            print("D8 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("D8-D9 Koltuk Mesafesi: "))
            x4 = L4+x3
            print("---------------------------")
            print("D9 Lamba Mesafesi: ",L4)
            print("D9 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("D9-D10 Koltuk Mesafesi: "))
            x5 = L5+x4
            
            if x5 >= 3339:
                    ae = 3481 - x5
                    ke = 142 - ae
                    ge = L5 - ke
                    te = x4 + ge

                    print("---------------------------")
                    print("D10 Lamba Mesafesi: ", ge)
                    print("D10 Lamba Koordinatı: ", te)
                    print("---------------------------")

                    print("---------------------------------------------------------")
                    print("---------------------------------------------------------")

            elif x5 <= 3339:
                print("---------------------------")
                print("D10 Lamba Mesafesi: ", L5)
                print("D10 Lamba Koordinatı: ", x5)
                print("---------------------------")
                print("---------------------------------------------------------")
                end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
                print("---------------------------------------------------------")
                
        else:
            print("---------------------------------------------------------")
            end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
            print("---------------------------------------------------------")

#/#/#/#/#/#/#/#/#/#/#/#/#/# 17R - Dar Kapı #/#/#/#/#/#/#/#/#/#/#/#/#/#/#
    
if model == ('17r'):

    tip = str(input("Kapı tipi(dar/geniş): "))

    if tip == ("dar"):

### Sol Sürücü
        print("SOL SÜRÜCÜ TARAFI LAMBA ÖLÇÜLERİ")
        print("---------------------------------------------------------")
        print("Sol Ön Kaplama Parçası")
        a = int(input("B-A1 Koltuk Mesafesi: "))
        b = int(193)
        c = int(142)
        toplam = a-b
        if toplam <= c:
            print("A1 Lamba Mesafesi: ",c)

        else:
            print("A1 Lamba Mesafesi: ",toplam)

        L2= int(input("A1-A2 Koltuk Mesafesi: "))

        if  toplam<=142:
            x = int(142)-toplam
            y = L2-x
            z = y+c
            print("---------------------------")
            print("A2 Lamba Mesafesi: ",L2)
            print("A2 Lamba Koordinatı: ",z)
            print("---------------------------")

            L3 = int(input("A2-A3 Koltuk Mesafesi: "))
            x3= L3+z
            print("---------------------------")
            print("A3 Lamba Mesafesi: ",L3)
            print("A3 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("A3-A4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("A4 Lamba Mesafesi: ",L4)
            print("A4 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("A4-A5 Koltuk Mesafesi: "))
            x5= L5+x4
            print("---------------------------")
            print("A5 Lamba Mesafesi: ",L5)
            print("A5 Lamba Koordinatı: ",x5)
            print("---------------------------")

            L6 = int(input("A5-A6 Koltuk Mesafesi: "))
            x6= L6+x5
            print("---------------------------")
            print("A6 Lamba Mesafesi: ",L6)
            print("A6 Lamba Koordinatı: ",x6)
            print("---------------------------")

            L7 = int(input("A6-A7 Koltuk Mesafesi: "))
            x7= L7+x6
            print("---------------------------")
            print("A7 Lamba Mesafesi: ",L7)
            print("A7 Lamba Koordinatı: ",x7)
            print("---------------------------")

            if x7 == 4751:
                print("Sol Ön Kaplama Limiti 4751mm.")

        elif toplam>=142:
            x2=toplam+L2
            print("---------------------------")
            print("A2 Lamba Mesafesi: ",L2)
            print("A2 Lamba Koordinatı: ",x2)
            print("---------------------------")

            L3 = int(input("A2-A3 Koltuk Mesafesi: "))
            x3= L3+x2
            print("---------------------------")
            print("A3 Lamba Mesafesi: ",L3)
            print("A3 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("A3-A4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("A4 Lamba Mesafesi: ",L4)
            print("A4 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("A4-A5 Koltuk Mesafesi: "))
            x5= L5+x4
            print("---------------------------")
            print("A5 Lamba Mesafesi: ",L5)
            print("A5 Lamba Koordinatı: ",x5)
            print("---------------------------")

            L6 = int(input("A5-A6 Koltuk Mesafesi: "))
            x6= L6+x5
            print("---------------------------")
            print("A6 Lamba Mesafesi: ",L6)
            print("A6 Lamba Koordinatı: ",x6)
            print("---------------------------")

            L7 = int(input("A6-A7 Koltuk Mesafesi: "))
            x7= L7+x6

            st = 4751 - x7
            if st <= 142:
                sc = 142-st
                sv = L7-sc
                sf = x6+sv
                print("---------------------------")
                print("A7 Lamba Mesafesi: ", sf)
                print("A7 Koltuk Mesafesi : ", sv)
                print("---------------------------")
                
            if st >= 142:
                print("---------------------------")
                print("A7 Lamba Mesafesi: ", L7)
                print("A7 Lamba Koordinatı: ", x7)
                print("---------------------------")

            koltuk = str(input("Orta Kapı Karşısında Koltuk(var/yok): "))
            if (koltuk == "yok"):
                
                print("---------------------------------------------------------")
                print("Sol Orta Kaplama Parçası")

                tp = int(input("A7 arkası boşluk: "))
                vp = int(input("Orta kapı boşluğu: "))
                bp = int(input("A8 önündeki boşluk: "))

                at = (tp + vp + bp) + sf
                rt = at - 6236
                

                print("---------------------------------------------------------")
                
                print("---------------------------")
                print("A8 Lamba Mesafesi: ", rt)
                print("---------------------------")
                L8 = int(input("A8-A9 koltuk mesafesi: "))
                x8 = rt + L8
                print("---------------------------")
                print("A9 Lamba Mesafesi: ", L8)
                print("A9 Lamba Koordinatı: ", x8)
                print("---------------------------")

                L9 = int(input("A9-A10 koltuk mesafesi: "))
                x9 = x8 + L9
                print("---------------------------")
                print("A10 Lamba Mesafesi: ", L9)
                print("A10 Lamba Koordinatı: ", x9)
                print("---------------------------")

                L10 = int(input("A10-A11 koltuk mesafesi: "))
                x10 = x9 + L10
                print("---------------------------")
                print("A11 Lamba Mesafesi: ", L10)
                print("A11 Lamba Koordinatı: ", x10)
                print("---------------------------")

                L11 = int(input("A11-A12 koltuk mesafesi: "))
                x11 = x10 + L11
                
                if x11 >= 3481:
                    print("Kaplama limiti 3481mm olduğundan, bu kaplamaya",
                          "daha fazla servis seti koyamazsınız.")
                    print("Bir sonraki kaplamaya kadar olan değerlere 0 giriniz.")

                elif x <= 3481:
                    L12 = int(input("A12-A13 koltuk mesafesi: "))
                    x12 = x11 + L12
                    print("---------------------------")
                    print("A13 Lamba Mesafesi: ", L12)
                    print("A13 Lamba Koordinatı: ", x12)
                    print("---------------------------")
        
      
                print("---------------------------------------------------------")

            if (koltuk == "var"):
                L8 = int(input("A7-A8 Koltuk Mesafesi: "))
                a8 = L8 + sv
                c8 = a8 - 4751
                if c8 <= 142:
                    av = L8 + x7
                    c8 = av - 4751

                    print("---------------------------")
                    print("A8 Lamba Mesafesi: ", L8)
                    print("A8 Lamba Koordinatı: ", c8)
                    print("---------------------------")
                    
                    L9 = int(input("A8-A9 Koltuk mesafesi: "))
                    g8 = c8 + L9
                    print("---------------------------")
                    print("A9 Lamba Mesafesi: ", L8)
                    print("A9 Lamba Koordinatı: ", g8)
                    print("---------------------------")

                    print("---------------------------------------------------------")
                    print("3.Kaplamaya geçiniz.")
                    print("---------------------------------------------------------")

                    
                    L9c = int(input("A9-A10 koltuk mesafesi: "))

                    lp = av + L9
                    yp = lp + L9c
                    xp = yp - 6236

                    print("---------------------------")        
                    print("A10 Lamba Mesafesi: ", L9c)
                    print("A10 Lamba Koordinatı: ", xp)
                    print("---------------------------")

                    L10 = int(input("A10-A11 koltuk mesafesi: "))
                    x10 = xp + L10
                    print("---------------------------")
                    print("A11 Lamba Mesafesi: ", L10)
                    print("A11 Lamba Koordinatı: ", x10)
                    print("---------------------------")

                    L11 = int(input("A11-A12 koltuk mesafesi: "))
                    x11 = x10 + L11
                    print("---------------------------")
                    print("A12 Lamba Mesafesi: ", L11)
                    print("A12 Lamba Koordinatı: ", x11)
                    print("---------------------------")
                            
                    L12 = int(input("A12-A13 koltuk mesafesi: "))
                    x12 = x11 + L12
                    print("---------------------------")
                    print("A13 Lamba Mesafesi: ", L12)
                    print("A13 Lamba Koordinatı: ", x12)
                    print("---------------------------")
                            
                    L13 = int(input("A13-A14 koltuk mesafesi: "))
                    x13 = x12 + L13

                    if x13 >= 3339:
                        ah = 3481 - x13
                        kh = 142 - ah
                        gh = L13 - kh
                        th = x12 + gh

                        print("---------------------------")
                        print("A14 Lamba Mesafesi: ", gh)
                        print("A14 Lamba Koordinatı: ", th)
                        print("---------------------------")

                    elif x13 <= 3339:
                        print("Kaplama limiti 3339mm olduğundan, bu kaplamaya",
                                 "daha fazla servis seti koyamazsınız.")
                        print("Bir sonraki kaplamaya kadar olan değerlere 0 giriniz.")

                   
                        

                elif c8 >= 142:
                    print("---------------------------")
                    print("A8 Lamba Mesafesi: ", L8)
                    print("A8 Lamba Koordinatı: ", c8)
                    print("---------------------------")
                    
                    L9 = int(input("A8-A9 Koltuk mesafesi:"))
                    g8 = c8 + L9
                    print("---------------------------")
                    print("A9 Lamba Mesafesi: ", L9)
                    print("A9 Lamba Koordinatı: ", z8)
                    print("---------------------------")
                    
                    print("---------------------------------------------------------")
                    print("3.Kaplamaya geçiniz.")
                    print("---------------------------------------------------------")


                    L9c = int(input("A9-A10 koltuk mesafesi: "))

                    lp = av + L9
                    yp = lp + L9c
                    xp = yp - 6236

                    print("---------------------------")
                    print("A10 Lamba Mesafesi: ", L9c)
                    print("A10 Lamba Koordinatı: ", xp)
                    print("---------------------------")

                    L10 = int(input("A10-A11 koltuk mesafesi: "))
                    x10 = x9 + L10
                    print("---------------------------")
                    print("A11 Lamba Mesafesi: ", L10)
                    print("A11 Lamba Koordinatı: ", x10)
                    print("---------------------------")

                    L11 = int(input("A11-A12 koltuk mesafesi: "))
                    x11 = x10 + L11
                    print("---------------------------")
                    print("A12 Lamba Mesafesi: ", L11)
                    print("A12 Lamba Koordinatı: ", x11)
                    print("---------------------------")
                            
                    L12 = int(input("A12-A13 koltuk mesafesi: "))
                    x12 = x11 + L12
                    print("---------------------------")
                    print("A13 Lamba Mesafesi: ", L12)
                    print("A13 Lamba Koordinatı: ", x12)
                    print("---------------------------")
                            
                    L13 = int(input("A13-A14 koltuk mesafesi: "))
                    x13 = x12 + L13

                    if x13 >= 3339:
                        ah = 3481 - x13
                        kh = 142 - ah
                        gh = L13 - kh
                        th = x12 + gh

                        print("---------------------------")
                        print("A14 Lamba Mesafesi: ", gh)
                        print("A14 Lamba Koordinatı: ", th)
                        print("---------------------------")

                    elif x13 <= 3339:
                        print("Kaplama limiti 3339mm olduğundan, bu kaplamaya",
                                 "daha fazla servis seti koyamazsınız.")
                        print("Bir sonraki kaplamaya kadar olan değerlere 0 giriniz.")

                         
                    print("---------------------------------------------------------")

                     
          
### Sağ Kapı
        print("SAĞ KAPI TARAFI LAMBA ÖLÇÜLERİ")    
        c = int(input("B-D1 Koltuk Mesafesi: "))
        d = int(193)
        f = int(142)
        toplams = c-d
        if toplams <= f:
            print("D1 Lamba Mesafesi: ",f)

        else:
            print("D1 Lamba Mesafesi: ",toplams)
        
        L2 = int(input("D1-D2 Koltuk Mesafesi: "))

        if toplams<=142:
            x = int(142)-toplams
            y = L2-x
            z = y+f
            print("---------------------------")
            print("D2 Lamba Mesafesi: ",L2)
            print("D2 Lamba Koordinatı: ",z)
            print("---------------------------")

            L3 = int(input("D2-D3 Koltuk Mesafesi: "))
            x3 = L3+z
            print("---------------------------")
            print("D3 Lamba Mesafesi: ",L3)
            print("D3 Lamba Koordinatı: ",x3)
            print("---------------------------")


            L4 = int(input("D3-D4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("D4 Lamba Mesafesi: ",L4)
            print("D4 Lamba Koordinatı: ",x4)
            print("---------------------------")


            L5 = int(input("D4-D5 Koltuk Mesafesi: "))
            x5= L5+x4
            print("---------------------------")
            print("D5 Lamba Mesafesi: ",L5)
            print("D5 Lamba Koordinatı: ",x5)
            print("---------------------------")

            L6 = int(input("D5-D6 Koltuk Mesafesi: "))
            x6= L6+x5
            print("---------------------------")
            print("D6 Lamba Mesafesi: ",L6)
            print("D6 Lamba Koordinatı: ",x6)
            print("---------------------------")

            if x6>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L7 = int(input("D6-D7 Koltuk Mesafesi: "))
            x7= L7+x6
            print("---------------------------")
            print("D7 Lamba Mesafesi: ",L7)
            print("D7 Lamba Koordinatı: ",x7)
            print("---------------------------")
            
            if x7>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L8 = int(input("D6-D7 Koltuk Mesafesi: "))
            x8= L8+x7
            gt = x8 - 4751
            print("---------------------------")
            print("D8 Lamba Mesafesi: ",L8)
            print("D8 Lamba Koordinatı: ",gt)
            print("---------------------------")
            


            print("---------------------------------------------------------")
            de = int(input("D7 - D8 arası mesafe: "))
            dt = int(input("Orta Kapı mesafesi: "))
            ds = int(input("Orta kapı bitiminden D9 arası mesafesi: "))
            print("---------------------------------------------------------")
            
            ud = (de + dt + ds + x7) - 6236

                
            print("Orta Kapı Sonrası Koltuklardan Devam Ediniz.")
            print("---------------------------------------------------------")

            print("D9 lamba mesafesi: ", ud)

            m = int(input("D9-D10 Koltuk Mesafesi: "))
            
            jk = m + ud
                
            print("D10 Lamba Mesafesi: ", jk)

            L3 = int(input("D10-D11 Koltuk Mesafesi: "))
            x3 = jk+L3
            print("---------------------------")
            print("D11 Lamba Mesafesi: ",L3)
            print("D11 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("D11-D12 Koltuk Mesafesi: "))
            x4 = L4+x3
            print("---------------------------")
            print("D12 Lamba Mesafesi: ",L4)
            print("D12 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("D12-D13 Koltuk Mesafesi: "))
            x5 = L5+x4
            
            if x5 >= 3339:
                    ae = 3481 - x5
                    ke = 142 - ae
                    ge = L5 - ke
                    te = x4 + ge

                    print("---------------------------")
                    print("D13 Lamba Mesafesi: ", ge)
                    print("D13 Lamba Koordinatı: ", te)
                    print("---------------------------")

            elif x5 <= 3339:
                print("---------------------------")
                print("D13 Lamba Mesafesi: ", L5)
                print("D13 Lamba Mesafesi: ", x5)
                end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
                print("---------------------------")
                
                
            else:
                end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
                print("---------------------------------------------------------")

        elif toplams>=142:
            x2 = toplams+L2
            print("---------------------------")
            print("D2 Lamba Mesafesi: ",L2)
            print("D2 Lamba Koordinatı: ",x2)
            print("---------------------------")

            L3 = int(input("D2-D3 Koltuk Mesafesi: "))
            x3 = L3+x2
            print("---------------------------")
            print("D3 Lamba Mesafesi: ",L3)
            print("D3 Lamba Koordinatı: ",x3)
            print("---------------------------")

            if x3>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L4 = int(input("D3-D4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("D4 Lamba Mesafesi: ",L4)
            print("D4 Lamba Koordinatı: ",x4)
            print("---------------------------")

            if x4>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L5 = int(input("D4-D5 Koltuk Mesafesi: "))
            x5= L5+x4
            print("---------------------------")
            print("D5 Lamba Mesafesi: ",L5)
            print("D5 Lamba Koordinatı: ",x5)
            print("---------------------------")

            if x5>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L6 = int(input("D5-D6 Koltuk Mesafesi: "))
            x6= L6+x5
            print("---------------------------")
            print("D6 Lamba Mesafesi: ",L6)
            print("D6 Lamba Koordinatı: ",x6)
            print("---------------------------")

            if x6>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L7 = int(input("D6-D7 Koltuk Mesafesi: "))
            x7= L7+x6
            print("---------------------------")
            print("D7 Lamba Mesafesi: ",L7)
            print("D7 Lamba Koordinatı: ",x7)
            print("---------------------------")

            if x7>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L8 = int(input("D6-D7 Koltuk Mesafesi: "))
            x8= L8+x7
            gt = x8 - 4751
            print("---------------------------")
            print("D8 Lamba Mesafesi: ",L8)
            print("D8 Lamba Koordinatı: ",gt)
            print("---------------------------")
                
            print("---------------------------------------------------------")
            de = int(input("D7 - D8 arası mesafe: "))
            dt = int(input("Orta Kapı mesafesi: "))
            ds = int(input("Orta kapı bitiminden D9 arası mesafesi: "))
            ud = (de + dt + ds + x7) - 6236
           
            print("---------------------------------------------------------")
            print("Orta Kapı Sonrası Koltuklardan Devam Ediniz.")
            print("---------------------------------------------------------")

            print("D9 lamba mesafesi: ", ud)

            m = int(input("D9-D10 Koltuk Mesafesi: "))
            
            jk = m + ud
                
            print("D10 Lamba Mesafesi: ", jk)

            L3 = int(input("D10-D11 Koltuk Mesafesi: "))
            x3 = jk+L3
            print("---------------------------")
            print("D11 Lamba Mesafesi: ",L3)
            print("D11 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("D11-D12 Koltuk Mesafesi: "))
            x4 = L4+x3
            print("---------------------------")
            print("D12 Lamba Mesafesi: ",L4)
            print("D12 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("D12-D13 Koltuk Mesafesi: "))
            x5 = L5+x4
            
            if x5 >= 3339:
                    ae = 3481 - x5
                    ke = 142 - ae
                    ge = L5 - ke
                    te = x4 + ge

                    print("---------------------------")
                    print("D13 Lamba Mesafesi: ", ge)
                    print("D13 Lamba Koordinatı: ", te)
                    print("---------------------------")

            elif x5 <= 3339:
                print("---------------------------")
                print("D13 Lamba Mesafesi: ", L5)
                print("D13 Lamba Koordinatı: ", x5)
                print("---------------------------")
                print("---------------------------------------------------------")
                end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
                print("---------------------------------------------------------")

    
        else:
            print("---------------------------------------------------------")
            end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
            print("---------------------------------------------------------")
            

#/#/#/#/#/#/#/#/#/#/#/#/#/# 17R - Geniş Kapı #/#/#/#/#/#/#/#/#/#/#/#/#/#/#
   
    if tip == "geniş":
        
### Sol Sürücü
        print("SOL SÜRÜCÜ TARAFI LAMBA ÖLÇÜLERİ")
        print("---------------------------------------------------------")
        print("Sol Ön Kaplama Parçası")
        a = int(input("B-A1 Koltuk Mesafesi: "))
        b = int(193)
        c = int(142)
        toplam = a-b
        if toplam <= c:
            print("A1 Lamba Mesafesi: ",c)

        else:
            print("A1 Lamba Mesafesi: ",toplam)

        L2= int(input("A1-A2 Koltuk Mesafesi: "))

        if  toplam<=142:
            x = int(142)-toplam
            y = L2-x
            z = y+c
            print("---------------------------")
            print("A2 Lamba Mesafesi: ",L2)
            print("A2 Lamba Koordinatı: ",z)
            print("---------------------------")

            L3 = int(input("A2-A3 Koltuk Mesafesi: "))
            x3= L3+z
            print("---------------------------")
            print("A3 Lamba Mesafesi: ",L3)
            print("A3 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("A3-A4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("A4 Lamba Mesafesi: ",L4)
            print("A4 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("A4-A5 Koltuk Mesafesi: "))
            x5= L5+x4
            print("---------------------------")
            print("A5 Lamba Mesafesi: ",L5)
            print("A5 Lamba Koordinatı: ",x5)
            print("---------------------------")

            L6 = int(input("A5-A6 Koltuk Mesafesi: "))
            x6= L6+x5
            print("---------------------------")
            print("A6 Lamba Mesafesi: ",L6)
            print("A6 Lamba Koordinatı: ",x6)
            print("---------------------------")

            L7 = int(input("A6-A7 Koltuk Mesafesi: "))
            x7= L7+x6
            print("---------------------------")
            print("A7 Lamba Mesafesi: ",L7)
            print("A7 Lamba Koordinatı: ",x7)
            print("---------------------------")

            if x7 == 4751:
                print("Sol Ön Kaplama Limiti 4751mm.")

        elif toplam>=142:
            x2=toplam+L2
            print("---------------------------")
            print("A2 Lamba Mesafesi: ",L2)
            print("A2 Lamba Koordinatı: ",x2)
            print("---------------------------")

            L3 = int(input("A2-A3 Koltuk Mesafesi: "))
            x3= L3+x2
            print("---------------------------")
            print("A3 Lamba Mesafesi: ",L3)
            print("A3 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("A3-A4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("A4 Lamba Mesafesi: ",L4)
            print("A4 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("A4-A5 Koltuk Mesafesi: "))
            x5= L5+x4
            print("---------------------------")
            print("A5 Lamba Mesafesi: ",L5)
            print("A5 Lamba Koordinatı: ",x5)
            print("---------------------------")

            L6 = int(input("A5-A6 Koltuk Mesafesi: "))
            x6= L6+x5
            print("---------------------------")
            print("A6 Lamba Mesafesi: ",L6)
            print("A6 Lamba Koordinatı: ",x6)
            print("---------------------------")

            L7 = int(input("A6-A7 Koltuk Mesafesi: "))
            x7= L7+x6

            st = 4751 - x7
            if st <= 142:
                sc = 142-st
                sv = L7-sc
                sf = x6+sv
                print("---------------------------")
                print("A7 Lamba Mesafesi: ", sf)
                print("A7 Koltuk Mesafesi : ", sv)
                print("---------------------------")
                
            if st >= 142:
                print("---------------------------")
                print("A7 Lamba Mesafesi: ", L7)
                print("A7 Lamba Koordinatı: ", x7)
                print("---------------------------")

            koltuk = str(input("Orta Kapı Karşısında Koltuk(var/yok): "))
            if (koltuk == "yok"):
                
                print("---------------------------------------------------------")
                print("Sol Orta Kaplama Parçası")

                tp = int(input("A7 arkası boşluk: "))
                vp = int(input("Orta kapı boşluğu: "))
                bp = int(input("A8 önündeki boşluk: "))

                at = (tp + vp + bp) + sf
                rt = at - 6236
                

                print("---------------------------------------------------------")
                
                 
                print("A8 Lamba mesafesi: ", rt)
                L8 = int(input("A8-A9 koltuk mesafesi: "))
                x8 = rt + L8
                print("---------------------------")
                print("A9 Lamba Mesafesi: ", L8)
                print("A9 Lamba Koordinatı: ", x8)
                print("---------------------------")

                L9 = int(input("A9-A10 koltuk mesafesi: "))
                x9 = x8 + L9
                print("---------------------------")
                print("A10 Lamba Mesafesi: ", L9)
                print("A10 Lamba Koordinatı: ", x9)
                print("---------------------------")

                L10 = int(input("A10-A11 koltuk mesafesi: "))
                x10 = x9 + L10
                print("---------------------------")
                print("A11 Lamba Mesafesi: ", L10)
                print("A11 Lamba Koordinatı: ", x10)
                print("---------------------------")

                L11 = int(input("A11-A12 koltuk mesafesi: "))
                x11 = x10 + L11
                
                if x11 >= 3481:
                    print("Kaplama limiti 3481mm olduğundan, bu kaplamaya",
                          "daha fazla servis seti koyamazsınız.")
                    print("Bir sonraki kaplamaya kadar olan değerlere 0 giriniz.")

                elif x <= 3481:
                    L12 = int(input("A12-A13 koltuk mesafesi: "))
                    x12 = x11 + L12
                    print("---------------------------")
                    print("A13 Lamba Mesafesi: ", L12)
                    print("A13 Lamba Koordinatı: ", x12)
                    print("---------------------------")
        
      
                
                print("---------------------------------------------------------")

            if (koltuk == "var"):
                L8 = int(input("A7-A8 Koltuk Mesafesi: "))
                a8 = L8 + sv
                c8 = a8 - 4751
                if c8 <= 142:
                    av = L8 + x7
                    c8 = av - 4751

                    print("---------------------------")
                    print("A8 Lamba Mesafesi: ", L8)
                    print("A8 Lamba Koordinatı: ", c8)
                    print("---------------------------")
                    
                    L9 = int(input("A8-A9 Koltuk mesafesi: "))
                    g8 = c8 + L9
                    print("---------------------------")
                    print("A9 Lamba Mesafesi: ", L9)
                    print("A9 Lamba Koordinatı: ", g8)
                    print("---------------------------")

                    print("-------------------------")
                    print("3.Kaplamaya geçiniz.")
                    print("-------------------------")

                    
                    L9c = int(input("A9-A10 koltuk mesafesi: "))

                    lp = av + L9
                    yp = lp + L9c
                    xp = yp - 6236

                    print("---------------------------")   
                    print("A10 Lamba Mesafesi: ", L9c)
                    print("A10 Lamba Koordinatı: ", xp)
                    print("---------------------------")

                    L10 = int(input("A10-A11 koltuk mesafesi: "))
                    x10 = xp + L10
                    print("---------------------------")
                    print("A11 Lamba Mesafesi: ", L10)
                    print("A11 Lamba Koordinatı: ", x10)
                    print("---------------------------")

                    L11 = int(input("A11-A12 koltuk mesafesi: "))
                    x11 = x10 + L11
                    print("---------------------------")
                    print("A12 Lamba Mesafesi: ", L11)
                    print("A12 Lamba Koordinatı: ", x11)
                    print("---------------------------")
                            
                    L12 = int(input("A12-A13 koltuk mesafesi: "))
                    x12 = x11 + L12
                    print("---------------------------")
                    print("A13 Lamba Mesafesi: ", L12)
                    print("A13 Lamba Koordinatı: ", x12)
                    print("---------------------------")
                            
                    L13 = int(input("A13-A14 koltuk mesafesi: "))
                    x13 = x12 + L13

                    if x13 >= 3339:
                        ah = 3481 - x13
                        kh = 142 - ah
                        gh = L13 - kh
                        th = x12 + gh

                        print("---------------------------")
                        print("A14 Lamba Mesafesi: ", gh)
                        print("A14 Lamba Koordinatı: ", th)
                        print("---------------------------")

                    elif x13 <= 3339:
                        print("Kaplama limiti 3339mm olduğundan, bu kaplamaya",
                                 "daha fazla servis seti koyamazsınız.")
                        print("Bir sonraki kaplamaya kadar olan değerlere 0 giriniz.")

                   
                        

                elif c8 >= 142:
                    print("---------------------------")
                    print("A8 Lamba Mesafesi: ", l8)
                    print("A8 Lamba Koordinatı: ", c8)
                    print("---------------------------")
                    
                    L9 = int(input("A8-A9 Koltuk mesafesi:"))
                    g8 = c8 + L9
                    print("---------------------------")
                    print("A9 Lamba Mesafesi: ", L9)
                    print("A9 Lamba Koordinatı: ", g8)
                    print("---------------------------")
                    
                    print("---------------------------------------------------------")
                    print("3.Kaplamaya geçiniz.")
                    print("---------------------------------------------------------")


                    L9c = int(input("A9-A10 koltuk mesafesi: "))

                    lp = av + L9
                    yp = lp + L9c
                    xp = yp - 6236

                    print("---------------------------")      
                    print("A10 Lamba Mesafesi: ", L9c)
                    print("A10 Lamba Koordinatı: ", xp)
                    print("---------------------------")

                    L10 = int(input("A10-A11 koltuk mesafesi: "))
                    x10 = x9 + L10
                    print("---------------------------")
                    print("A11 Lamba Mesafesi: ", L10)
                    print("A11 Lamba Koordinatı: ", x10)
                    print("---------------------------")

                    L11 = int(input("A11-A12 koltuk mesafesi: "))
                    x11 = x10 + L11
                    print("---------------------------")
                    print("A12 Lamba Mesafesi: ", L11)
                    print("A12 Lamba Koordinatı: ", x11)
                    print("---------------------------")
                            
                    L12 = int(input("A12-A13 koltuk mesafesi: "))
                    x12 = x11 + L12
                    print("---------------------------")
                    print("A13 Lamba Mesafesi: ", L12)
                    print("A13 Lamba Koordinatı: ", x12)
                    print("---------------------------")
                            
                    L13 = int(input("A13-A14 koltuk mesafesi: "))
                    x13 = x12 + L13

                    if x13 >= 3339:
                        ah = 3481 - x13
                        kh = 142 - ah
                        gh = L13 - kh
                        th = x12 + gh

                        print("---------------------------")
                        print("A14 lamba mesafesi: ", gh)
                        print("A14 lamba koordinatı: ", th)
                        print("---------------------------")

                    elif x13 <= 3339:
                        print("Kaplama limiti 3339mm olduğundan, bu kaplamaya",
                                 "daha fazla servis seti koyamazsınız.")
                        print("Bir sonraki kaplamaya kadar olan değerlere 0 giriniz.")

                         
                    print("---------------------------------------------------------")            
          
### Sağ Kapı
        print("SAĞ KAPI TARAFI LAMBA ÖLÇÜLERİ")    
        c = int(input("B-D1 Koltuk Mesafesi: "))
        d = int(193)
        f = int(142)
        toplams = c-d
        if toplams <= f:
            print("D1 Lamba Mesafesi: ",f)

        else:
            print("D1 Lamba Mesafesi: ",toplams)
        
        L2 = int(input("D1-D2 Koltuk Mesafesi: "))

        if toplams<=142:
            x = int(142)-toplams
            y = L2-x
            z = y+f
            print("---------------------------")
            print("D2 Lamba Mesafesi: ",L2)
            print("D2 Lamba Koordinatı: ",z)
            print("---------------------------")

            L3 = int(input("D2-D3 Koltuk Mesafesi: "))
            x3 = L3+z
            print("---------------------------")
            print("D3 Lamba Mesafesi: ",L3)
            print("D3 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("D3-D4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("D4 Lamba Mesafesi: ",L4)
            print("D4 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("D4-D5 Koltuk Mesafesi: "))
            x5= L5+x4
            print("---------------------------")
            print("D5 Lamba Mesafesi: ",L5)
            print("D5 Lamba Koordinatı: ",x5)
            print("---------------------------")

            L6 = int(input("D5-D6 Koltuk Mesafesi: "))
            x6= L6+x5
            print("---------------------------")
            print("D6 Lamba Mesafesi: ",L6)
            print("D6 Lamba Koordinatı: ",x6)
            print("---------------------------")

            if x6>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L7 = int(input("D6-D7 Koltuk Mesafesi: "))
            x7= L7+x6
            print("---------------------------")
            print("D7 Lamba Mesafesi: ",L7)
            print("D7 Lamba Koordinatı: ",x7)
            print("---------------------------")

            if x7>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            print("---------------------------------------------------------")
            de = int(input("D7 - D8 arası mesafe: "))
            dt = int(input("Orta Kapı mesafesi: "))
            ds = int(input("Orta kapı bitiminden D9 arası mesafesi: "))
            print("---------------------------------------------------------")
            
            ud = (de + dt + ds + x7) - 6236

                
            print("Orta Kapı Sonrası Koltuklardan Devam Ediniz.")
            print("---------------------------------------------------------")

            print("D9 lamba mesafesi: ", ud)

            m = int(input("D9-D10 Koltuk Mesafesi: "))
            
            jk = m + ud
                
            print("D10 Lamba Mesafesi: ", jk)

            L3 = int(input("D10-D11 Koltuk Mesafesi: "))
            x3 = jk+L3
            print("---------------------------")
            print("D11 Lamba Mesafesi: ",L3)
            print("D11 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("D11-D12 Koltuk Mesafesi: "))
            x4 = L4+x3
            print("---------------------------")
            print("D12 Lamba Mesafesi: ",L4)
            print("D12 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("D12-D13 Koltuk Mesafesi: "))
            x5 = L5+x4
            
            if x5 >= 3339:
                    ae = 3481 - x5
                    ke = 142 - ae
                    ge = L5 - ke
                    te = x4 + ge

                    print("---------------------------")
                    print("D13 Lamba Mesafesi: ", ge)
                    print("D13 Lamba Koordinatı: ", te)
                    print("---------------------------")

            elif x5 <= 3339:
                print("---------------------------")
                print("D13 Lamba Mesafesi: ", L5)
                print("D13 Lamba Koordinatı: ", x5)
                end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
                print("---------------------------")
                

            else:
                end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
                print("---------------------------------------------------------")

        elif toplams>=142:
            x2 = toplams+L2
            print("---------------------------")
            print("D2 Lamba Mesafesi: ",L2)
            print("D2 Lamba Koordinatı: ",x2)
            print("---------------------------")

            L3 = int(input("D2-D3 Koltuk Mesafesi: "))
            x3 = L3+x2
            print("---------------------------")
            print("D3 Lamba Mesafesi: ",L3)
            print("D3 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("D3-D4 Koltuk Mesafesi: "))
            x4= L4+x3
            print("---------------------------")
            print("D4 Lamba Mesafesi: ",L4)
            print("D4 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("D4-D5 Koltuk Mesafesi: "))
            x5= L5+x4
            print("---------------------------")
            print("D5 Lamba Mesafesi: ",L5)
            print("D5 Lamba Koordinatı: ",x5)
            print("---------------------------")

            L6 = int(input("D5-D6 Koltuk Mesafesi: "))
            x6= L6+x5
            print("---------------------------")
            print("D6 Lamba Mesafesi: ",L6)
            print("D6 Lamba Koordinatı: ",x6)
            print("---------------------------")

            if x6>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")

            L7 = int(input("D6-D7 Koltuk Mesafesi: "))
            x7= L7+x6
            print("---------------------------")
            print("D7 Lamba Mesafesi: ",L7)
            print("D7 Lamba Koordinatı: ",x7)
            print("---------------------------")

            if x7>=(4609):
                print("Bu alanın uzunluğu 4609mm daha fazla koltuk koyamazsınız.")
                
            print("---------------------------------------------------------")
            de = int(input("D7 - D8 arası mesafe: "))
            dt = int(input("Orta Kapı mesafesi: "))
            ds = int(input("Orta kapı bitiminden D9 arası mesafesi: "))
            ud = (de + dt + ds + x7) - 6236
           
            print("---------------------------------------------------------")
            print("Orta Kapı Sonrası Koltuklardan Devam Ediniz.")
            print("---------------------------------------------------------")

            print("D9 lamba mesafesi: ", ud)

            m = int(input("D9-D10 Koltuk Mesafesi: "))
            
            jk = m + ud
                
            print("D10 Lamba Mesafesi: ", jk)

            L3 = int(input("D10-D11 Koltuk Mesafesi: "))
            x3 = jk+L3
            print("---------------------------")
            print("D11 Lamba Mesafesi: ",L3)
            print("D11 Lamba Koordinatı: ",x3)
            print("---------------------------")

            L4 = int(input("D11-D12 Koltuk Mesafesi: "))
            x4 = L4+x3
            print("---------------------------")
            print("D12 Lamba Mesafesi: ",L4)
            print("D12 Lamba Koordinatı: ",x4)
            print("---------------------------")

            L5 = int(input("D12-D13 Koltuk Mesafesi: "))
            x5 = L5+x4
            
            if x5 >= 3339:
                    ae = 3481 - x5
                    ke = 142 - ae
                    ge = L5 - ke
                    te = x4 + ge

                    print("---------------------------")
                    print("D13 Lamba Mesafesi: ", ge)
                    print("D13 Lamba Koordinatı: ", te)
                    print("---------------------------")

            elif x5 <= 3339:
                print("---------------------------")
                print("D13 Lamba Mesafesi: ", L5)
                print("D13 Lamba Koordinatı: ", x5)
                print("---------------------------")
                print("---------------------------------------------------------")
                end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
                print("---------------------------------------------------------")

    
        else:
            print("---------------------------------------------------------")
            end = str(input("Farklı Bir Kombinasyon için Programı Yeniden Başlatınız:..."))
            print("---------------------------------------------------------")


