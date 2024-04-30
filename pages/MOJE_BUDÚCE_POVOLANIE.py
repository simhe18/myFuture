import streamlit

bankovnictvo=0
ekonomika=0
it=0
manazment=0
marketing=0
obchod=0
cestovny_ruch=0
doprava=0
socialna_starostlivost=0
sportovy_odbornik=0
pedagog=0
zdravotnictvo=0
architektura=0
veterinar=0
banska_cinnost=0
remeselne_zivnosti=0

#streamlit run "c:/Users/Ja/Desktop/bakalárka projekt/HOME.py"
import streamlit as st

### 1 otázka
# Title of the form
st.title('Questionnaire')

# Create the form with radio buttons for the answer options
answer_pohlavie = st.radio('1.Pohlavie', ['dievča', 'chlapec'])


### 2 otázka
import streamlit as st
answer_byvanie = st.radio('2.Kde bývaš?', ['mesto', 'dedina'])


### 3 otazka
options = ['3.ročník', '4.ročník', '5.ročník', '6.ročník', '7.ročník', '8.ročník', '9.ročník']
answer_rocnik = st.radio('3.Ktorý ročník ZŠ navštevuješ?', options)

### 4 otazka
options = [
    'hrám sa s priateľmi spoločenské hry',
    'hrám sa vonku s priateľmi',
    'čítam knihu',
    'kreslím alebo maľujem',
    'hrám videohry',
    'venujem sa športu',
    'počúvam hudbu',
    'oddychujem a zabávam sa pozeraním televízora',
    'tvorím a modelujem rôzne projekty'
]
answers_volno = st.radio('4.Čo najradšej robíš vo svojom voľnom čase?', options)
if answers_volno == 'hrám sa s priateľmi spoločenské hry':
    marketing = marketing+1
    bankovnictvo = bankovnictvo+1
    obchod = obchod+1
    socialna_starostlivost = socialna_starostlivost+1
    zdravotnictvo = zdravotnictvo+1

elif answers_volno == 'hrám sa vonku s priateľmi':
    sportovy_odbornik = sportovy_odbornik+1
    remeselne_zivnosti = remeselne_zivnosti+1
    banska_cinnost = banska_cinnost+1
    obchod = obchod+1
    cestovny_ruch = cestovny_ruch+1
    socialna_starostlivost = socialna_starostlivost+1
    veterinar = veterinar+1

elif answers_volno == 'čítam knihu':
    pedagog = pedagog+1
    ekonomika = ekonomika+1
    doprava = doprava+1
    socialna_starostlivost = socialna_starostlivost+1
    zdravotnictvo = zdravotnictvo+1
    veterinar = veterinar+1
    remeselne_zivnosti = remeselne_zivnosti+1
elif answers_volno == 'kreslím alebo maľujem':
    architektura = architektura+1
    marketing = marketing+1
    pedagog = pedagog+1
    veterinar = veterinar+1
    remeselne_zivnosti = remeselne_zivnosti+1
elif answers_volno == 'hrám videohry':
    it = it+1
    banska_cinnost = banska_cinnost+1
elif answers_volno ==  'venujem sa športu':
    sportovy_odbornik = sportovy_odbornik+1
    cestovny_ruch = cestovny_ruch+1
    veterinar = veterinar+1
    remeselne_zivnosti = remeselne_zivnosti+1
elif answers_volno == 'počúvam hudbu':
    it = it+1
    remeselne_zivnosti = remeselne_zivnosti+1
    sportovy_odbornik = sportovy_odbornik+1
elif answers_volno == 'oddychujem a zabávam sa pozeraním televízora':
    it = it+1
    doprava = doprava+1
    cestovny_ruch = cestovny_ruch+1
elif answers_volno == 'tvorím a modelujem rôzne projekty':
    architektura = architektura+1
    pedagog = pedagog+1
    banska_cinnost = banska_cinnost+1
else:
    pass


