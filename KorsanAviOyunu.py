import pgzrun
import time
from pgzhelper import *
from veritabanlari import *
import webbrowser

WIDTH = 800
HEIGHT = 500

TITLE = "KORSAN AVI"
FPS = 30
hiz = 0.1
hiz2 = 1
ilerii =  "False"
ilerii2 = "False"
ilerii3 = "False"
ilerii4 = "False"
sayim = 0
sayim1 = 0
sayim3 = 0
sayim4 = 0
seviye = 1
seviye2 = 0
basim = 0
kazanmak = 0
oldurulen_iskelet = 0
oldurulen_gemi = 0
mod = "menü"
basim_artisi = 100
puan = 10000
bombalar = []
bombalar2 = []
can = 3
ses = "True"
dusman_sayisi = 4
new_image = "dusman1"
sure = 0
alinabilecek12 = "False"
alinabilecek22 = "False"
alinabilecek32 = "False"
alinabilecek42 = "False"
zorluk2 = "False"
super_patlama = "False"
dusman1_can = 3
dusman2_can = 3
dusman4_can = 3
gemi_adami = "False"
setup_db_puan()
setup_db_seviye()
setup_db_12()
setup_db_22()
setup_db_32()
setup_db_42()
setup_db_ses()
setup_db_basim_artisi()
seviye = yukle_seviye()
puan = yukle_puan()
ses = yukle_ses()
basim_artisi = yukle_basim_artisi()
alinabilecek12 = yukle_alinabilecek12()
alinabilecek22 = yukle_alinabilecek22()
alinabilecek32 = yukle_alinabilecek32()
alinabilecek42 = yukle_alinabilecek32()

benim_gemim = Actor("normal_gemi", (400, 340))
alinabilecek1= Actor("dusman1",(100,150))
alinabilecek2= Actor("dusman3",(300,250))
alinabilecek3= Actor("tas1",(500,150))
alinabilecek4= Actor("tas2",(700,250))
adsiz9 = Actor("adsiz9")
dusman_kayik2 = Actor("dusman_kayik", (800,100))
dusman_kayik3 = Actor("dusman_kayik", (900,380))
dusman_kayik4 = Actor("dusman_kayik", (1050,180))
dusman_kayik5 = Actor("dusman_kayik", (1200,280))
dusman_gemi_son1 = Actor("son_tas1", (1000,100))
dusman_gemi_son2 = Actor("son_tas2", (1100,380))
dusman_gemi_son3 = Actor("son_tas3", (1250,150))
dusman_gemi_son4 = Actor("son_tas4", (1400,190))
alinabilecek11= Actor("dusman1",(100,100))
alinabilecek111= Actor("dusman1",(700,350))
gemi_resmi = Actor("oldurulen_gem", (200,30))
iskelet_resmi = Actor("oldurulen_is", (340,30))
buton1 = Actor("buton3",(100,100))
buton2 = Actor("buton4",(200,100))
buton3 = Actor("buton4",(300,100))
buton4 = Actor("buton4",(400,100))
buton5 = Actor("buton4",(500,100))
buton6 = Actor("buton4",(600,100))
buton7 = Actor("buton4",(700,100))
buton8 = Actor("buton4",(100,250))
buton9 = Actor("buton4",(200,250))
buton10 = Actor("buton4",(300,250))
buton11 = Actor("buton4",(400,250))
buton12 = Actor("buton4",(500,250))
buton13 = Actor("buton4",(600,250))
buton14 = Actor("buton4",(700,250))
buton15 = Actor("buton4",(100,400))
buton16 = Actor("buton4",(200,400))
buton17 = Actor("buton4",(300,400))
buton18 = Actor("buton4",(400,400))
buton19 = Actor("buton4",(500,400))
buton20 = Actor("buton4",(600,400))
buton21 = Actor("buton4",(700,400))
buton22 = Actor("buton4",(100,100))
buton23 = Actor("buton4",(200,100))
buton24 = Actor("buton4",(300,100))
buton25 = Actor("buton4",(400,100))
buton26 = Actor("buton4",(500,100))
buton27 = Actor("buton4",(600,100))
buton28 = Actor("buton4",(700,100))
buton29 = Actor("buton4",(100,250))
buton30 = Actor("buton4",(200,250))
buton31 = Actor("buton4",(300,250))
buton32 = Actor("buton4",(400,250))
buton33 = Actor("buton4",(500,250))
buton34 = Actor("buton4",(600,250))
buton35 = Actor("buton4",(700,250))
buton36 = Actor("buton4",(100,400))
buton37 = Actor("buton4",(200,400))
buton38 = Actor("buton4",(300,400))
buton39 = Actor("buton4",(400,400))
buton40 = Actor("buton4",(500,400))
adam = Actor("kayik", (100,250))
bonus_buton = Actor("buton3",(600,400))
ileri = Actor("ileri", (770, 250))
ileri2 = Actor("ileri", (30, 250))
alinabilecek222= Actor("tas2",(100,350))
alinabilecek26= Actor("dusman3",(500,60))
alinabilecek33= Actor("tas1",(300,60))
canlar = Actor("can", (50, 30))
bayrak = Actor("bayrak", (50, 30))
alinabilecek44= Actor("tas2",(700,100))
a_gemi = Actor("normal_gemi", (380, 420))
b_gemi = Actor("tas1", (380, 240))
c_gemi = Actor("dusman4", (390, 300))
arkaplan = Actor("adsiz3")
kaybettiniz = Actor("adsiz4")
menu = Actor("adsiz5")
kazandiniz = Actor("adsiz6")
dusman1 = Actor("dusman1", (100,-175))
dusman2 = Actor("dusman4", (300,-700))
dusman3 = Actor("dusman3", (500,-550))
dusman4 = Actor("dusman1", (700,-920))
oyna = Actor("bonus", (170, 250))
bonus_oyna = Actor("bonus", (400, 275))
oyna2 = Actor("bonus", (400, 300))
oyna3 = Actor("bonus", (400, 250))
son_oyun_gemisi = Actor("son_oyun_gemisi", (100,250))
dukkan = Actor("bonus", (170,400))
seviyeler = Actor("bonus", (570, 400))
puan_gemisi = Actor("normal_gemi", (300, 200))
koleksiyon = Actor("bonus", (570,325))
para_birimi = Actor("bonus", (170,325))
geri_don = Actor("bonus", (400, 350))
geri_don2 = Actor("bonus", (400, 350))
bilgi = Actor("bonus", (570, 250))
mermi_topu = Actor("mermi_topu", (400, 290))
mermi_topu2 = Actor("mermi_topu2", (150,250))
bomba2 = Actor("bomba")
bomba3 = Actor("bomba2")
bonus_1 = Actor("bonus22", (650, 100))
bonus_2 = Actor("bonus22", (650, 225))
bonus_3 = Actor("bonus22", (650, 350))
hakkinda = Actor("adsiz8")
bomba2.pos = a_gemi.pos
bomba3.pos = mermi_topu2.pos
carpi = Actor("carpi",(770,30))
ayar_arkaplan = Actor("adsiz3")
ayarlar = Actor("ayarlar", (750,50))
sesli = Actor("bonus", (170,250))
sessiz = Actor("bonus", (570, 250))
sifirla = Actor("bonus", (370,400))



