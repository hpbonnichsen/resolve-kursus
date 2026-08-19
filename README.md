# Klip din første film færdig

Kursusside til et forløb i DaVinci Resolve for gymnasiet. Siden er
kursusmateriale til deltagere, ikke en salgsside: den skal på få sekunder svare
en elev på hvad forløbet er, hvor vi er nået til, og hvad man skal gøre nu.

Ren HTML, CSS og ganske lidt JavaScript. Ingen build, ingen afhængigheder.
Åbn `index.html` direkte i en browser.

## Struktur

```
index.html          hele forsiden
css/style.css       alt design
js/nav.js           sidepanelets folde-tilstand, intet andet
assets/             tom indtil videre
```

## Design

Nostromo-paletten fra `hpb_systems_portfolio`, hvor amber er accent og
brødteksten er varm off-white `#ece3d6`. Tokens er kopieret uændret, så de to
sites ser ud til at høre sammen.

DaVinci Resolve-logoets tre dråber er tilpasset ind i paletten frem for at blive
brugt råt: den gul-grønne absorberes af amber, og de to andre er roteret mod
varme med mætningen sat ned til `--res-teal #3E9CB8` og `--res-rust #D9553F`.
De optræder som venstrekant på et modulkort, som klipblok på timeline-striben og
som farve på modulnumrene i sidepanelet, hvor tallet selv bærer betydningen.
Amber skal blive ved med at være den eneste farve der betyder "det her er
vigtigt". Logoets regnbuekant optræder ét sted: gradientlinjen under
hero-overskriften.

**Hero fylder skærmen alene.** Rammen er det eneste man møder ved landing:
fire hjørne-L'er med tidskode og REC-markør, og næsten tomt indeni. Det negative
rum er selve motivet, så siden signalerer film og postproduktion uden et eneste
billede. Teksten er låst til 660 px inde i en ramme der fylder hele bredden, og
forskellen mellem de to bredder er hele pointen.

**Sidepanelet** er navigationen. Sammenfoldet er det en 72 px stribe med
modulnumrene i deres farvekodning; udfoldet viser det modulnavne, undertitler og
hvor holdet er nu. Tilstanden bor på `<html data-nav>`, gemmes i `localStorage`
og læses tilbage af et inline-script i `<head>`, så et udfoldet panel ikke
blinker sammenfoldet ved indlæsning. Under 900 px lægger panelet sig oven på
indholdet, og et klik på et link lukker det igen.

**Timeline-striben** ligger under hero som overgangen til indholdet. Modulerne
er tegnet som klipblokke med bredder der svarer til deres vægt i forløbet, så
illustrationen også er indholdsfortegnelsen.

Layoutet er fuldbredde uden `max-width`. Over 1700 px går modulgitteret fra tre
til fire kort i rækken, så linjelængderne forbliver læsbare når siden får hele
bredden at arbejde med.

Bevægelse er ren CSS via `animation-timeline: view()`, pakket i `@supports` og
slået fra under `prefers-reduced-motion`.

## Vedligehold

**Flyt markøren når holdet rykker videre.** Tre steder i `index.html`:

1. Sidepanelet: flyt `class="is-active"` og `aria-current="step"` til det
   aktuelle modul, og ret `<p class="side__now">`.
2. Timeline-striben: flyt `class="tl__clip is-active"`, og ret
   `<p class="tl__now">`.
3. Modulkortet: ret `card__meta` til `"… · vi er her nu"`.

**Gitterets rytme** skal altid gå op i tolv kolonner. Den er 6+6 / 8+4 / 4+4+4
som standard og 3+3+6 / 3+3+3+3 over 1700 px. Ændrer du antallet af moduler,
skal begge rytmer regnes igennem igen.

## Mangler stadig

- Rigtige tal i statuslinjen (moduler, lektioner, Resolve-version).
- Link til øvelsesmaterialet (står som "Link følger").
- Undersiderne bag hvert modul. Kortene siger "Materiale kommer snart" og er
  bevidst ikke links, så der ikke er noget dødt at klikke på.

## Verificeret

- Alle tekst- og baggrundskombinationer er tjekket programmatisk mod WCAG AA,
  inklusive sidepanelets farvekodede modulnumre. Laveste er 5,10:1.
- Ingen vandret side-scroll ved 375, 900, 1440 eller 1920 px. Timeline-striben
  scroller inde i sin egen container på mobil.
- Panelets toggle er testet: `data-nav` og `aria-expanded` følges ad, og
  tilstanden overlever genindlæsning.
- Panelets skjulte tekst er `display: none` i sammenfoldet tilstand, så den
  heller ikke læses op af skærmlæsere.
- Siden står fuldt læsbar med reduceret bevægelse og uden support for
  `animation-timeline`.