### 5 otazka
options = [
    'Matematika',
    'Jazyk a literatúra',
    'Vedecké predmety (biológia, chémia, fyzika)',
    'Hudba',
    'Telesná výchova',
    'Výtvarná výchova',
    'Dejepis',
    'Technické predmety (informatika, technická výchova)',
    'Jazyky'
    
]
answer_predmet = st.radio('5.Aký je tvoj obľúbený predmet v škole?', options)
if answer_predmet == 'Matematika':
    bankovnictvo = bankovnictvo+1
    ekonomika = ekonomika+1
    manazment = manazment+1
    marketing = marketing+1
    architektura = architektura+1
    it = it+1
elif answer_predmet == 'Jazyk a literatúra':
    remeselne_zivnosti = remeselne_zivnosti+1
    pedagog = pedagog+1
elif answer_predmet == 'Vedecké predmety (biológia, chémia, fyzika)':
    banska_cinnost = banska_cinnost+1
    veterinar = veterinar+1
    architektura = architektura+1
    zdravotnictvo = zdravotnictvo+1
elif answer_predmet == 'Hudba':
    remeselne_zivnosti = remeselne_zivnosti+1
    pedagog = pedagog+1
elif answer_predmet == 'Telesná výchova':
    remeselne_zivnosti = remeselne_zivnosti+1
    sportovy_odbornik = sportovy_odbornik+1
    pedagog = pedagog+1
elif answer_predmet == 'Výtvarná výchova':
    marketing = marketing+1
    doprava = doprava+1
    remeselne_zivnosti=remeselne_zivnosti+1
    pedagog = pedagog+1
    architektura = architektura+1
elif answer_predmet == 'Dejepis':
    bankovnictvo = bankovnictvo+1
    ekonomika = ekonomika+1
    it = it+1
    pedagog = pedagog+1
    architektura = architektura+1
    banska_cinnost = banska_cinnost+1
elif answer_predmet == 'Technické predmety (informatika, technická výchova)':
    it = it+1
    obchod = obchod+1
    doprava = doprava+1
    pedagog = pedagog+1
    architektura = architektura+1
    remeselne_zivnosti = remeselne_zivnosti+1
elif answer_predmet == 'Jazyky':
    bankovnictvo = bankovnictvo+1
    ekonomika = ekonomika+1
    remeselne_zivnosti = remeselne_zivnosti+1
    it = it+1
    marketing = marketing+1
    manazment = manazment+1
    cestovny_ruch = cestovny_ruch+1
    doprava = doprava+1
else:
    pass

### 6 otazka
options = [
    'hra so stavebnicou',
    'hra na povolania lekár/veterinár',
    'role-playing hra',
    'športové hry',
    'vytváranie príbehov alebo scenárov',
    'vedecké hry',
    'výtvarné hry',
    'logické hry'
    
]
answer_hra = st.radio('6.Ktorá hra ťa baví najviac?', options)
if answer_hra == 'hra so stavebnicou':
    architektura = architektura+1
elif answer_hra == 'hra na povolania lekár/veterinár':
    zdravotnictvo = zdravotnictvo+1
    veterinar = veterinar+1
    socialna_starostlivost = socialna_starostlivost+1
elif answer_hra == 'role-playing hra':
    bankovnictvo = bankovnictvo+1
    manazment = manazment+1
    marketing = marketing+1
    obchod = obchod+1
elif answer_hra == 'športové hry':
    sportovy_odbornik = sportovy_odbornik+1
    remeselne_zivnosti = remeselne_zivnosti+1
elif answer_hra ==  'vytváranie príbehov alebo scenárov':
    remeselne_zivnosti = remeselne_zivnosti+1
    pedagog = pedagog+1
elif answer_hra == 'vedecké hry':
    banska_cinnost = banska_cinnost+1
    pedagog = pedagog+1
elif answer_hra == 'výtvarné hry':
    remeselne_zivnosti = remeselne_zivnosti+1
    marketing = marketing+1
    cestovny_ruch = cestovny_ruch+1
