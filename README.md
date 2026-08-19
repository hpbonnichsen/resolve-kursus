# Klip din første film færdig

Kursusside til et forløb i DaVinci Resolve for gymnasiet. Siden er
kursusmateriale til deltagere, ikke en salgsside: den skal på få sekunder svare
en elev på hvad forløbet er, hvor vi er nået til, og hvad man skal gøre nu.

Ren HTML og CSS. Ingen build, ingen afhængigheder, intet JavaScript. Åbn
`index.html` direkte i en browser.

## Struktur

```
index.html          hele forsiden
css/style.css       alt design
assets/             tom indtil videre
```

## Design

Nostromo-paletten fra `hpb_systems_portfolio`, hvor amber er accent og
brødteksten er varm off-white `#ece3d6`. Tokens er kopieret uændret, så de to
sites ser ud til at høre sammen.

DaVinci Resolve-logoets tre dråber er tilpasset ind i paletten frem for at blive
brugt råt: den gul-grønne absorberes af amber, og de to andre er roteret mod
varme med mætningen sat ned til `--res-teal #3E9CB8` og `--res-rust #D9553F`.
De optræder kun som kodning i små doser (venstrekant på et modulkort, klipblok
på timeline-striben), aldrig som flader og aldrig som tekst. Amber skal blive
ved med at være den eneste farve der betyder "det her er vigtigt".
Logoets regnbuekant optræder ét sted: gradientlinjen under hero-overskriften.

Hero er bygget som en **viewer-ramme**: fire hjørne-L'er i 2.39:1 med tidskode
og REC-markør, og næsten tomt indeni. Det negative rum er selve motivet, så
siden signalerer film og postproduktion uden et eneste billede. Under rammen
løber en **timeline-stribe** hvor modulerne er tegnet som klipblokke: den er
både illustration og indholdsfortegnelse, og den viser hvor holdet er lige nu.

Bevægelse er ren CSS via `animation-timeline: view()`, pakket i `@supports` og
slået fra under `prefers-reduced-motion`.

## Vedligehold

**Flyt markøren når holdet rykker videre.** To steder i `index.html`:

1. På timeline-striben: flyt `class="tl__clip is-active"` og
   `aria-current="step"` til det aktuelle modul, og ret linjen
   `<p class="tl__now">`.
2. På det tilhørende modulkort: ret `card__meta` til `"… · vi er her nu"`.

**Modulkortenes bredde** styres af `.card--module` og `.card--wide` i CSS.
Rytmen er 6+6 / 8+4 / 4+4+4, så de tolv kolonner går op. Ændrer du antallet af
moduler, skal den rytme regnes igennem igen.

## Mangler stadig

- Rigtige tal i statuslinjen (moduler, lektioner, Resolve-version).
- Link til øvelsesmaterialet (står som "Link følger").
- Undersiderne bag hvert modul. Kortene siger "Materiale kommer snart" og er
  bevidst ikke links, så der ikke er noget dødt at klikke på.

## Verificeret

- Alle tekst- og baggrundskombinationer er tjekket programmatisk mod WCAG AA.
  Laveste er 5,70:1, alle øvrige ligger over 6:1.
- Ingen vandret side-scroll ved 360, 768 eller 1440 px. Timeline-striben
  scroller inde i sin egen container på mobil.
- Siden står fuldt læsbar med reduceret bevægelse og uden support for
  `animation-timeline`.