def draw():
    global seviye, mod, puan, zorluk2, sesli, sessiz, sifirla, ses, seviye2, basim, ilerii, ilerii2, kazanmak, gemi_adami
    global oldurulen_iskelet, oldurulen_gemi, sure

    if mod == "oyun":
        arkaplan.draw()
        benim_gemim.draw()
        dusman1.draw()
        dusman2.draw()
        canlar.draw()
        dusman3.draw()
        dusman4.draw()
        mermi_topu.draw()
        screen.draw.text(str(can) + "\n", center=(110, 41), color = 'black', fontsize = 37)
        screen.draw.text("=", center= (90, 25), color="black", fontsize = 37)
        # Füzelerin çizilmesi   
        for i in range(len(bombalar)):
            bombalar[i].draw()
        carpi.draw()
    

    if mod == "kaybettin":
        kaybettiniz.draw()
        geri_don.draw()
        carpi.draw()
        screen.draw.text("GERİ DÖN!", center= (400, 350), color="black", fontsize = 40)
        screen.draw.text(str(puan) + "\n", center=(400, 295), color = 'black', fontsize = 60)
        
    if mod == "son_seviye":
        arkaplan.draw()
        screen.draw.text("Bonus Seviye!", center= (400, 100), color="black", fontsize = 90)
        screen.draw.text("Oyunun son ve en zor seviyesi!", center= (400, 175), color="black", fontsize = 40)
        bonus_oyna.draw()
        screen.draw.text("BAŞLA!", center= (400, 275), color="black", fontsize = 50)
        carpi.draw()

    if mod == "son_kaybettiniz":
        kaybettiniz.draw()
        geri_don2.draw()
        screen.draw.text("GERİ DÖN!", center= (400, 350), color="black", fontsize = 40)
        screen.draw.text(str(oldurulen_gemi) + "\n", center=(400, 295), color = 'black', fontsize = 60)
        screen.draw.text(",", center= (450, 270), color="black", fontsize = 70)
        screen.draw.text(str(oldurulen_iskelet) + "\n", center=(500, 295), color = 'black', fontsize = 60)

    if mod == "son_kazandiniz":
        adsiz9.draw()
        alinabilecek11.draw()
        alinabilecek26.draw()
        alinabilecek33.draw()
        alinabilecek44.draw()
        alinabilecek111.draw()
        alinabilecek222.draw()


    if mod == "kazandiniz":
        kazandiniz.draw()
        carpi.draw()
        if seviye < 40:
            oyna2.draw()
            screen.draw.text("DEVAM ET!", center= (400, 300), color="black", fontsize = 40)
            screen.draw.text(str(seviye) + "\n", center=(530, 120), color = 'black', fontsize = 70)
        if seviye == 40:
            kazanmak = 1
            oyna3.draw()
            screen.draw.text("MENÜYE DÖN!", center= (400, 250), color="black", fontsize = 35)
            screen.draw.text("BU SON SEVİYEYDİ....", center= (400, 350), color="black", fontsize = 60)
            screen.draw.text(str(seviye) + "\n", center=(530, 120), color = 'black', fontsize = 70)

    if mod == "para":
        arkaplan.draw()
        screen.draw.text(str(puan) + "\n", center=(165, 40), color = 'black', fontsize = 37)
        screen.draw.text("=", center= (100, 25), color="black", fontsize = 37)
        screen.draw.text(str(basim) + "\n", center=(300, 380), color = 'black', fontsize = 90)
        screen.draw.text("Gemiye tıkla ve puan kazan!" , center=(400, 27), color = 'black', fontsize = 37)
        bayrak.draw()
        if benim_gemim.image == "normal_gemi":
            puan_gemisi.draw()
            puan_gemisi.image = "normal_gemi"

        if benim_gemim.image == "kullan2":
            puan_gemisi.draw()
            puan_gemisi.image = "kullan2"

        if benim_gemim.image == "kullan1":
            puan_gemisi.draw()
            puan_gemisi.image = "kullan1"

        if benim_gemim.image == "kullan3":
            puan_gemisi.draw()
            puan_gemisi.image = "kullan3"

        if benim_gemim.image == "kullan4":
            puan_gemisi.draw()
            puan_gemisi.image = "kullan4"

        bonus_1.draw()
        screen.draw.text("Her tıklayışta +1 puan", center= (650, 80), color="black", fontsize = 26)
        screen.draw.text("Ücret = 100 puan", center= (650, 110), color="black", fontsize = 26)
        bonus_2.draw()
        screen.draw.text("Her tıklayışta +2 puan", center= (650, 200), color="black", fontsize = 26)
        screen.draw.text("Ücret = 300 puan", center= (650, 235), color="black", fontsize = 26)
        bonus_3.draw()
        screen.draw.text("Her tıklayışta +3 puan", center= (650, 330), color="black", fontsize = 26)
        screen.draw.text("Ücret = 500 puan", center= (650, 360), color="black", fontsize = 26)
        carpi.draw()
        

    if mod == "seviye_sec":
        arkaplan.draw()
        carpi.draw()
        if ilerii == "False":
            ileri.draw()
            buton1.draw()
            buton2.draw()
            buton3.draw()
            buton4.draw()
            buton5.draw()
            buton6.draw()
            buton7.draw()
            buton8.draw()
            buton9.draw()
            buton10.draw()
            buton11.draw()
            buton12.draw()
            buton13.draw()
            buton14.draw()
            buton15.draw()
            buton16.draw()
            buton17.draw()
            buton18.draw()
            buton19.draw()
            buton20.draw()
            buton21.draw()
            screen.draw.text("1", center= (100, 100), color="black", fontsize = 60)
            screen.draw.text("2", center= (200, 100), color="black", fontsize = 60)
            screen.draw.text("3", center= (300, 100), color="black", fontsize = 60)
            screen.draw.text("4", center= (400, 100), color="black", fontsize = 60)
            screen.draw.text("5", center= (500, 100), color="black", fontsize = 60)
            screen.draw.text("6", center= (600, 100), color="black", fontsize = 60)
            screen.draw.text("7", center= (700, 100), color="black", fontsize = 60)
            screen.draw.text("8", center= (100, 250), color="black", fontsize = 60)
            screen.draw.text("9", center= (200, 250), color="black", fontsize = 60)
            screen.draw.text("10", center= (300, 250), color="black", fontsize = 60)
            screen.draw.text("11", center= (400, 250), color="black", fontsize = 60)
            screen.draw.text("12", center= (500, 250), color="black", fontsize = 60)
            screen.draw.text("13", center= (600, 250), color="black", fontsize = 60)
            screen.draw.text("14", center= (700, 250), color="black", fontsize = 60)
            screen.draw.text("15", center= (100, 400), color="black", fontsize = 60)
            screen.draw.text("16", center= (200, 400), color="black", fontsize = 60)
            screen.draw.text("17", center= (300, 400), color="black", fontsize = 60)
            screen.draw.text("18", center= (400, 400), color="black", fontsize = 60)
            screen.draw.text("19", center= (500, 400), color="black", fontsize = 60)
            screen.draw.text("20", center= (600, 400), color="black", fontsize = 60)
            screen.draw.text("21", center= (700, 400), color="black", fontsize = 60)
        elif ilerii == "True":
            ileri2.draw()
            buton22.draw()
            buton23.draw()
            buton24.draw()
            buton25.draw()
            buton26.draw()
            buton27.draw()
            buton28.draw()
            buton29.draw()
            buton30.draw()
            buton31.draw()
            buton32.draw()
            buton33.draw()
            buton34.draw()
            buton35.draw()
            buton36.draw()
            buton37.draw()
            buton38.draw()
            buton39.draw()  
            buton40.draw()
            screen.draw.text("22", center= (100, 100), color="black", fontsize = 60)
            screen.draw.text("23", center= (200, 100), color="black", fontsize = 60)
            screen.draw.text("24", center= (300, 100), color="black", fontsize = 60)
            screen.draw.text("25", center= (400, 100), color="black", fontsize = 60)
            screen.draw.text("26", center= (500, 100), color="black", fontsize = 60)
            screen.draw.text("27", center= (600, 100), color="black", fontsize = 60)
            screen.draw.text("28", center= (700, 100), color="black", fontsize = 60)
            screen.draw.text("29", center= (100, 250), color="black", fontsize = 60)
            screen.draw.text("30", center= (200, 250), color="black", fontsize = 60)
            screen.draw.text("31", center= (300, 250), color="black", fontsize = 60)
            screen.draw.text("32", center= (400, 250), color="black", fontsize = 60)
            screen.draw.text("33", center= (500, 250), color="black", fontsize = 60)
            screen.draw.text("34", center= (600, 250), color="black", fontsize = 60)
            screen.draw.text("35", center= (700, 250), color="black", fontsize = 60)
            screen.draw.text("36", center= (100, 400), color="black", fontsize = 60)
            screen.draw.text("37", center= (200, 400), color="black", fontsize = 60)
            screen.draw.text("38", center= (300, 400), color="black", fontsize = 60)
            screen.draw.text("39", center= (400, 400), color="black", fontsize = 60)
            screen.draw.text("40", center= (500, 400), color="black", fontsize = 60)
            if seviye <41:
                screen.draw.text("SON!", center= (650, 400), color="black", fontsize = 80)
            if seviye == 41:
                bonus_buton.draw()
                screen.draw.text("BONUS", center= (600, 400), color="black", fontsize = 30)
        
    if mod == "deneme":
        arkaplan.draw()

    if mod == "menü":
        menu.draw()
        oyna.draw()
        bilgi.draw()
        dukkan.draw()
        para_birimi.draw()
        koleksiyon.draw()
        a_gemi.draw()
        b_gemi.draw()
        bomba2.draw()
        screen.draw.text("OYNA", center= (170, 250), color="black", fontsize = 30)
        screen.draw.text("PUAN TOPLA    ", center= (170, 325), color="black", fontsize = 30)
        screen.draw.text("HAKKINDA", center= (570, 250), color="black", fontsize = 30)
        screen.draw.text("DÜKKAN", center= (170, 400), color="black", fontsize = 30)
        screen.draw.text("KOLEKSİYON", center= (570, 325), color="black", fontsize = 30)
        screen.draw.text(str(puan) + "\n", center=(165, 40), color = 'black', fontsize = 37)
        screen.draw.text(str(seviye) + "\n", center=(370, 40), color = 'black', fontsize = 37)
        screen.draw.text("=", center= (100, 25), color="black", fontsize = 37)
        screen.draw.text("SEVİYE:", center= (300, 25), color="red", fontsize = 37)
        ayarlar.draw()
        bayrak.draw()
        

    if mod == "hakkinda":
        hakkinda.draw()
        c_gemi.draw()
        carpi.draw()

    if mod == "son_oyun":
        arkaplan.draw()
        son_oyun_gemisi.draw()
        mermi_topu2.draw()
        carpi.draw()
        iskelet_resmi.draw()
        gemi_resmi.draw()
        dusman_kayik2.draw()
        dusman_kayik3.draw()
        dusman_kayik4.draw()
        canlar.draw()
        dusman_kayik5.draw()
        dusman_gemi_son1.draw()
        dusman_gemi_son2.draw()
        dusman_gemi_son3.draw()
        dusman_gemi_son4.draw()
        screen.draw.text(str(can) + "\n", center=(110, 41), color = 'black', fontsize = 37)
        screen.draw.text("=", center= (90, 25), color="black", fontsize = 37)
        screen.draw.text(str(oldurulen_gemi) + "\n", center=(250, 41), color = 'black', fontsize = 37)
        screen.draw.text("=", center= (230, 25), color="black", fontsize = 37)
        screen.draw.text(str(oldurulen_iskelet) + "\n", center=(410, 41), color = 'black', fontsize = 37)
        screen.draw.text("=", center= (380, 25), color="black", fontsize = 37)
        if gemi_adami == "True":
            adam.draw() 
        for v in range(len(bombalar2)):
            bombalar2[v].draw()


    if mod == "dükkan":
        arkaplan.draw()
        carpi.draw()
        alinabilecek1.draw()
        alinabilecek2.draw()
        alinabilecek3.draw()
        alinabilecek4.draw()
        screen.draw.text(str(puan) + "\n", center=(165, 40), color = 'black', fontsize = 37)
        screen.draw.text("=", center= (100, 25), color="black", fontsize = 37)
        bayrak.draw()
        screen.draw.text("Ücret : 50 Puan", center=(100, 250), color="black", fontsize = 30)
        screen.draw.text("Ücret : 100 Puan", center=(300, 350), color="black", fontsize = 30)
        screen.draw.text("Ücret : 150 Puan", center=(500, 250), color="black", fontsize = 30)
        screen.draw.text("Ücret : 200 Puan", center=(700, 350), color="black", fontsize = 30)


    if mod == "koleksiyon":
        arkaplan.draw()
        carpi.draw()
        if alinabilecek12 == "True":
            alinabilecek1.draw()
            screen.draw.text("Aldın!", center=(100, 250), color="black", fontsize = 30)
        if alinabilecek22 == "True":
            alinabilecek2.draw()
            screen.draw.text("Aldın", center=(300, 350), color="black", fontsize = 30)
        if alinabilecek32 == "True":
            alinabilecek3.draw()
            screen.draw.text("Aldın!", center=(500, 250), color="black", fontsize = 30)
        if alinabilecek42 == "True":
            alinabilecek4.draw()
            screen.draw.text("Aldın!", center=(700, 350), color="black", fontsize = 30)
        

    if mod == "ayarlar":
        ayar_arkaplan.draw()
        sesli.draw()
        sessiz.draw()
        sifirla.draw()
        carpi.draw()
        screen.draw.text("SESLİ OYNA", center= (170, 250), color="black", fontsize = 30)
        screen.draw.text("SESSİZ OYNA", center= (570, 250), color="black", fontsize = 30)
        screen.draw.text("SIFIRLA", center= (370, 400), color="black", fontsize = 30)
        alinabilecek11.draw()
        alinabilecek26.draw()
        alinabilecek33.draw()
        alinabilecek44.draw()
        alinabilecek111.draw()
        alinabilecek222.draw()

