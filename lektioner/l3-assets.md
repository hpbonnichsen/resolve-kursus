# L3 – assets og timeline-opsætning

Til `lektion-3-edit.html`. Alt materiale er Efterår, 23,976 fps. Ingen skærmbilleder
på listen endnu, det tager vi når trinlisten er skrevet og teksten kan styre hvad der
skal vises.

## Svar på dit spørgsmål: tom, delvist bygget, eller start/slutning?

**Blank, ikke delvist bygget.** Begrundelsen hænger direkte sammen med researchen fra
sidst: pointen med Del 2 er at de selv gennemfører hele cyklussen (finde, markere,
lægge ned, ordne) på rigtigt materiale, efter de lige har øvet den på løsrevne klip i
Del 1. Bygger du halvdelen for dem, mister de netop den del af øvelsen, der er
formålet. Og "jeg byggede den selv" er den følelse, hele blokken skal efterlade dem
med.

Det du til gengæld skal forberede, er **råmaterialet**, ikke selve sekvensen. Det
svarer til det Blackmagic-bogen kalder subclips: klip der er trimmet ned til
overskuelige stykker på forhånd, så de ikke skal lede i ti minutters råfilm for at
finde det rigtige øjeblik. Det er forskellen mellem en øvelse i at redigere og en
øvelse i at lede.

Til gengæld bygger du to ting, der IKKE er tomme:

- **FACIT-timelinen**: den færdige scene, nøjagtig som den ser ud i filmen
- Evt. **markers** i binnen eller på en tom hjælpe-timeline, som gæt-fri fingerpeg
  uden at afsløre rækkefølgen. Det er samme greb, du selv brugte i Fairlight-kapitlet
  i 2022-hæftet ("klipperen har allerede noteret hvad der skal ordnes"), og det er
  værd at genbruge her.

## Bins der skal bygges

```
03 Edit
├── Del 1 – Øvelsesklip      3-4 klip, lav stakes, ikke en del af facit
└── Del 2 – Byg scenen
    ├── Råklip               kun det denne scene skal bruge, trimmet til subclips
    └── Timelines
        ├── FACIT            den færdige scene, låst/ikke redigerbar
        └── PUZZLE           tom. Oprettes evt. af deltagerne selv i trin 1
```

`PUZZLE`-timelinen behøver du ikke oprette på forhånd. Et af de første trin i Del 2 er
formentlig at de selv laver en ny timeline. Det er også sådan Blackmagic-bogen gør
det, og det er en god øvelse i sig selv: de skal kunne starte forfra, hvis noget går
galt.

## Del 1 – øvelsesklip

**3-4 korte klip**, ingen sammenhæng krævet mellem dem. Formålet er udelukkende at
øve mekanikken: hover for preview, dobbeltklik, JKL, sæt I/O, træk ned, swap med
genvej, og til sidst Append.

Kriterier for de klip, du vælger:

- Skal have et **tydeligt "rigtigt" øjeblik** at finde med I/O: en bevægelse, et
  klip der starter roligt og har noget der sker undervejs. Det behøver ikke være
  tale; en handling der starter og slutter tydeligt virker lige så godt.
- **10–20 sekunder råt materiale pr. klip er nok.** Længere gør blot JKL-øvelsen
  langsommere uden at lære mere.
- De skal ikke ligne hinanden. Deltagerne skal kunne genkende dem, når de skal
  swappe rækkefølgen, uden at kigge to gange.

Disse klip må gerne være outtakes eller klip, der IKKE endte i den færdige film. Det
er lav-stakes-materiale, så det er fint hvis de er lidt kedelige eller mislykkede.

## Del 2 – byg scenen

Her mangler jeg dit kendskab til selve filmen for at kunne skrive noget mere præcist,
men her er kriterierne for hvilken scene der egner sig:

**Længde:** 3-6 klip, samlet 8-15 sekunder færdig varighed. Kortere, og øvelsen
føles triviel. Længere, og 40 minutter rækker ikke for en nybegynder, der first-time
skal bruge JKL og I/O på seriøst.

**Kompleksitet:** Én ting ad gangen. Har scenen brug for J/L-cuts, overlap mellem
spor, eller Ripple Trim for at fungere godt, er den for avanceret til Del 2. De
teknikker hører til senere i lektionen (se afsnittet efter Del 2 i kursusplan.md).
Den ideelle scene kan bygges alene med det, Del 1 lige har lært: JKL, I/O, drag/
Append, og evt. ét swap.

**Genkendelighed:** Vælg en scene med en tydelig, aflæselig historie, hvor noget bevæger
sig hen imod noget, eller en handling har en tydelig start og slutning. Det gør det
lettere for dem at vide, om de er på rette spor, uden konstant at skulle sammenligne
med FACIT.

**Undgå:** dialog der kræver at man lytter meget nøje for at ramme det rigtige
in-punkt. Det er fint stof til en øvet redigør, men koster for meget tid her.

## Til dig, når du har bygget dem

Send mig:

- Navnene på klippene i `Del 2 – Byg scenen / Råklip`, i den rækkefølge de skal
  bruges i facit
- Hvor lang FACIT-timelinen er, og evt. et par sekunders beskrivelse af hvad der sker
- Om du har brugt markers, og i så fald hvad de siger

Så skriver jeg trinlisten i ren tekst med de rigtige navne, i stedet for generiske
pladsholdere.
