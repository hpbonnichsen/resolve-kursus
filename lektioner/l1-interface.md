# L1 · Interface og praktiske indstillinger – udkast

**09:15–09:45 · 30 minutter · Fuldt styret**

Status: udkast til gennemlæsning. Ingen HTML bygget endnu.

## Formål

Deltageren skal forlade blokken med to ting: en fornemmelse af at Resolve ikke er
ét program med faneblade, men flere programmer i samme fil, og de indstillinger på
plads, som er besværlige at rette bagefter.

Det er bevidst en kedelig blok. Den betaler sig hele resten af dagen, fordi den
fjerner de fejl der ellers dukker op kl. 13 og ingen kan forklare.

## Tidsbudget

| Del | Min |
|---|---|
| 1. Hvor er vi henne | 5 |
| 2. Project Settings – opløsning og framerate | 8 |
| 3. Preferences – lager, autosave og backup | 9 |
| 4. Farvestyring *(kun hvis materialet er log)* | 5 |
| Luft | 3 |

Uden del 4 er der 8 minutters luft. Det er formentlig realistisk at regne med, at
mindst én maskine driller i den første blok.

---

## 1. Hvor er vi henne (5 min)

Deltagerne har projektet åbent hjemmefra. Start med at få alle det samme sted hen.

**Det siges, det vises ikke som opgave:**

Nederst i programmet står en række knapper. Hver af dem skifter ikke bare panelerne
rundt. Den skifter reelt til et andet program inde i Resolve. Man klipper ét sted,
farvelægger et andet, laver lyd et tredje. Rækkefølgen er ikke tilfældig: den følger
den vej en film bliver til.

I dag bruger vi tre af dem plus den sidste. Resten kigger vi på efter pausen.

**Det de gør selv:**

1. Klik på husikonet i nederste højre hjørne. Nu er I i **Project Manager**. Det er
   her alle projekter bor, og det er her I altid kan komme tilbage til
2. Dobbeltklik på kursusprojektet for at åbne det igen

Pointen med at gå ud og ind: de skal vide at der er en vej tilbage. Det er den
hyppigste panik hos begyndere: at de tror de har mistet noget.

---

## 2. Project Settings – opløsning og framerate (8 min)

**Det siges:**

Et projekt har en opløsning og en billedhastighed. De to tal beskriver den film I
laver. Ikke de klip I lægger ind. Lægger man klip ind, der ikke passer, skalerer
Resolve dem, og så er skarpheden væk.

Framerate er den vigtige af de to, for **den kan ikke ændres, når først der ligger
noget på timelinen.** Opløsningen kan man rette bagefter. Det kan billedhastigheden
ikke.

**Det de gør selv:**

1. Klik på tandhjulet i nederste højre hjørne. Det åbner Project Settings
2. Under **Master Settings**, find **Timeline Resolution**
3. Sæt den til `1920 x 1080 HD`
4. Find **Timeline Frame Rate** lige under
5. Sæt den til `[udfyldes: skal matche råmaterialet i pakken]`
6. Klik **Save**

**Sidder du fast:** Er Timeline Frame Rate grå og kan ikke klikkes, ligger der
allerede noget på en timeline i projektet. Det er ikke noget problem i dag:
værdien er sat rigtigt i pakken på forhånd.

---

## 3. Preferences – lager, autosave og backup (9 min)

Tre indstillinger. Den første handler om hastighed, de to andre om ikke at miste
sit arbejde.

**Det siges:**

Resolve gemmer løbende af sig selv. Der er ingen "Gem som" man skal huske hver
halve time, sådan som man kender det fra Word. Til gengæld er der to ting man selv
skal slå til, og de er slået fra som standard hos nogle.

**Det de gør selv:**

1. Åbn Preferences med `Ctrl` + `,` på Windows eller `Cmd` + `,` på Mac
2. Vælg fanen **System** øverst, og derefter **Media Storage** i venstre side
3. Her står den disk, Resolve bruger til sine arbejdsfiler. Den skal være den
   hurtigste og største disk I har, og er der en ekstern SSD, er det den
4. Skift til fanen **User** øverst
5. Vælg **Project Save and Load** i venstre side
6. Tjek at der er flueben ved **Live Save**. Det er den, der gemmer løbende
7. Sæt flueben ved **Project Backups**. Den gemmer versioner tilbage i tiden, så
   man kan hoppe tilbage til i går, hvis noget går galt
8. Klik **Save**

**Sidder du fast:** Finder du ikke Preferences i menuen, er den placeret forskelligt
på Mac og Windows. Genvejen virker begge steder.

---

## 4. Farvestyring (5 min) – *kun hvis materialet er log*

**Springes over, hvis intet af råmaterialet er optaget i log.**

**Det siges:**

Nogle kameraer optager et billede der ser gråt og fladt ud med vilje. Det hedder
log, og det gemmer flere detaljer til senere. Ulempen er at det er kedeligt at
klippe i. Vi retter det nu og ikke senere, for ellers sidder I en time og vænner jer
til at det ser forkert ud.

I skal ikke forstå det. I skal sætte to menupunkter.

**Det de gør selv:**

1. Åbn Project Settings igen (tandhjulet nederst til højre)
2. Vælg **Color Management** i venstre side
3. Sæt **Color science** til `DaVinci YRGB Color Managed`
4. Klik **Save**
5. Marker alle klip i Media Pool
6. Højreklik på et af dem og vælg **Input Color Space**
7. Vælg `[udfyldes: afhænger af kameraet bag råmaterialet]`

Billedet skifter foran øjnene på dem. Det er hele pointen med at gøre det som en
øvelse frem for at have gjort det på forhånd i pakken.

---

## Skærmbilleder der skal tages

Alle fra Resolve 21. De gamle fra hæftet er version 18 og kan ikke bruges.

1. **Project Manager** med kursusprojektet synligt. Ring om husikonet i nederste
   højre hjørne
2. **Project Settings, Master Settings**. Ring om Timeline Resolution og Timeline
   Frame Rate
3. **Preferences, System → Media Storage**. Ring om disklisten
4. **Preferences, User → Project Save and Load**. Ring om Live Save og Project
   Backups
5. *(kun hvis log)* **Project Settings, Color Management**. Ring om Color science
6. *(kun hvis log)* **Højrekliksmenuen** med Input Color Space markeret

Fem til seks billeder. Det er den tætteste billeddækning på hele dagen, og det er
med vilje: her er hånden holdt hårdest.

---

## Skal afklares før siden bygges

**Framerate i pakken.** Hvilken billedhastighed er råmaterialet? Tallet skal stå i
trin 2.5, og det skal matche det, du sætter i arkivet.

**Er noget af materialet log?** Afgør om del 4 er med. Hvis ja: hvilket kamera, så
Input Color Space-valget kan skrives ud.

**Genvejen til Project Manager.** Dit hæfte fra 2022 opgiver `Shift` + `1`. Jeg har
sat den ind i genvejstabellen på `program.html`, men jeg har ikke kunnet bekræfte at
den stadig gælder i version 21. Tjek den, før den står foran tolv mennesker. Det
samme gælder placeringen af Preferences i menuen på Windows.

**Restore hjemmefra?** Forløbet her forudsætter at deltagerne møder op med projektet
åbent. Skal `Restore Project Archive` alligevel ligge på dagen, skal det ind som del
0, og så holder tidsbudgettet ikke.