def carpismalar():
    global mod, puan, seviye, seviye2, zorluk2, dusman_sayisi, can, new_image, dusman1_can
    global dusman2_can, dusman4_can, sesli, sessiz, ses, sifirla, gemi_adami, oldurulen_iskelet,oldurulen_gemi

    if mod == "son_oyun":
        if (mod == "son_oyun" and gemi_adami == "True") and adam.colliderect(dusman_kayik2):
            if ses == "True":
                sounds.patlama2.play()
            dusman_kayik2.x = 920
            oldurulen_iskelet +=1

        if (mod == "son_oyun" and gemi_adami == "True") and adam.colliderect(dusman_kayik3):
            if ses == "True":
                sounds.patlama2.play()
            dusman_kayik3.x = 1020
            oldurulen_iskelet +=1

        if (mod == "son_oyun" and gemi_adami == "True") and adam.colliderect(dusman_kayik4):
            if ses == "True":
                sounds.patlama2.play()
            dusman_kayik4.x = 1170
            oldurulen_iskelet +=1

        if (mod == "son_oyun" and gemi_adami == "True") and adam.colliderect(dusman_kayik5):
            if ses == "True":
                sounds.patlama2.play()
            dusman_kayik5.x = 1320
            oldurulen_iskelet +=1

    for k in range(len(bombalar2)):
        if mod == "son_oyun":
            if bombalar2[k].colliderect(dusman_gemi_son1):
                if ses == "True":
                    sounds.patlama2.play()
                bombalar2.pop(k)
                oldurulen_gemi += 1
                dusman_gemi_son1.x = 0
                break

            if bombalar2[k].colliderect(dusman_gemi_son2):
                if ses == "True":
                    sounds.patlama2.play()
                bombalar2.pop(k)
                oldurulen_gemi += 1
                dusman_gemi_son2.x = 0
                break
                
            if bombalar2[k].colliderect(dusman_gemi_son3):
                if ses == "True":
                    sounds.patlama2.play()
                bombalar2.pop(k)
                oldurulen_gemi += 1
                dusman_gemi_son3.x = 0
                break

            if bombalar2[k].colliderect(dusman_gemi_son4):
                if ses == "True":
                    sounds.patlama2.play()
                bombalar2.pop(k)
                oldurulen_gemi += 1
                dusman_gemi_son4.x = 0
                break


    for j in range(len(bombalar)):
        if seviye <= 9:
            if bombalar[j].colliderect(dusman1):
                if ses == "True":
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman1.x = 100000
                puan = puan + 1
                dusman_sayisi -=1
                break
            if bombalar[j].colliderect(dusman2):
                if ses == "True":
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman2.x = 100000
                puan = puan + 1
                dusman_sayisi -=1
                break
            
            if bombalar[j].colliderect(dusman3):
                if ses == "True":
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman3.x = 100000
                puan = puan + 1
                dusman_sayisi -=1
                break

            if bombalar[j].colliderect(dusman4):
                if ses == "True":
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman4.x = 100000
                puan = puan + 1
                dusman_sayisi -=1
                break

        if seviye >= 10:
            if bombalar[j].colliderect(dusman1):
                if ses == "True":
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman1_can -= 1
                if dusman1_can == 0:
                    dusman1.x = 100000
                    puan = puan + 100
                    dusman_sayisi -=1
                break
            if bombalar[j].colliderect(dusman2):
                if ses == "True":
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman2_can -= 1
                if dusman2_can == 0:
                    dusman2.x = 100000
                    puan = puan + 100
                    dusman_sayisi -=1
                break

            if bombalar[j].colliderect(dusman3):
                if ses == "True":
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman3.x = 100000
                puan = puan + 1
                dusman_sayisi -=1
                break

            if bombalar[j].colliderect(dusman4):
                if ses == "True":
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman4_can -= 1
                if dusman4_can == 0:
                    dusman4.x = 100000
                    puan = puan + 100
                    dusman_sayisi -=1
                break