elif answer_hra == 'logické hry':
    ekonomika = ekonomika+1
    it = it+1
    doprava = doprava+1
    architektura = architektura+1

else:
    pass

### 7 otazka 
options = [
    'Fantasy a Sci-fi film',
    'Animovaný film',
    'Dobrodružný film',
    'Dokumentárny film',
    'Romantický film',
    'Historický film',
    'Akčný film',
    'Komédia'
    
]
answer_film = st.radio('7.Ktorý film ťa baví najviac?', options)
if answer_film == 'Fantasy a Sci-fi film':
    architektura = architektura+1
    banska_cinnost = banska_cinnost+1
elif answer_film == 'Animovaný film':
    pedagog = pedagog+1
    socialna_starostlivost = socialna_starostlivost+1
    marketing = marketing+1
    obchod = obchod+1
elif answer_film == 'Dobrodružný film':
    cestovny_ruch = cestovny_ruch+1
    doprava = doprava+1
    sportovy_odbornik = sportovy_odbornik+1
elif answer_film == 'Dokumentárny film':
    banska_cinnost = banska_cinnost+1
    veterinar = veterinar+1
    zdravotnictvo = zdravotnictvo+1
    pedagog = pedagog+1
    socialna_starostlivost = socialna_starostlivost+1
elif answer_film == 'Romantický film':
    marketing = marketing+1
    bankovnictvo = bankovnictvo+1
    obchod = obchod+1
    cestovny_ruch = cestovny_ruch+1
elif answer_film == 'Historický film':
    ekonomika = ekonomika+1
    marketing = marketing+1
    cestovny_ruch = cestovny_ruch+1
    pedagog = pedagog+1
    architektura = architektura+1
    banska_cinnost = banska_cinnost+1
elif answer_film == 'Akčný film':
    banska_cinnost = banska_cinnost+1
    zdravotnictvo = zdravotnictvo+1
    sportovy_odbornik = sportovy_odbornik+1
    cestovny_ruch = cestovny_ruch+1
elif answer_film == 'Komédia':
    marketing = marketing+1
    obchod = obchod+1
    doprava = doprava+1
    remeselne_zivnosti = remeselne_zivnosti+1

else:
    pass

### 8 otazka
options = [
    'na exotickú pláž/ostrov',
    'do veľkého mesta',
    'do národného parku',
    'do historického mesta',
    'na hory',
    'do džungle/tropického lesa',
    'do krajiny s exotickou kuchyňou',
    'na festival',
    'do vesmíru',
    'do polárnych oblastí'
    
]
answer_destinacia = st.radio('8.Kam by si najradšej cestoval/-a?', options)
if answer_destinacia == 'na exotickú pláž/ostrov':
    it = it+1
    marketing = marketing+1
    zdravotnictvo = zdravotnictvo+1
elif answer_destinacia == 'do veľkého mesta':
    bankovnictvo = bankovnictvo+1
    ekonomika = ekonomika+1
    it = it+1
    marketing = marketing+1
elif answer_destinacia == 'do národného parku':
    veterinar = veterinar+1
    cestovny_ruch = cestovny_ruch+1
elif answer_destinacia == 'do historického mesta':
    architektura = architektura+1
    remeselne_zivnosti = remeselne_zivnosti+1
elif answer_destinacia == 'na hory':
    sportovy_odbornik = sportovy_odbornik+1
    socialna_starostlivost = socialna_starostlivost+1
    pedagog = pedagog+1
    banska_cinnost = banska_cinnost+1
elif answer_destinacia == 'do džungle/tropického lesa':
    veterinar = veterinar+1
    sportovy_odbornik = sportovy_odbornik+1
    it = it+1
elif answer_destinacia == 'do krajiny s exotickou kuchyňou':
    cestovny_ruch = cestovny_ruch+1
    obchod = obchod+1
