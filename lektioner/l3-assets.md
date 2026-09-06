# L3 – assets og timeline-opsætning (Edit L1/L2/L3)

Til `lektion-3-edit.html`. Alt materiale er Efterår, 23,976 fps. Opdateret
2026-09-05: strukturen matcher nu det, HP faktisk har bygget i `.dra`-pakken
(bin `03 EDIT` med undermapperne `L1`, `L2`, `L3`), ikke det oprindelige forslag.

## Puzzle-designet er ændret siden sidst

Den oprindelige anbefaling var en helt blank timeline. HP har i praksis bygget noget
bedre egnet til beginners: en **FACIT-timeline** med filmens færdige intro, og en
**PUZZLE-timeline hvor de fleste klip er fjernet**, ikke alle. Deltagerne genskaber
introen ved at genindsætte det manglende med det, de lige har lært, i stedet for at
starte fra et tomt lærred.

Det er en god ændring: de tilbageværende klip fungerer som landemærker, så ingen
sidder helt fast, men opgaven er stadig at bygge, ikke at flytte rundt på noget der
allerede er der. Byggeprocessen i `materialepakke.md` skal opdateres tilsvarende
(den beskriver stadig den blanke variant som opskrift for L3).

## Bins, som de faktisk ser ud

```
03 EDIT
├── L1                 basics + genskab introen (facit + puzzle)
├── L2                 udvidet: inspector, transitions, keyframing m.m.
└── L3                 composite, bro til Color
```

Jeg kender endnu ikke det fulde indhold af `L1`, `L2` og `L3`-mapperne indefra
(kun den ene disclosure-trekant fra dit screenshot). Det jeg mangler at få at vide,
står i bunden af hvert afsnit herunder.

## Edit L1 – basics og genskab introen (ca. 40 min)

**Kriterier for øvelsesklippene** (de klip der bruges til selve mekanik-øvelsen,
før man går løs på introen): tydeligt "rigtigt" øjeblik at finde med I/O, 10-20
sekunder råt materiale pr. klip, og klip der ikke ligner hinanden, så de er nemme
at genkende ved swap. Gerne outtakes eller klip der ikke endte i den færdige film,
det er lav-stakes-materiale.

**FACIT + PUZZLE:** FACIT er filmens rigtige intro. PUZZLE er samme timeline med de
fleste klip fjernet. Jeg mangler at vide:

- Hvor mange klip er der i FACIT-introen i alt, og hvilke af dem er fjernet i PUZZLE?
- Klippenes navne, i den rækkefølge de optræder i FACIT
- FACIT-introens samlede længde
- Er der markers på PUZZLE-timelinen som fingerpeg? Hvis ja, hvad står der?
- Ligger de fjernede klip stadig tilgængelige i en bin, klar til at blive
  genindsat, eller skal deltagerne finde dem et andet sted fra?

## Edit L2 – udvidet, overblik (ca. 25 min)

Indhold ifølge kursusplan.md: Inspector, transitions, freeze frame, simpel
keyframing, handles, slow motion, clip attributes-effekten, title basics. Alt på
overbliksniveau, ikke dybdeøvelse, se `kursusplan.md` for begrundelsen.

Jeg mangler at vide, hvad der allerede ligger i `03 EDIT / L2`-binnen:

- Er der bygget et eksempelklip til hver teknik (fx ét klip med freeze frame,
  ét med slow motion), eller skal de bruge det samme klip flere gange?
- Er der en facit-timeline for L2, eller er denne del ren demonstration uden en
  byggeøvelse?

## Edit L3 – composite, bro til Color (ca. 15 min)

Indhold ifølge kursusplan.md: en simpel composite-øvelse, som samtidig indleder
tankegangen fra Color-siden.

Jeg mangler at vide:

- Hvad består composite-øvelsen konkret af? (Fx to spor der blandes, en simpel
  opacitet/blend-øvelse, et logo lagt ovenpå.)
- Hvilket materiale skal bruges, og ligger det allerede i `L3`-binnen?

## Skærmbilleder til at gøre L3 færdig (2026-09-05)

Klipnavne er ikke længere vigtige (du har lavet en dedikeret mappe med de klip, de
skal bruge), og de mørke billeder i storyboardet er guitaristen, der går ind foran
kameraet, ikke et lysproblem. To grupper mangler nu: dem der erstatter de syv
pladsholdere, der allerede ligger i `lektion-3-edit.html` (kopier af `Alien.jpg`),
og dem til selve genskab-introen-øvelsen, som slet ikke har billeder endnu.

### Erstat de syv pladsholdere

Samme fremgangsmåde som L1 og L2: beskær til det der er tale om, ryd skærmen for
andre programmer, samme vinduesstørrelse hele vejen, gerne 1400-1800 px bred, under
150 KB efter komprimering. Filnavnene skal være de samme som i dag, så jeg blot kan
erstatte billedet uden at røre HTML'en.

1. **`l3-1-source-viewer.jpg`**: Source viewer med et klip åbnet og JKL-
   afspilningskontrollerne synlige forneden.
2. **`l3-2-io-markering.jpg`**: Source viewer med start- og slutpunkt sat, og
   lydkurven imellem dem synlig.
3. **`l3-3-traek-til-timeline.jpg`**: Et klip landet på timelinen, lige efter det
   er trukket ned fra source viewer.
4. **`l3-4-flere-klip.jpg`**: Tre-fire klip på timelinen, klar til at blive
   byttet om (ingen annotation nødvendig, det er bare konteksten).
5. **`l3-5-trim-vaerktoejer.jpg`**: Værktøjslinjen over timelinen med Selection,
   Trim og Blade synlige. Ring om de tre, hvis du har tid til annotation.
6. **`l3-6-inspector.jpg`**: Inspector med et klip valgt, Transform og Crop
   foldet ud.
7. **`l3-7-titel-effekt.jpg`**: Effects-panelet med en titel eller effekt
   trukket ned på timelinen.

### Nye, til genskab-introen-øvelsen

Disse findes slet ikke endnu, siden den del af siden stadig kun er en tekst-
skitse.

8. **`l3-8-facit.jpg`**: Facit-timelinen, hele eller de første 42 sekunder.
   Du har allerede `L1 start 1.png` og `L1 start 2.png` liggende i Downloads.
   De kan formentlig genbruges direkte i stedet for at tage nye. Send dem, så
   beskærer og bygger jeg dem ind.
9. **`l3-9-puzzle.jpg`**: PUZZLE-timelinen, som den ser ud med de 15 klip
   fjernet. Det er den vigtigste af de nye, det er den der viser opgaven.
10. **`l3-10-raaklip.jpg`**: Binnen med de klip, de skal genindsætte. Gerne med
    thumbnails store nok til at se hvad hvert klip viser.

## Til dig

Send de screenshots, du kan nå. Prioritér `l3-9-puzzle.jpg` og `l3-10-raaklip.jpg`
højst, det er dem der endnu ikke er noget billede eller tekst for på siden. Så
bygger jeg genskab-introen-delen færdig med rigtige trin, i stedet for skelettet
der står der nu.