def update(dt):
    global mod, puan, seviye, seviye2, zorluk2, dusman_sayisi, can, new_image, dusman1_can, sure
    global dusman2_can, dusman4_can, sesli, sessiz, ses, sifirla, gemi_adami, oldurulen_gemi, oldurulen_iskelet
    carpismalar()
    if mod != "son_kazandiniz":
        sure += 1
    if mod == "son_seviye":
        can = 15
    if ilerii == "False":
        if seviye >= 1:
            buton1.image = "buton3"
        if seviye >= 2:
            buton2.image = "buton3"
        if seviye >= 3:
            buton3.image = "buton3"
        if seviye >= 4:
            buton4.image = "buton3"
        if seviye >= 5:
            buton5.image = "buton3"
        if seviye >= 6:
            buton6.image = "buton3"
        if seviye >= 7:
            buton7.image = "buton3"
        if seviye >= 8:
            buton8.image = "buton3"
        if seviye >= 9:
            buton9.image = "buton3"
        if seviye >= 10:
            buton10.image = "buton3"
        if seviye >= 11:
            buton11.image = "buton3"
        if seviye >= 12:
            buton12.image = "buton3"
        if seviye >= 13:
            buton13.image = "buton3"
        if seviye >= 14:
            buton14.image = "buton3"
        if seviye >= 15:
            buton15.image = "buton3"
        if seviye >= 16:
            buton16.image = "buton3"
        if seviye >= 17:
            buton17.image = "buton3"
        if seviye >= 18:
            buton18.image = "buton3"
        if seviye >= 19:
            buton19.image = "buton3"
        if seviye >= 20:
            buton20.image = "buton3"
        if seviye >= 21:
            buton21.image = "buton3"
    if ilerii == "True":
        if seviye >= 22:
            buton22.image = "buton3"
        if seviye >= 23:
            buton23.image = "buton3"
        if seviye >= 24:
            buton24.image = "buton3"
        if seviye >= 25:
            buton25.image = "buton3"
        if seviye >= 26:
            buton26.image = "buton3"
        if seviye >= 27:
            buton27.image = "buton3"
        if seviye >= 28:
            buton28.image = "buton3"
        if seviye >= 29:
            buton29.image = "buton3"
        if seviye >= 30:
            buton30.image = "buton3"
        if seviye >= 31:
            buton31.image = "buton3"
        if seviye >= 32:
            buton32.image = "buton3"
        if seviye >= 33:
            buton33.image = "buton3"
        if seviye >= 34:
            buton34.image = "buton3"
        if seviye >= 35:
            buton35.image = "buton3"
        if seviye >= 36:
            buton36.image = "buton3"
        if seviye >= 37:
            buton37.image = "buton3"
        if seviye >= 38:
            buton38.image = "buton3"
        if seviye >= 39:
            buton39.image = "buton3"
        if seviye >= 40:
            buton40.image = "buton3"

    if seviye < 1:
        buton1.image = "buton4"
    if seviye < 2:
        buton2.image = "buton4"
    if seviye < 3:
        buton3.image = "buton4"
    if seviye < 4:
        buton4.image = "buton4"
    if seviye < 5:
        buton5.image = "buton4"
    if seviye < 6:
        buton6.image = "buton4"
    if seviye < 7:
        buton7.image = "buton4"
    if seviye < 8:
        buton8.image = "buton4"
    if seviye < 9:
        buton9.image = "buton4"
    if seviye < 10:
        buton10.image = "buton4"
    if seviye < 11:
        buton11.image = "buton4"
    if seviye < 12:
        buton12.image = "buton4"
    if seviye < 13:
        buton13.image = "buton4"
    if seviye < 14:
        buton14.image = "buton4"
    if seviye < 15:
        buton15.image = "buton4"
    if seviye < 16:
        buton16.image = "buton4"
    if seviye < 17:
        buton17.image = "buton4"
    if seviye < 18:
        buton18.image = "buton4"
    if seviye < 19:
        buton19.image = "buton4"
    if seviye < 20:
        buton20.image = "buton4"
    if seviye < 21:
        buton21.image = "buton4"
    if seviye < 22:
        buton22.image = "buton4"
    if seviye < 23:
        buton23.image = "buton4"
    if seviye < 24:
        buton24.image = "buton4"
    if seviye < 25:
        buton25.image = "buton4"
    if seviye < 26:
        buton26.image = "buton4"
    if seviye < 27:
        buton27.image = "buton4"
    if seviye < 28:
        buton28.image = "buton4"
    if seviye < 29:
        buton29.image = "buton4"
    if seviye < 30:
        buton30.image = "buton4"
    if seviye < 31:
        buton31.image = "buton4"
    if seviye < 32:
        buton32.image = "buton4"
    if seviye < 33:
        buton33.image = "buton4"
    if seviye < 34:
        buton34.image = "buton4"
    if seviye < 35:
        buton35.image = "buton4"
    if seviye < 36:
        buton36.image = "buton4"
    if seviye < 37:
        buton37.image = "buton4"
    if seviye < 38:
        buton38.image = "buton4"
    if seviye < 39:
        buton39.image = "buton4"
    if seviye < 40:
        buton40.image = "buton4"
    if seviye == 41 and mod == "oyun":
        mod = "son_seviye"

    if mod == "menü":
        bomba2.y -= 10
    if (keyboard.left and benim_gemim.x > 40) and mod == "oyun":
        benim_gemim.x -= 20
        mermi_topu.x -= 20
    if (keyboard.right and benim_gemim.x < 760) and mod == "oyun":
        benim_gemim.x += 20
        mermi_topu.x += 20
    if keyboard.space and mod == "oyun":
        bomba = Actor("bomba")
        bomba.pos = mermi_topu.pos
        bombalar.append(bomba)
    if (keyboard.up and son_oyun_gemisi.y > 60) and (mod == "son_oyun" and adam.y > 60):
        if gemi_adami == "False":
            son_oyun_gemisi.y -= 20
            mermi_topu2.y -= 20
        else:
            adam.y -= 20
    if (keyboard.down and son_oyun_gemisi.y < 390) and (mod == "son_oyun" and adam.y < 390):
        if gemi_adami == "False":
            son_oyun_gemisi.y += 20
            mermi_topu2.y += 20
        else:
            adam.y += 20
    if (keyboard.space and mod == "son_oyun") and son_oyun_gemisi.image == "son_oyun_gemisi":
        if gemi_adami == "False":
            bomba3 = Actor("bomba2")
            bomba3.pos = mermi_topu2.pos
            bombalar2.append(bomba3)

    if (keyboard.right and adam.x <760) and gemi_adami == "True":
        adam.x += 20

    if (keyboard.left and adam.x >40) and gemi_adami == "True":
        adam.x -= 20
    
    if keyboard.x and mod == "son_oyun":
        gemi_adami= "True"

    if (keyboard.z and mod == "son_oyun") and adam.colliderect(son_oyun_gemisi):
        gemi_adami = "False"

    if gemi_adami == "True":
        son_oyun_gemisi.image = "digergemi"
    if gemi_adami == "False":
        son_oyun_gemisi.image = "son_oyun_gemisi"
        adam.x = 100
        adam.y = 200

    if mod == "oyun":
        for i in range(len(bombalar)):
            if bombalar[i].y < 0:
                bombalar.pop(i)
                break
            else:
                bombalar[i].y = bombalar[i].y - 10
    time.sleep(hiz)

    if mod == "son_oyun":
        dusman_kayik2.x -= 7
        dusman_kayik3.x -= 7
        dusman_kayik4.x -= 7
        dusman_kayik5.x -=7
        dusman_gemi_son1.x -= 7
        dusman_gemi_son2.x -= 7
        dusman_gemi_son3.x -= 7
        dusman_gemi_son4.x -= 7
        for i in range(len(bombalar2)):
            if bombalar2[i].x < 0:
                bombalar2.pop(i)
                break
            else:
                bombalar2[i].x = bombalar2[i].x + 10

    if dusman_kayik2.x <= 0:
        dusman_kayik2.x = 800

    if dusman_kayik3.x <= 0:
        dusman_kayik3.x = 900
    
    if dusman_kayik4.x <= 0:
        dusman_kayik4.x = 1500

    if dusman_kayik5.x <= 0:
        dusman_kayik5.x = 1500

    if dusman_gemi_son1.x <= 0:
        dusman_gemi_son1.x = 1000

    if dusman_gemi_son2.x <= 0:
        dusman_gemi_son2.x = 1100

    if dusman_gemi_son3.x <= 0:
        dusman_gemi_son3.x = 1250

    if dusman_gemi_son4.x <= 0:
        dusman_gemi_son4.x = 1400
    
    if mod == "son_oyun":
        if oldurulen_gemi >= 50 and oldurulen_iskelet >= 50:
            mod = "son_kazandiniz"
        if can == 0:
            mod = "son_kaybettiniz"
        if son_oyun_gemisi.colliderect(dusman_gemi_son1):
            if ses == "True":
                sounds.patlama2.play()
            can -= 1
            dusman_gemi_son1.x = -5
            oldurulen_gemi += 1

        if son_oyun_gemisi.colliderect(dusman_gemi_son2):
            if ses == "True":
                sounds.patlama2.play()
            can -= 1
            dusman_gemi_son2.x = -5
            oldurulen_gemi += 1

        if son_oyun_gemisi.colliderect(dusman_gemi_son3):
            if ses == "True":
                sounds.patlama2.play()
            can -= 1
            dusman_gemi_son3.x = -5
            oldurulen_gemi += 1

        if son_oyun_gemisi.colliderect(dusman_gemi_son4):
            if ses == "True":
                sounds.patlama2.play()
            can -= 1
            dusman_gemi_son4.x = -5
            oldurulen_gemi += 1


        if son_oyun_gemisi.colliderect(dusman_kayik2):
            if ses == "True":
                sounds.patlama2.play()
            can -= 1
            dusman_kayik2.x = -5
            oldurulen_iskelet += 1

        if son_oyun_gemisi.colliderect(dusman_kayik3):
            if ses == "True":
                sounds.patlama2.play()
            can -= 1
            dusman_kayik3.x = -5
            oldurulen_iskelet += 1

        if son_oyun_gemisi.colliderect(dusman_kayik4):
            if ses == "True":
                sounds.patlama2.play()
            can -= 1
            dusman_kayik4.x = -5
            oldurulen_iskelet += 1
        
        if son_oyun_gemisi.colliderect(dusman_kayik5):
            if ses == "True":
                sounds.patlama2.play()
            can -= 1
            dusman_kayik5.x = -5
            oldurulen_iskelet += 1


    if mod == "oyun":
        dusman1.y = dusman1.y + 10 - hiz
        dusman2.y = dusman2.y + 10 - hiz
        dusman3.y = dusman3.y + 10 - hiz
        dusman4.y = dusman4.y + 10 - hiz

        if dusman1.y >= 500:
            dusman1.y = HEIGHT - 550
            
        if dusman2.y >= 500:
            dusman2.y = HEIGHT - 550
            
        if dusman3.y >= 500:
            dusman3.y = HEIGHT - 530
            
        if dusman4.y >= 500:
            dusman4.y = HEIGHT - 530

        if seviye <= 9:
            if benim_gemim.colliderect(dusman1):
                if ses == "True":
                    sounds.patlama2.play()
                dusman1.x = 10000
                can -= 1
                dusman_sayisi -= 1
                puan += 1
                puan_guncelle(puan)

            elif benim_gemim.colliderect(dusman2):
                if ses == "True":
                    sounds.patlama2.play()
                dusman2.x = 100000
                can -= 1
                dusman_sayisi -= 1
                puan += 1
                puan_guncelle(puan)

            elif benim_gemim.colliderect(dusman3):
                if ses == "True":
                    sounds.patlama2.play()
                dusman3.x = 100000
                can -= 1
                dusman_sayisi -= 1
                puan += 1
                puan_guncelle(puan)

            elif benim_gemim.colliderect(dusman4):
                if ses == "True":
                    sounds.patlama2.play()
                dusman4.x = 100000
                can -= 1
                dusman_sayisi -= 1
                puan += 1
                puan_guncelle(puan)

            if can == 0:
                mod = "kaybettin"

            if dusman_sayisi == 0:
                mod = "kazandiniz"
                seviye2 += 1
                puan_guncelle(puan)


        if seviye >= 10:
            if benim_gemim.colliderect(dusman1):
                if ses == "True":
                    sounds.patlama2.play()
                dusman1_can -= 1
                if dusman1_can == 0:
                    dusman1.x = 100000
                    dusman_sayisi -= 1
                    puan += 1
                    puan_guncelle(puan)
                can -= 1

            elif benim_gemim.colliderect(dusman2):
                if ses == "True":
                    sounds.patlama2.play()
                dusman2_can -= 1
                if dusman2_can == 0:
                    dusman2.x = 100000
                    can -= 1
                    dusman_sayisi -= 1
                    puan += 1
                    puan_guncelle(puan)
                can -= 1

            elif benim_gemim.colliderect(dusman3):
                if ses == "True":
                    sounds.patlama2.play()
                dusman3.x = 100000
                can -= 1
                dusman_sayisi -= 1
                puan += 1
                puan_guncelle(puan)

            elif benim_gemim.colliderect(dusman4):
                if ses == "True":
                    sounds.patlama2.play()
                dusman4_can -= 1
                if dusman4_can == 0:
                    dusman4.x = 100000
                    dusman_sayisi -= 1
                    puan += 1
                    puan_guncelle(puan)
                can -= 1
                

            if can == 0:
                mod = "kaybettin"

            if dusman_sayisi == 0:
                mod = "kazandiniz"
                seviye2 += 1

    if mod == "menü":
        if bomba2.colliderect(b_gemi):
            if ses == "True":
                sounds.patlama2.play()
            b_gemi.image = "patlama"
            if bomba2.y == 270:
                time.sleep(0.5)
                b_gemi.image = "tas1"
                bomba2.y = 420


    if mod == "oyun" and seviye >= 10:
        zorluk2 = "True"

    if mod == "oyun" and zorluk2 == "True":
        dusman1.image = "tas1"
        dusman2.image = "tas2"
        dusman4.image = "tas4"
        dusman1.y = dusman1.y + 10
        dusman2.y = dusman2.y + 10
        dusman4.y = dusman4.y + 10

    if seviye >= 20:
        dusman1.y = dusman1.y + 20
        dusman2.y = dusman2.y + 20
        dusman4.y = dusman4.y + 20
        
        

