# Materialepakken – byggevejledning

Deltagerne henter **ét arkiv** inden kursusdagen og gendanner det i Resolve med
`Restore Project Archive`. Én handling, ingen relinking, intet der kan komme offline.

Dette dokument er rammen. Bins fyldes op efterhånden som lektionerne designes, men
strukturen skal stå nu, så alt andet kan bygges ovenpå.

## 1. Transcode først

**Al kursusmedie konverteres til 1080p H.264 ved 23,976 fps før det importeres.**
Det er rigeligt til undervisning, og det er forskellen på en pakke der kan hostes og
en der ikke kan.

```bash
ffmpeg -i input.mov -vf scale=-2:1080 -r 23.976 -c:v libx264 -crf 20 -preset slow \
       -c:a aac -b:a 192k output.mp4
```

`-crf 20` er visuelt tabsfrit til formålet. Skal pakken skæres yderligere ned, gå til
`-crf 23` før du går ned i opløsning: opløsningen er det deltagerne ser.

### Hvorfor projektet kører på 23,976

Det er den hastighed, din **Efterår**-footage er optaget i (23,98 er samme tal, bare
afrundet). Projektet kræver derfor ingen billedhastighedskonvertering af Efterår
overhovedet, kun opløsning og codec skal ensrettes i transcoden.

23,976 og 24 ser identiske ud i en filoversigt, men er det ikke, og forskellen driver
langsomt lyden ud af sync over nogle minutter. Derfor er kommandoen ovenfor stadig
skrevet med `-r 23.976`, selv om Efterår ikke behøver det: den er sikkerhedsnettet,
hvis der senere kommer materiale ind til Color eller Fusion, der ikke matcher.

Billedhastigheden er en **projektindstilling**, ikke en timeline-indstilling: alle
timelines i projektet deler den, og den låser sig så snart der ligger noget på den
første. Det er derfor den skal besluttes nu og ikke senere.

Vælger du en anden hastighed, skal tallet rettes to steder mere: i projektets Master
Settings og i trin 2 på `lektion-1-interface.html`.

## 2. Bin-struktur

Lektionsopdelt, så mappen de kender fra siden også findes i programmet.

```
dr_kursus_virum
├── 00 Eget materiale       tom, klar til deres egne filer
│   └── Reserve             fallback for dem der intet har med
├── 01 Interface
├── 02 Pages
├── 03 Edit
│   ├── Del 1 – Øvelsesklip 3-4 klip, lav stakes, ikke en del af facit
│   └── Del 2 – Byg scenen
│       ├── Råklip          kun det denne scene skal bruge, trimmet til subclips
│       └── Timelines
│           ├── FACIT       den færdige scene, låst/ikke redigerbar
│           └── PUZZLE      tom. Deltagerne opretter selv timelinen i trin 1
├── 04 Color
├── 05 Fusion
├── 06 Deliver
└── 99 BONUS - Fairlight
```

`03 Edit` følger den variant af puzzle-designet, der er blank i stedet for
omrokeret: se `lektioner/l3-assets.md` for den fulde begrundelse. Kort sagt bygges
her ikke en `PUZZLE`-timeline med klip i forkert rækkefølge, kun en `FACIT` og et
scoped `Råklip`-bin. Selve byggeprocessen er derfor kortere for denne lektion:

1. Klip facit færdigt på en timeline og navngiv den `FACIT`
2. Læg kun de klip, scenen bruger, i `Råklip` som subclips
3. Lad `PUZZLE`-timelinen være ikke-eksisterende. Deltagerne opretter den selv

`04 Color` og `05 Fusion` bruger derimod den oprindelige, omrokerede variant, når de
skal bygges, se opskriften nedenfor.

## 3. Sådan bygges en omrokeret puzzle-lektion (L4, L5)

1. Klip facit færdigt på en timeline og navngiv den `FACIT – lektion N`
2. Dupliker den, omdøb til `PUZZLE – lektion N`
3. På puzzle-timelinen: byt om på klippene, så rækkefølgen er forkert men alle brikker
   er der. **Ingen huller**: de skal kunne flytte rundt uden at skulle lukke mellemrum
4. Til de åbne varianter: fjern klippene fra timelinen og læg subclipsene i en
   `Råklip`-bin i stedet, med en tom timeline ved siden af
5. Læg to-tre brikker i binnen som *ikke* hører til. Udvælgelsen bliver en del af
   opgaven

Facit-timelinen bliver liggende i projektet i begge varianter. Målet skal være kendt:
det er hele pointen i en Parsons-opgave. Det er vejen derhen der er opgaven.

## 4. Navngivning

Brikkerne navngives **neutralt**: `A`, `B`, `C` eller `brik-01`. Hedder de
`01-åbning`, `02-nærbillede`, `03-slutning`, har du afsløret rækkefølgen, og opgaven
er væk.

## 5. Eksport

`File > Project Manager > højreklik på projektet > Export Project Archive`
Filnavn: `Resolve-kursus-2026.dra`

## 6. Mål størrelsen med det samme

GitHub Releases tager **maks 2 GB pr. fil**, og det er der siden allerede hoster
`kaffe.mp4` fra. Ligger arkivet over, skal det et andet sted hen, og det skal du vide
nu og ikke den 6. september.

```bash
du -h Resolve-kursus-2026.dra
```

Tolv deltagere skal også kunne hente den hjemmefra. Under 1 GB er behageligt, under
2 GB er nødvendigt.

## 7. Test på en fremmed maskine

Gendan arkivet på en maskine der aldrig har set projektet, helst Windows, da det er
der de fleste deltagere sidder. Tjek at alt medie er online, og at alle timelines
åbner. **Det er den ene ting der ikke må fejle på dagen.**

## Note om rettigheder

Efterår, kaffevideoen og musikvideoen er dine egne og frit dine at dele. L3 bygger nu
udelukkende på Efterår, så der er intet at afklare der.

**Bliver Blackmagics "Beginner's Guide"-materiale (Organ Mountain Outfitters) taget i
brug senere**, fx til Color eller Fusion, skal det afklares først: hverken bogens
webside eller PDF'en nævner vilkår for selve mediepakken, kun en generel
copyright-notits om bogens tekst og billeder. Skriv i så fald til
learning@blackmagicdesign.com og spørg direkte, om footage fra
`R20_Beginner_Guide.zip` må indgå i et materialearkiv, der distribueres til betalende
kursister, før det pakkes ind.