elif answer_destinacia == 'na festival':
    marketing = marketing+1
    manazment = manazment+1
    remeselne_zivnosti = remeselne_zivnosti+1
    doprava = doprava+1
elif answer_destinacia == 'do vesmíru':
    doprava = doprava+1
    bankovnictvo = bankovnictvo+1
    ekonomika = ekonomika+1
    it = it+1
    manazment = manazment+1
    banska_cinnost = banska_cinnost+1
elif answer_destinacia == 'do polárnych oblastí':
    zdravotnictvo = zdravotnictvo+1
    marketing = marketing+1

else:
    pass

### 9 otazka
options = [
    'Športové aktivity: Futbal, basketbal, plávanie, gymnastika, tenis alebo iný šport',
    'Hudobné nástroje: Klavír, gitara, husle, spev alebo iný hudobný nástroj',
    'Umenie a kreatívne aktivity: Maľovanie, kreslenie, remeselné práce alebo vytváranie umeleckých diel',
    'Jazykové zručnosti',
    'Práca s chemickými látkami',
    'Programovanie a technológie: Programovanie počítačových hier, tvorba webových stránok alebo práca s technologickými zariadeniami',
    'Dramatické umenie: Herectvo, réžia, divadelné predstavenia',
    'Hranie logických hier (šach, sudoku), riešenie matematických hádaniek alebo účasť na matematických súťažiach',
    'Organizovanie udalostí, vedenie tímu alebo riadenie projektov',
    'Debaty a komunikácia'
    
]
answer_aktivita = st.radio('9.Ktorú aktivitu alebo hru hráš veľmi dobre?', options)
if answer_aktivita == 'Športové aktivity: Futbal, basketbal, plávanie, gymnastika, tenis alebo iný šport':
    sportovy_odbornik = sportovy_odbornik+1
    pedagog = pedagog+1
    zdravotnictvo = zdravotnictvo+1
elif answer_aktivita == 'Hudobné nástroje: Klavír, gitara, husle, spev alebo iný hudobný nástroj':
    remeselne_zivnosti = remeselne_zivnosti+1
    pedagog = pedagog+1
    socialna_starostlivost = socialna_starostlivost+1
elif answer_aktivita == 'Umenie a kreatívne aktivity: Maľovanie, kreslenie, remeselné práce alebo vytváranie umeleckých diel':
    remeselne_zivnosti = remeselne_zivnosti+1
    pedagog = pedagog+1
    architektura = architektura+1
    obchod = obchod+1
elif answer_aktivita == 'Jazykové zručnosti':
    bankovnictvo = bankovnictvo+1
    manazment = manazment+1
    marketing = marketing+1
    it = it+1
elif answer_aktivita == 'Práca s chemickými látkami':
    zdravotnictvo = zdravotnictvo+1
    pedagog = pedagog+1
    veterinar = veterinar+1
elif answer_aktivita == 'Programovanie a technológie: Programovanie počítačových hier, tvorba webových stránok alebo práca s technologickými zariadeniami':
    it = it+1
    ekonomika = ekonomika+1
    manazment = manazment+1
    marketing = marketing+1
elif answer_aktivita == 'Dramatické umenie: Herectvo, réžia, divadelné predstavenia':
    pedagog = pedagog+1
    remeselne_zivnosti = remeselne_zivnosti+1
elif answer_aktivita == 'Hranie logických hier (šach, sudoku), riešenie matematických hádaniek alebo účasť na matematických súťažiach':
    bankovnictvo = bankovnictvo+1
    ekonomika = ekonomika+1
    doprava = doprava+1
    obchod = obchod+1
elif answer_aktivita == 'Organizovanie udalostí, vedenie tímu alebo riadenie projektov':
    manazment = manazment+1
    marketing = marketing+1
    zdravotnictvo = zdravotnictvo+1
    pedagog = pedagog+1
