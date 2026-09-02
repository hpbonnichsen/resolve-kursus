# L2 – assets

Til `lektion-2-siderne.html`. Lektionen er 09:45–10:15, 30 minutter, og falder i to
halvdele: en rundtur i siderne, som vises frem, og import af materiale, som de gør selv.

## Status

**Rundturen kan bygges nu.** Alt hvad den kræver, ligger allerede i repoet.

**Anden halvdel er blokeret af pakken.** Skærmbillederne af Media Pool skal vise de
rigtige lektionsbins, og de findes ikke før `.dra`-arkivet er bygget. Tag dem, når
projektet står.

---

## Findes allerede

### De otte sider
`assets/Screenshots/02` til `09`: media, photos, cut, edit, fusion, color, fairlight,
deliver. Alle 4K-PNG'er på omkring en halv megabyte.

De skal igennem samme behandling som L1's: nedskaleret og konverteret til JPG. Men
ikke til 1800 px. Otte helskærmsbilleder ved fuld bredde bliver til godt en megabyte
sidevægt, og de skal alligevel kun give et indtryk af hvordan en side ser ud, ikke
læses i detaljer. **900 px er rigeligt**, og så lander de samlet under 400 KB.

### Sidernes ikoner
`assets/icons/media.png`, `cut.png`, `edit.png`, `fusion.png`, `color.png`,
`fairlight.png`, `deliver.png`. Gennemsigtige og klar til brug.

### Bundlinjen
`assets/l1-1-bundlinjen.jpg` genbruges. Den er allerede beskåret og annoteret, og det
er en fordel at genkende den fra lektionen før.

---

## Skal tages, når pakken er bygget

Alle med samme fremgangsmåde som L1: beskær til det der er tale om, samme
vinduesstørrelse hele vejen, ryd skærmen for andre programmer og personlige filstier.

### 1. `l2-1-media-pool.jpg`
**Hvad:** Media Pool med de lektionsopdelte bins foldet ud i venstre side.
**Beskæring:** Kun Media Pool-panelet, ikke hele programmet.
**Annotation:** Ramme om binlisten.
**Hvorfor:** De skal genkende strukturen, de får udleveret. Det er det eneste
skærmbillede i lektionen, der viser *deres* projekt og ikke bare programmet.

### 2. `l2-2-import.jpg`
**Hvad:** Højrekliksmenuen i Media Pool med Import Media synlig.
**Annotation:** Ring om menupunktet.
**Hvorfor:** Der er tre måder at få materiale ind på. De skal kun kende én.

### 3. `l2-3-source-viewer.jpg`
**Hvad:** Source viewer med et klip åbent, gerne med lydkurven synlig.
**Annotation:** Ring om afspilningsknapperne.
**Hvorfor:** Bruges til at forklare J, K og L, som er den vigtigste vane i hele kurset.

Tre billeder. Sammenlignet med L1's fem er det med vilje: stilladset er begyndt at
blive trukket væk.

---

## Et forslag til opbygningen

De otte helskærmsbilleder er dårlige som hovedindhold. Ved 900 px er teksten i dem
alligevel ulæselig, og otte næsten ens grå flader efter hinanden er svære at skelne.

Byg i stedet listen op om **ikonet plus to sætninger**: hvad siden er til, og hvornår
man går derhen. Ikonet er det, de skal genkende i bundlinjen, og det er skarpt i alle
størrelser. Helskærmsbilledet lægges under hver enkelt med `loading="lazy"`, så det
kun hentes, hvis nogen ruller ned til det.

Det giver en side, man kan skimme på tredive sekunder, og som stadig kan slås op i
bagefter.