def on_mouse_down(button, pos):
    global mod, puan, seviye, dusman_sayisi, can, new_image, dusman1_can, dusman2_can, dusman4_can, sesli, sessiz, ses, sifirla
    global alinabilecek12, alinabilecek22, alinabilecek32, alinabilecek42, zorluk2, super_patlama, sesli, sessiz, ses, sifirla
    global basim, ilerii, sayim1, sayim2, sayim3, sayim4, basim_artisi, kazanmak, hiz, seviye2, sayim, oldurulen_iskelet
    global oldurulen_gemi

    if mod == "menü" and oyna.collidepoint(pos):
        mod = "deneme"
        time.sleep(0.5)
        mod = "seviye_sec"
    if ilerii == "False":
        if (mod == "seviye_sec" and buton1.collidepoint(pos)) and buton1.image == "buton3":
            seviye = 1
            mod = "oyun"

        if (mod == "seviye_sec" and buton2.collidepoint(pos)) and buton2.image == "buton3":
            seviye = 2
            mod = "oyun"
        
        if (mod == "seviye_sec" and buton3.collidepoint(pos)) and buton3.image == "buton3":
            seviye = 3
            mod = "oyun"

        if (mod == "seviye_sec" and buton4.collidepoint(pos)) and buton4.image == "buton3":
            seviye = 4
            mod = "oyun"
        
        if (mod == "seviye_sec" and buton5.collidepoint(pos)) and buton5.image == "buton3":
            seviye = 5
            mod = "oyun"

        if mod == "son_oyun" and carpi.collidepoint(pos):
            mod = "menü"

        if (mod == "seviye_sec" and buton6.collidepoint(pos)) and buton6.image == "buton3":
            seviye = 6
            mod = "oyun"
        
        if (mod == "seviye_sec" and buton7.collidepoint(pos)) and buton7.image == "buton3":
            seviye = 7
            mod = "oyun"

        if (mod == "seviye_sec" and buton8.collidepoint(pos)) and buton8.image == "buton3":
            sayim += 1
            if sayim == 2:
                seviye = 8
                mod = "oyun"

        if (mod == "seviye_sec" and buton9.collidepoint(pos)) and buton9.image == "buton3":
            sayim1 += 1
            if sayim1 == 2:
                seviye = 9
                mod = "oyun"

        if (mod == "seviye_sec" and buton10.collidepoint(pos)) and buton10.image == "buton3":
            seviye = 10
            mod = "oyun"

        if (mod == "seviye_sec" and buton11.collidepoint(pos)) and buton11.image == "buton3":
            seviye = 11
            mod = "oyun"

        if (mod == "seviye_sec" and buton12.collidepoint(pos)) and buton12.image == "buton3":
            seviye = 12
            mod = "oyun"

        if (mod == "seviye_sec" and buton13.collidepoint(pos)) and buton13.image == "buton3":
            seviye = 13
            mod = "oyun"

        if (mod == "seviye_sec" and buton14.collidepoint(pos)) and buton14.image == "buton3":
            seviye = 14
            mod = "oyun"

        if (mod == "seviye_sec" and buton15.collidepoint(pos)) and buton15.image == "buton3":
            seviye = 15
            mod = "oyun"

        if (mod == "seviye_sec" and buton16.collidepoint(pos)) and buton16.image == "buton3":
            seviye = 16
            mod = "oyun"

        if (mod == "seviye_sec" and buton17.collidepoint(pos)) and buton17.image == "buton3":
            seviye = 17
            mod = "oyun"

        if (mod == "seviye_sec" and buton18.collidepoint(pos)) and buton18.image == "buton3":
            seviye = 18
            mod = "oyun"

        if (mod == "seviye_sec" and buton19.collidepoint(pos)) and buton19.image == "buton3":
            seviye = 19
            mod = "oyun"

        if (mod == "seviye_sec" and buton20.collidepoint(pos)) and buton20.image == "buton3":
            seviye = 20
            mod = "oyun"

        if (mod == "seviye_sec" and buton21.collidepoint(pos)) and buton21.image == "buton3":
            seviye = 21
            mod = "oyun"

    if ilerii == "True":
        if (mod == "seviye_sec" and buton22.collidepoint(pos)) and buton22.image == "buton3":
            seviye = 22
            mod = "oyun"

        if (mod == "seviye_sec" and buton23.collidepoint(pos)) and buton23.image == "buton3":
            seviye = 23
            mod = "oyun"

        if (mod == "seviye_sec" and buton24.collidepoint(pos)) and buton24.image == "buton3":
            seviye = 24
            mod = "oyun"

        if (mod == "seviye_sec" and buton25.collidepoint(pos)) and buton25.image == "buton3":
            seviye = 25
            mod = "oyun"

        if (mod == "seviye_sec" and buton26.collidepoint(pos)) and buton26.image == "buton3":
            seviye = 26
            mod = "oyun"

        if (mod == "seviye_sec" and buton27.collidepoint(pos)) and buton27.image == "buton3":
            seviye = 27
            mod = "oyun"

        if (mod == "seviye_sec" and buton28.collidepoint(pos)) and buton28.image == "buton3":
            seviye = 28
            mod = "oyun"

        if (mod == "seviye_sec" and buton29.collidepoint(pos)) and buton29.image == "buton3":
            sayim3 += 1
            if sayim3 == 2:
                seviye = 29
                mod = "oyun"

        if (mod == "seviye_sec" and buton30.collidepoint(pos)) and buton30.image == "buton3":
            sayim4 += 1
            if sayim4 == 2:
                seviye = 30
                mod = "oyun"

        if (mod == "seviye_sec" and buton31.collidepoint(pos)) and buton31.image == "buton3":
            seviye = 31
            mod = "oyun"

        if (mod == "seviye_sec" and buton32.collidepoint(pos)) and buton32.image == "buton3":
            seviye = 32
            mod = "oyun"

        if (mod == "seviye_sec" and buton33.collidepoint(pos)) and buton33.image == "buton3":
            seviye = 33
            mod = "oyun"

        if (mod == "seviye_sec" and buton34.collidepoint(pos)) and buton34.image == "buton3":
            seviye = 34
            mod = "oyun"

        if (mod == "seviye_sec" and buton35.collidepoint(pos)) and buton35.image == "buton3":
            seviye = 35
            mod = "oyun"

        if (mod == "seviye_sec" and buton36.collidepoint(pos)) and buton36.image == "buton3":
            seviye = 36
            mod = "oyun"

        if (mod == "seviye_sec" and buton37.collidepoint(pos)) and buton37.image == "buton3":
            seviye = 37
            mod = "oyun"

        if (mod == "seviye_sec" and buton38.collidepoint(pos)) and buton38.image == "buton3":
            seviye = 38
            mod = "oyun"

        if (mod == "seviye_sec" and buton39.collidepoint(pos)) and buton39.image == "buton3":
            seviye = 39
            mod = "oyun"

        if (mod == "seviye_sec" and buton40.collidepoint(pos)) and buton40.image == "buton3":
            seviye = 40
            mod = "oyun"

        if (mod == "seviye_sec" and bonus_buton.collidepoint(pos)) and bonus_buton.image == "buton3":
            mod = "son_seviye"

    if mod == "menü" and bilgi.collidepoint(pos):
        mod = "hakkinda"
        
    if mod == "hakkinda" and c_gemi.collidepoint(pos):
        webbrowser.open("https://yigittalhagurbuz123.github.io/Korsan-Avi-Sitesi/nasil-oynan%C4%B1r.html")

    if mod == "oyun" and carpi.collidepoint(pos):
        mod = "menü"
        sayim = 0
        sayim1 = 0
        sayim3 = 0
        sayim4 = 0

    if mod == "hakkinda" and carpi.collidepoint(pos):
        mod = "menü"

    if mod == "menü" and dukkan.collidepoint(pos):
        mod = "dükkan"

    if mod == "dükkan" and carpi.collidepoint(pos):
        mod = "menü"

    if mod == "menü" and koleksiyon.collidepoint(pos):
        mod = "koleksiyon"

    if mod == "kazandiniz" and carpi.collidepoint(pos):
        sayim = 0
        sayim1 = 0
        sayim3 = 0
        sayim4 = 0
        if seviye == 40:
            mod = "menü"
            sayim = 0
            sayim1 = 0
            sayim3 = 0
            sayim4 = 0
        mod = "menü"
    
    if mod == "kaybettin" and carpi.collidepoint(pos):
        sayim = 0
        sayim1 = 0
        sayim3 = 0
        sayim4 = 0
        mod = "menü"

    if mod == "koleksiyon" and carpi.collidepoint(pos):
        mod = "menü"

    if mod == "dükkan" and alinabilecek1.collidepoint(pos):
        if puan >= 50:
            benim_gemim.image = "kullan1"
            alinabilecek12 = "True"
            a_12_guncelle(alinabilecek12)
            puan -= 50
            puan_guncelle(puan)
            alinabilecek1.y = 130
            animate(alinabilecek1, tween='bounce_end', duration=0.5, y=150)

    if mod == "dükkan" and alinabilecek2.collidepoint(pos):
        if puan >= 100:
            benim_gemim.image = "kullan2"
            alinabilecek22 = "True"
            a_22_guncelle(alinabilecek22)
            puan -= 100
            puan_guncelle(puan)
            alinabilecek2.y = 230
            animate(alinabilecek2, tween='bounce_end', duration=0.5, y=250)

    if mod == "dükkan" and alinabilecek3.collidepoint(pos):
        if puan >= 150:
            benim_gemim.image = "kullan3"
            alinabilecek32 = "True"
            a_32_guncelle(alinabilecek32)
            puan -= 150
            puan_guncelle(puan)
            alinabilecek3.y = 130
            animate(alinabilecek3, tween='bounce_end', duration=0.5, y=150)

    if mod == "dükkan" and alinabilecek4.collidepoint(pos):
        if puan >= 200:
            benim_gemim.image = "kullan4"
            alinabilecek42 = "True"
            a_42_guncelle(alinabilecek42)
            puan -= 200
            puan_guncelle(puan)
            alinabilecek4.y = 230
            animate(alinabilecek4, tween='bounce_end', duration=0.5, y=250)

    if (mod == "kazandiniz" and seviye <= 39) and oyna2.collidepoint(pos):
        sayim = 0
        sayim1 = 0
        sayim3 = 0
        sayim4 = 0
        mod = "oyun"
        if mod == "oyun" and seviye <= 9:
            benim_gemim.x = 400
            mermi_topu.x = 400
            seviye += 1
            puan_guncelle(puan)
            seviye_guncelle(seviye)
            dusman_sayisi = 4
            can = 3
            dusman1.y = HEIGHT - 175
            dusman1.x = 100
            dusman2.y = HEIGHT - 700
            dusman2.x = 300
            dusman3.y = HEIGHT - 550
            dusman3.x = 500
            dusman4.y = HEIGHT - 920
            dusman4.x = 700

        if mod == "oyun" and seviye >= 10:
            benim_gemim.x = 400
            mermi_topu.x = 400
            seviye += 1
            puan_guncelle(puan)
            seviye_guncelle(seviye)
            dusman_sayisi = 4
            can = 3
            dusman1_can = 3
            dusman2_can = 3
            dusman4_can = 3
            dusman1.y = HEIGHT - 175
            dusman1.x = 100
            dusman2.y = HEIGHT - 700
            dusman2.x = 300
            dusman3.y = HEIGHT - 550
            dusman3.x = 500
            dusman4.y = HEIGHT - 920
            dusman4.x = 700
        
    if mod == "kaybettin" and geri_don.collidepoint(pos):
        mod = "oyun"
        sayim = 0
        sayim1 = 0
        sayim3 = 0
        sayim4 = 0
        if mod == "oyun" and seviye <= 9:
            benim_gemim.x = 400
            mermi_topu.x = 400
            dusman_sayisi = 4
            can = 3
            dusman1_can = 3
            dusman2_can = 3
            dusman4_can = 3
            dusman1.y = HEIGHT - 175
            dusman1.x = 100
            dusman2.y = HEIGHT - 700
            dusman2.x = 300
            dusman3.y = HEIGHT - 550
            dusman3.x = 500
            dusman4.y = HEIGHT - 920
            dusman4.x = 700

        if mod == "oyun" and seviye >= 10:
            benim_gemim.x = 400
            mermi_topu.x = 400
            dusman_sayisi = 4
            can = 3
            dusman1_can = 3
            dusman2_can = 3
            dusman4_can = 3
            dusman1.y = HEIGHT - 175
            dusman1.x = 100
            dusman2.y = HEIGHT - 700
            dusman2.x = 300
            dusman3.y = HEIGHT - 550
            dusman3.x = 500
            dusman4.y = HEIGHT - 920
            dusman4.x = 700

    if mod == "koleksiyon" and alinabilecek1.collidepoint(pos):
        benim_gemim.image = "kullan1"
        alinabilecek12 = "True"
        seviye_guncelle(seviye)
        alinabilecek1.y = 130
        animate(alinabilecek1, tween='bounce_end', duration=0.5, y=150)

    if mod == "koleksiyon" and alinabilecek2.collidepoint(pos):
        benim_gemim.image = "kullan2"
        alinabilecek22 = "True"
        a_22_guncelle(alinabilecek22)
        alinabilecek2.y = 230
        animate(alinabilecek2, tween='bounce_end', duration=0.5, y=250)

    if mod == "koleksiyon" and alinabilecek3.collidepoint(pos):
        benim_gemim.image = "kullan3"
        alinabilecek32 = "True"
        a_32_guncelle(alinabilecek32)
        alinabilecek3.y = 130
        animate(alinabilecek3, tween='bounce_end', duration=0.5, y=150)

    if mod == "koleksiyon" and alinabilecek4.collidepoint(pos):
        benim_gemim.image = "kullan4"
        alinabilecek42 = "True"
        a_42_guncelle(alinabilecek42)
        alinabilecek4.y = 230
        animate(alinabilecek4, tween='bounce_end', duration=0.5, y=250)

    if mod == "ayarlar" and sesli.collidepoint(pos):
        ses = "True"
        ses_guncelle(ses)
        sesli.y = 230
        animate(sesli, tween='bounce_end', duration=0.5, y=250)

    if mod == "ayarlar" and sessiz.collidepoint(pos):
        ses = "False"
        ses_guncelle(ses)
        sessiz.y = 230
        animate(sessiz, tween='bounce_end', duration=0.5, y=250)

    if mod == "ayarlar" and sifirla.collidepoint(pos):
        mod = "menü"
        benim_gemim.x = 400
        mermi_topu.x = 400
        puan = 0
        puan_guncelle(puan)
        basim = 0
        seviye = 1
        seviye_guncelle(seviye)
        dusman_sayisi = 4
        basim_artisi = 0.5
        basim_artisi_guncelle(basim_artisi)
        ses = "True"
        ses_guncelle(ses)
        can = 3
        benim_gemim.image = "normal_gemi"
        dusman1_can = 3
        dusman2_can = 3
        dusman4_can = 3
        dusman1.y = HEIGHT - 175
        dusman1.x = 100
        dusman2.y = HEIGHT - 700
        dusman2.x = 300
        dusman3.y = HEIGHT - 550
        dusman3.x = 500
        dusman4.y = HEIGHT - 920
        dusman4.x = 700
        sifirla.y = 370
        alinabilecek12 = "False"
        a_12_guncelle(alinabilecek12)
        alinabilecek22 = "False"
        a_22_guncelle(alinabilecek22)
        alinabilecek32 = "False"
        a_32_guncelle(alinabilecek32)
        alinabilecek42 = "False"
        a_42_guncelle(alinabilecek42)

    if mod == "menü" and ayarlar.collidepoint(pos):
        mod = "ayarlar"

    if mod == "ayarlar" and carpi.collidepoint(pos):
        mod = "menü"

    if mod == "son_seviye" and carpi.collidepoint(pos):
        mod = "menü"
        sayim = 0
        sayim2 = 0
        sayim1 = 0
        sayim3 = 0
        sayim4 = 0

    if mod == "son_seviye" and bonus_oyna.collidepoint(pos):
        mod = "son_oyun"

    if mod == "seviye_sec" and carpi.collidepoint(pos):
        mod = "menü"
        ilerii = "False"
        sayim = 0
        sayim1 = 0
        sayim3 = 0
        sayim4 = 0

    if mod == "menü" and para_birimi.collidepoint(pos):
        mod = "para"

    if mod == "para" and carpi.collidepoint(pos):
        mod = "menü"

    if mod == "seviye_sec" and ileri.collidepoint(pos):
        ilerii = "True"

    if mod == "seviye_sec" and ileri2.collidepoint(pos):
        ilerii = "False"

    if bonus_1.collidepoint(pos):
        if puan >= 100:
            puan -= 100
            puan_guncelle(puan)
            basim_artisi = 1
            basim_artisi_guncelle(basim_artisi)
            bonus_1.y = 75
            animate(bonus_1, tween='bounce_end', duration=0.5, y=100)

    if bonus_2.collidepoint(pos):
        if puan >= 300:
            puan -= 300
            puan_guncelle(puan)
            basim_artisi = 2
            basim_artisi_guncelle(basim_artisi)
            bonus_2.y = 200
            animate(bonus_2, tween='bounce_end', duration=0.5, y=225)

    if bonus_3.collidepoint(pos):
        if puan >= 500:
            puan -= 500
            puan_guncelle(puan)
            basim_artisi = 3
            basim_artisi_guncelle(basim_artisi)
            bonus_3.y = 325
            animate(bonus_3, tween='bounce_end', duration=0.5, y=350)

    if mod == "para" and puan_gemisi.collidepoint(pos):
        puan += basim_artisi
        puan_guncelle(puan)
        basim += basim_artisi
        puan_gemisi.y = 220
        animate(puan_gemisi, tween='bounce_end', duration=0.5, y=200)

    if mod == "son_seviye" and bonus_oyna.collidepoint(pos):
        mod = "oyun"


    if (mod == "kazandiniz" and kazanmak == 1) and oyna3.collidepoint(pos):
        mod = "menü"
        seviye += 1
        puan_guncelle(puan)
        seviye_guncelle(seviye)

    if mod == "son_kaybettiniz" and geri_don2.collidepoint(pos):
        mod = "son_seviye"
        oldurulen_gemi = 0
        oldurulen_iskelet = 0
        can = 15


pgzrun.go()