elif answer_aktivita == 'Debaty a komunikácia':
    socialna_starostlivost = socialna_starostlivost+1
    remeselne_zivnosti = remeselne_zivnosti+1
    cestovny_ruch = cestovny_ruch+1
    obchod = obchod+1
    marketing = marketing+1
else:
    pass


### 10 otazka
options = [
    'učebné úspechy: dosiahol som vysoké hodnotenie z testu, zvládol som náročné učivo, zvládol som skúšku',
    'športové výkony: vyhral som zápas, dosiahol som osobný rekord',
    'vytvoril som umelecké dielo',
    'naprogramoval som aplikáciu',
    'bol som vedúcim teamu',
    'dobrovoľnícka činnosť',
    'dosiahol som osobné ciele a viac sa spoznal',
    'úspešne som prekonal svoj strach',
    'zúčastnil som sa matematickej súťaže',
    'naučil som sa niečo nové (jazyk, šport)'
    
]
answer_uspech = st.radio('10.Kedy si bol/-a hrdý/-á na niečo, čo si dokázal/-a urobiť?', options)
if answer_uspech == 'učebné úspechy: dosiahol som vysoké hodnotenie z testu, zvládol som náročné učivo, zvládol som skúšku':
    bankovnictvo = bankovnictvo+1
    ekonomika = ekonomika+1
    doprava = doprava+1
    it = it+1
elif answer_uspech == 'športové výkony: vyhral som zápas, dosiahol som osobný rekord':
    sportovy_odbornik = sportovy_odbornik+1
elif answer_uspech == 'vytvoril som umelecké dielo':
    socialna_starostlivost = socialna_starostlivost+1
    remeselne_zivnosti = remeselne_zivnosti+1
    architektura = architektura+1
elif answer_uspech == 'naprogramoval som aplikáciu':
    it = it+1
elif answer_uspech == 'bol som vedúcim teamu':
    manazment = manazment+1
    marketing = marketing+1
elif answer_uspech == 'dobrovoľnícka činnosť':
    socialna_starostlivost = socialna_starostlivost+1
    obchod = obchod+1
elif answer_uspech == 'dosiahol som osobné ciele a viac sa spoznal':
    socialna_starostlivost = socialna_starostlivost+1
    remeselne_zivnosti = remeselne_zivnosti+1
elif answer_uspech == 'úspešne som prekonal svoj strach':
    cestovny_ruch = cestovny_ruch+1
    banska_cinnost = banska_cinnost+1
elif answer_uspech == 'zúčastnil som sa matematickej súťaže':
    bankovnictvo = bankovnictvo+1
    ekonomika = ekonomika+1
    it = it+1
    manazment = manazment+1
elif answer_uspech == 'naučil som sa niečo nové (jazyk, šport)':
    zdravotnictvo = zdravotnictvo+1
    veterinar = veterinar+1
    pedagog = pedagog+1

else:
    pass

### 11 otazka
options = [
    'rodina',
    'zdravie',
    'priatelia',
    'láska',
    'vzdelanie',
    'príroda a životné prostredie',
    'mier a spravodlivosť',
    'šťastie a radosť',
    'sloboda',
    'dobrosrdečnosť a pomoc druhým'
    
]
answer_najdolezitejsie = st.radio('11.Čo je podľa teba najdôležitejšie na svete?', options)
if answer_najdolezitejsie == 'rodina':
    bankovnictvo = bankovnictvo+1
    ekonomika = ekonomika+1
    socialna_starostlivost = socialna_starostlivost+1
    pedagog = pedagog+1
elif answer_najdolezitejsie == 'priatelia':
    it = it+1
    manazment = manazment+1
    marketing = marketing+1
elif answer_najdolezitejsie == 'zdravie':
    zdravotnictvo = zdravotnictvo+1
    veterinar = veterinar+1
elif answer_najdolezitejsie == 'láska':
    pedagog = pedagog+1
    veterinar = veterinar+1
    zdravotnictvo = zdravotnictvo+1
elif answer_najdolezitejsie == 'vzdelanie':
    it = it+1
    manazment = manazment+1
    architektura = architektura+1
elif answer_najdolezitejsie == 'príroda a životné prostredie':
    veterinar = veterinar+1
    banska_cinnost = banska_cinnost+1
elif answer_najdolezitejsie ==  'mier a spravodlivosť':
    remeselne_zivnosti = remeselne_zivnosti+1
    sportovy_odbornik = sportovy_odbornik+1
    architektura = architektura+1
elif answer_najdolezitejsie == 'šťastie a radosť':
    veterinar = veterinar+1
    sportovy_odbornik = sportovy_odbornik+1
elif answer_najdolezitejsie == 'sloboda':
    cestovny_ruch = cestovny_ruch+1
    doprava = doprava+1
    sportovy_odbornik = sportovy_odbornik+1
elif answer_najdolezitejsie == 'dobrosrdečnosť a pomoc druhým':
    socialna_starostlivost = socialna_starostlivost+1
    obchod = obchod+1
    remeselne_zivnosti = remeselne_zivnosti+1

else:
    pass

### 12 otazka
options = [
    'súcitím s ľuďmi, ktorí majú ťažkosti (empatia)',
    'rád robím dobré skutky',
    'pomáhať druhým je pre mňa spoločenská zodpovednosť',
    'vznikajú nové a silné priateľstvá',
    'mám rád, keď som vzorom pre druhých',
    'radosť na oboch stranách'
    
]
answer_pomoc = st.radio('12.Prečo je dôležité pomáhať iným?', options)
if answer_pomoc == 'súcitím s ľuďmi, ktorí majú ťažkosti (empatia)':
    socialna_starostlivost = socialna_starostlivost+1
    obchod = obchod+1
elif answer_pomoc == 'rád robím dobré skutky':
    zdravotnictvo = zdravotnictvo+1
    socialna_starostlivost = socialna_starostlivost+1
    veterinar = veterinar+1
    banska_cinnost = banska_cinnost+1
elif answer_pomoc == 'pomáhať druhým je pre mňa spoločenská zodpovednosť':
    bankovnictvo = bankovnictvo+1
    ekonomika = ekonomika+1
    it = it+1
elif answer_pomoc == 'vznikajú nové a silné priateľstvá':
    manazment = manazment+1
    doprava = doprava+1
    sportovy_odbornik = sportovy_odbornik+1
elif answer_pomoc == 'mám rád, keď som vzorom pre druhých':
    manazment = manazment+1
    bankovnictvo = bankovnictvo+1
elif answer_pomoc == 'radosť na oboch stranách':
    obchod = obchod+1
    marketing = marketing+1


else:
    pass

### 13 otazka
options = [
    'ochranu životného prostredia',
    'spravodlivosť',
    'zlepšenie vzdelávania',
    'lepšiu zdravotnícku starostlivosť',
    'boj proti chudobe',
    'zlepšenie inovácií a technológií',
    'kultúrnu rozmanitosť',
    'mier a bezpečnosť',
    'zlepšenie umeleckej oblasti'
   
]
answer_svet = st.radio('13.Čo by si chcel/-a dosiahnuť, aby svet bol lepším miestom?', options)
if answer_svet == 'ochranu životného prostredia':
    zdravotnictvo = zdravotnictvo+1
    veterinar = veterinar+1
    banska_cinnost = banska_cinnost+1
    remeselne_zivnosti = remeselne_zivnosti+1
elif answer_svet ==  'spravodlivosť':
    remeselne_zivnosti = remeselne_zivnosti+1
    sportovy_odbornik = sportovy_odbornik+1
    pedagog = pedagog+1
elif answer_svet == 'zlepšenie vzdelávania':
    bankovnictvo = bankovnictvo+1
    it = it+1
    manazment = manazment+1
    pedagog = pedagog+1
elif answer_svet == 'lepšiu zdravotnícku starostlivosť':
    zdravotnictvo = zdravotnictvo+1
    veterinar = veterinar+1
elif answer_svet == 'boj proti chudobe':
    bankovnictvo = bankovnictvo+1
    marketing = marketing+1
    remeselne_zivnosti = remeselne_zivnosti+1
    socialna_starostlivost = socialna_starostlivost+1
elif answer_svet == 'zlepšenie inovácií a technológií':
    it = it+1
    marketing = marketing+1
    manazment = manazment+1
    zdravotnictvo = zdravotnictvo+1
    doprava = doprava+1
elif answer_svet == 'kultúrnu rozmanitosť':
    cestovny_ruch = cestovny_ruch+1
    it = it+1
    obchod = obchod+1
elif answer_svet == 'mier a bezpečnosť':
    it = it+1 
    manazment = manazment+1
    remeselne_zivnosti = remeselne_zivnosti+1
    doprava = doprava+1
elif answer_svet == 'zlepšenie umeleckej oblasti':
    architektura = architektura+1
    remeselne_zivnosti = remeselne_zivnosti+1

else:
    pass

### 14 otazka
#st.write('Which career field do you prefer?')
#options = [
    #'bankovníctvo (napr. bankový poradca)',
    #'ekonomika, financie, účtovníctvo (napr. audítor, daňový špecialista, účtovník)',
    #'informačné technológie (napr. programátor, IT analytik, web dizajnér)',
    #'manažment (napr. vedúci predajne, projektový manažér)',
    #'marketing a reklama (napr. grafik, marketingový analytik)',
    #'obchod a služby so zákazníkom (maklér, predavač)',
    #'cestovný ruch a hotelierstvo (napr. delegát, pracovník cestovnej kancelárie)',
    #'doprava a logistika (napr. pilot, lodný kapitán, rušňovodič, kuriér)',
    #'sociálna starostlivosť (napr. opatrovateľ)',
    #'športový odborník (napr. inštruktor, tréner)',
    #'pedagogické povolania (napr. učiteľ, vychovávateľ)',
    #'zdravotníctvo (napr. lekár, farmaceut, masér)',
    #'architektúra, stavebníctvo, geodézia (napr. architekt, stavebný dozor, geodet)',
    #'veterinárske lekárstvo (napr. veterinárny lekár, veterinárny asistent)',
    #'banská činnosť (napr. vedúci lomu, vedúci bane)',
    #'remeselné živnosti (napr. kuchár, kaderník, murár, tesár, mäsiar, manikúra)',
    
#]
#answer_kariera = st.selectbox('Ktorá oblasť povolaní sa ti páči?', options)

button_clicked = st.button("Vyhodnotenie")

# Execute the code below if the button is clicked
if button_clicked:

    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== bankovnictvo and bankovnictvo !=0:
        st.write("Najviac by si sa hodil/-a do oblasti BANKOVNICTVA, mozes byt napriklad bankovy poradca, uverovy specialista alebo pracovnik na prepazke")
    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== ekonomika and ekonomika !=0:
        st.write("Najviac by si sa hodil/-a do oblasti EKONOMIKY, FINANCII A UCTOVNICTVA, mozes byt napriklad auditor, advokat, danovy specialista, ekonom, mzdovy uctovnik, financny poradca, financny riaditel")
    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== it and it !=0:
        st.write("Najviac by si sa hodil/-a do oblasti INFORMACNYCH TECHNOLOGII, mozes byt napriklad IT analytik, testovac softveru a aplikacii, aplikacny programator, bezpecnostny specialista IT, databazovy specialista, pracovnik help desku, hardverovy kozultant, webdizajner, webmaster")
    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== manazment and manazment !=0:
        st.write("Najviac by si sa hodil/-a do oblasti MANAZMENTU, mozes byt napriklad produktovy manazer, projektovy manazer, vykonny riaditel, veduci predajne")
    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== marketing and marketing !=0:
        st.write("Najviac by si sa hodil/-a do oblasti MARKETINGU A REKLAMY, mozes byt napriklad brand manazer, copywriter, event manazer, grafik, marketingovy analytik, media planner")
    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== obchod and obchod !=0:
        st.write("Najviac by si sa hodil/-a do oblasti OBCHODU A SLUZIEB, mozes byt napriklad makler, obchodny asistent, pokladnik, pracovnik call centra, predavacka")
    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== cestovny_ruch and cestovny_ruch !=0:
        st.write("Najviac by si sa hodil/-a do oblasti CESTOVNEHO RUCHU A HOTELIERSTVA, mozes byt napriklad delegat cestovnej kancelarie, sprievodca, pracovnik za prepazkou, chyzny, casnik, recepcny")
    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== doprava and doprava !=0:
        st.write("Najviac by si sa hodil/-a do oblasti DOPRAVY A LOGISTIKY, mozes byt napriklad colny deklarant, dispecer, kurier, skladnik, spediter, taxikar, pilot, palubny sprievodca, technik lietadiel, lodny kapitan, kormidelnik, rusnovodic")
    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== socialna_starostlivost and socialna_starostlivost !=0:
        st.write("Najviac by si sa hodil/-a do oblasti SOCIALNEJ STAROSTLIVOSTI, mozes byt napriklad opatrovatel, instruktor socialnej rehabilitacie")
    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== sportovy_odbornik and sportovy_odbornik !=0:
        st.write("Najviac by si sa hodil/-a do oblasti SPORTOVEHO ODBORNIKA, mozes byt napriklad inštruktor, trener")
    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== pedagog and pedagog !=0:
        st.write("Najviac by si sa hodil/-a do oblasti PEDAGOGICKYCH POVOLANI, mozes byt napriklad ucitel (podla stupna školy), vychovavatel, korepetitor, pedagogicky asistent, školsky trener, učitel jazykovej skoly, ucitel umeleckej skoly, karierovy poradca, logoped, psycholog, socialny pedagog")
    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== zdravotnictvo and zdravotnictvo !=0:
        st.write("Najviac by si sa hodil/-a do oblasti ZDRAVOTNICTVA, mozes byt napriklad dentalny hygienik, farmaceut, fyzioterapeut, lekar, logped, maser, optometrista, ocny optik, ortopedicky technik, porodny asistent, psycholog, radiologicky technik, sanitar, sestra, zachranar, zubny asistent, zubny lekar")
    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== architektura and architektura !=0:
        st.write("Najviac by si sa hodil/-a do oblasti ARCHITEKTURY, STAVEBNICTVA, GEODEZIE, mozes byt napriklad architekt, stavebny dozor, stavbyveduci, geodet, kartograf")
    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== veterinar and veterinar !=0:
        st.write("Najviac by si sa hodil/-a do oblasti VETERINARSKEHO LEKARSTVA, mozes byt napriklad veterinarny lekar, veterinarny asistent")
    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== banska_cinnost and banska_cinnost !=0:
        st.write("Najviac by si sa hodil/-a do oblasti BANSKEJ CINNOSTI, mozes byt napriklad veduci lomu, veduci bane, strelmajster, odpalovac ohnostrojov")
    if max(bankovnictvo, ekonomika, it, manazment, marketing, obchod, cestovny_ruch, doprava, socialna_starostlivost, sportovy_odbornik, pedagog, zdravotnictvo, architektura, veterinar, banska_cinnost, remeselne_zivnosti)== remeselne_zivnosti and remeselne_zivnosti !=0 :
        st.write("Najviac by si sa hodil/-a do oblasti REMESELNYCH ZIVNOSTI, mozes byt napriklad zamocnik, hodinar, kamenar, masiar, pekar, stolar, autokarosar, zlatnik, murar, tesar, klampiar, strechar, kadernik, kuchar, kominar, manikura, pedikura, kozmeticke sluzby, kachliarstvo")

print(marketing)
print(len(answers_volno))   


