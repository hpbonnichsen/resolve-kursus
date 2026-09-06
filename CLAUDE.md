# Projektbriefing – DaVinci Resolve-kursus

Læs denne fil først i en ny session. Den er skrevet, så arbejdet kan fortsætte på en
anden computer uden at genopdage beslutningerne, vi allerede har taget.

## Hvad projektet er

Et endagskursus i DaVinci Resolve for voksne begyndere, **7/9 2026, kl. 9-15, Virum
Gymnasium**. Siden er både onboarding før dagen og selve undervisningsmaterialet på
dagen. Edit er delt i tre selvstændige dele (Edit L1/L2/L3), så der er otte
undervisningsblokke i alt, ét materialearkiv deltagerne henter på forhånd.

Kanoniske dokumenter, læs dem, ikke kun denne fil:

- **`kursusplan.md`**: dagens forløb, tidsbudget, hvad hver lektion dækker
- **`materialepakke.md`**: hvordan `.dra`-arkivet bygges, bin-struktur, puzzle-opskrifter
- **`README.md`**: designsystemet, palette, principper, hvorfor siden ser ud som den gør
- **`lektioner/l*-assets.md`**: asset-specs pr. lektion, skrevet før hver side bygges

## Status lige nu

| Lektion | Status |
|---|---|
| L1 · Interface og indstillinger | Bygget, `lektion-1-interface.html`. Ét skærmbillede mangler retagning (viser stadig 24 fps, skal være 23,976, markeret med `ROUGH CUT`-kommentar i HTML'en) |
| L2 · Siderne og dit materiale | Bygget, `lektion-2-siderne.html`. To billeder er placeholders: source viewer er tomt (skal vise et åbnet klip), Photo-siden mangler ikon (findes ikke i ikonsættet) |
| L3 · Edit L1, L2, L3 | **Alle tre færdige.** `lektion-3-edit.html` (L1), `lektion-3-edit-l2.html` (L2), `lektion-3-edit-l3.html` (L3). Edit er dermed hele lektionen færdigbygget, linket fra `program.html` alle steder |
| L4 · Color | **Færdig**, `lektion-4-color.html`. Interfacet (9 emner) → korrektion før grading → superviseret leg med tre valgfrie opgaver (skift rosens farve, orange/teal, ret et blåt klip fra "Hund på efterårstur") → CST, med før/efter-billede |
| L5 · Fusion | **Færdig**, `lektion-5-fusion.html`. Nodes genopfrisket → titel (hands-on) → custom transition (hands-on) → avanceret HUD-effekt (ren demo) → green screen (valgfri bonus) |
| L6 · Eget materiale | **Færdig**, `lektion-6-eget-materiale.html`. Frit valg mellem fire retninger → Deliver-siden. Eget materiale kræver bevidst et helt nyt projekt (test af L1's opsætning uden hjælp), de tre andre retninger fortsætter i kursusprojektet |

**Edit L1 består af to dele i samme fil**, adskilt af `<hr>` men uden separate
sider: "De rå håndgreb" (drag/JKL/I-O, swap, Append, trim-værktøjer, link/snap,
zoom) og "Genskab filmens åbning" (FACIT + PUZZLE-timeline hvor 15 klip er fjernet,
deltagerne genindsætter dem fra en råklip-bin). 40 minutter i alt.

**Edit L2 er sin egen fil, `lektion-3-edit-l2.html`**, ikke et afsnit i Edit L1's
fil. Det er den lektion, hvor `lektioner/udkast/edit-l2-inspector-titler.html`
(Inspector + titler) blev genbrugt. To af de seks dele har et ikon fra
`assets/icons/` ved siden af overskriften (`add-transition.png`, `freeze-frame.png`);
de øvrige fire (Inspector, Handles, Speed/Clip Attributes, Keyframing) har intet
matchende ikon i pakken og klarer sig med skærmbilleder alene.

**Edit L3 er sin egen fil, `lektion-3-edit-l3.html`**, bygget 2026-09-06. Anden
struktur end L1/L2: en "se effekten, gæt, få det forklaret"-opbygning i stedet for
trin-for-trin fra start. Effekten er en person, der forsvinder via samme kildeklip
lagt på to spor (én med personen, én trimmet til et senere, tomt tidspunkt) og
Opacity keyframet fra 100 til 0 på det øverste lag, samlet i et Compound Clip.
**Én uafklaret antagelse** står som kommentar øverst i filen: at rammaterialet i
`03 EDIT / L3`-binnen er ét enkelt klip, deltagerne selv skal lægge ned to gange.
Er binnen allerede delt i to færdige subclips, skal trin 1 i "Sådan er den lavet"
rettes.

**Hele Edit-lektionen (L1, L2, L3) er nu færdigbygget.**

**L4 Color afviger fra den oprindelige plan i `kursusplan.md`** (den beskrev Parsons
med distraktor-klip og shot matching). Det faktiske indhold, leveret af HP
2026-09-06, er demonstreret, ikke en øvelse med facit: en interface-tour over ni
navngivne værktøjer, konceptet "ret før du styler", superviseret fri leg uden facit,
og en afsluttende forklaring af CST. `kursusplan.md` er opdateret til at matche.
To ikoner fra `assets/icons/` bruges (`primarieslog-color-wheels.png`,
`scopes.png`), samme regel som i Edit L2: kun ved sikkert match.

**CST-billederne kom 2026-09-06.** To billeder bruges: node-panelet med Input/
Output Color Space, og et split før/efter-billede der viser forskellen visuelt.

**Ny genanvendelig komponent: `.heading-icon`** i `css/style.css`, erstatter en
inline-style, der var brugt to gange (L2 og L4) til ikon-foran-overskrift. Brug
den fremover i stedet for at gentage inline CSS.

**`.ideas`** er en ny, let komponent til valgfrie forslag i en fri-leg-øvelse,
adskilt fra `.steps` fordi der hverken er rækkefølge eller facit.

**Site-navigation bygget 2026-09-07.** Alle ti sider har nu samme fulde
navigation: Inden dagen, Program, 01 Interface, 02 Pages, 03 Edit, 04 Color,
05 Fusion, 06 Deliver og fri leg, Genveje. Genveje blev først fjernet, så
genindsat sidst i rækken efter ønske fra HP.

"03 Edit" er tre sider, så den er en fold, ikke et link: `<details class="nav__fold">`
med et `<ul class="nav__sub">` af de tre Edit-sider indeni. Ren HTML, ingen
JavaScript. På Edit-siderne selv står folden åben som standard (`open`-attributten
plus klassen `nav__fold--active`), så man ser og kan skifte mellem Edit L1/L2/L3
uden at klikke først. På alle andre sider er den lukket.

**Vigtig detalje, hvis nav'en redigeres igen:** `.nav__sub` må ikke være
`position: absolute`. Det blev prøvet først, men går galt, fordi folden står
åben permanent på Edit-siderne: en absolut positioneret boks ville flyde oven på
sidens eget indhold i stedet for at skubbe det ned. Den er nu normalt flow, som
alt andet foldbart på siden. Se README.md's navigations-afsnit for den fulde
begrundelse.

Nav'en genereres ens i alle 10 filer af et Python-script
(`build_nav.py`, kørt fra scratchpad, ikke gemt i repoet). Skal nav'en ændres
igen (ny lektion, ny rækkefølge), er det hurtigere at skrive scriptet om og
køre det på ny end at redigere 10 filer i hånden.

## Nøglebeslutninger, med begrundelse, så de ikke skal tages om

- **Dato/tid: 7/9 2026, 9-15.** Ikke 9-16, som en tidligere version af planen antog.
- **Framerate: 23,976 fps**, ikke 24. Matcher Efterårs egen optagelseshastighed.
- **Edit bygger på HP's eget "Hund på efterårstur", ikke Blackmagics "Beginner's
  Guide"-bog.** Bogen (i `research/`, ikke committet, se `.gitignore`) blev brugt
  som research for at finde den rigtige rækkefølge at undervise i (JKL/I-O før
  Append, ikke omvendt, bekræftet af både bogen og HP's eget hæfte fra 2022), men
  selve OMO-materialet fra bogen bruges ikke. Det løste også et rettighedsspørgsmål
  om at distribuere fremmed footage, se `materialepakke.md`.
- **Edit L1's puzzle er reduceret, ikke blank.** FACIT-timelinen viser filmens
  rigtige åbning; PUZZLE-timelinen har 15 af klippene fjernet (ikke alle), og
  deltagerne genindsætter dem fra en scoped råklip-bin. Ændret fra den oprindelige
  "helt blank timeline"-anbefaling, fordi HP i praksis byggede noget bedre egnet
  til total-begyndere: de tilbageværende klip er landemærker.
- **Edit er tre selvstændige dele (L1/L2/L3), ikke tre afsnit i én fil.** Navnene
  matcher bin-strukturen i `.dra`-pakken (`03 EDIT / L1, L2, L3`), som er HP's egen
  organisering, ikke en fejl. Alle tre dele deler ikke længere ét fast tidsrum:
  Edit L1 er 40 minutter og har sin egen side; L2 (~25 min) og L3 (~15 min) er
  separate opgaver, der bygges senere.
- **Arbejdsformen er stepwise, én lektion ad gangen:** ramme til godkendelse → trinliste
  i ren tekst → HP tager skærmbilleder/bygger i Resolve → HTML bygges → HP bygger
  timelines/bins i Resolve. Ingen lektion skrives i ét hug.
- **Ingen JavaScript på siden.** Foldning løses med `<details>`, ikke script.
- **Ingen 'em-dash' noget sted** (det lange bindestreg-tegn amerikansk typografi
  bruger), hverken på siden eller i planlægningsdokumenterne. Dansk tegnsætning i
  stedet: kolon, komma, punktum, eller almindelig tankestreg (–) kun i
  overskrifter/etiketter.
- **Genveje viser altid både Windows og Mac.** `Ctrl` har et `Cmd`-modstykke, `Alt`
  et `Option`-modstykke, overalt hvor en genvej nævnes.

## Filkort

```
index.html                  onboarding før dagen
program.html                dagens program, download, genveje
lektion-1-interface.html    L1, færdig
lektion-2-siderne.html      L2, færdig
lektion-3-edit.html         Edit L1, færdig
lektion-3-edit-l2.html      Edit L2, færdig
lektion-3-edit-l3.html      Edit L3, færdig
lektion-4-color.html        L4 Color, færdig
lektion-5-fusion.html       L5 Fusion, færdig
lektion-6-eget-materiale.html  L6, færdig
css/style.css               hele designsystemet, se README for tokens
assets/                     billeder, ikoner (assets/icons/, baggrund fjernet)
kursusplan.md               dagsplan
materialepakke.md           byggevejledning til .dra-arkivet
lektioner/                  asset-specs pr. lektion, arbejdsdokumenter
lektioner/udkast/           indhold flyttet ud af en side, til senere genbrug
research/                   kildemateriale, IKKE committet (se .gitignore)
```

**L5 Fusion afviger fra den oprindelige plan** (som havde tre hands-on trin med
distraktor-klip). Det faktiske indhold, bekræftet af HP 2026-09-06: to dele
hands-on (titel, custom transition), én ren demo uden byggeøvelse (avanceret
HUD-effekt med Tracker-node), og en fjerde, valgfri del (green screen), der ligger
på siden men ikke er en del af de 40 minutter på dagen. `kursusplan.md` er
opdateret til at matche.

**L6 afviger fra den oprindelige plan** (som antog en reservebin med kaffevideo-
klip, der aldrig blev bygget). Det faktiske indhold, bekræftet af HP 2026-09-06:
et frit valg mellem fire retninger, ingen af dem har facit. `kursusplan.md` er
rettet, og en stale reference til kaffevideoen i `program.html`s dagsprogram er
også rettet.

## Alle seks lektioner er nu færdigbygget

L1 til L6 findes alle som sider, linket fra `program.html` alle steder. Tilbage
står kun det, der er noteret som ikke gjort undervejs: Edit L2/L3 dækker ikke hele
den oprindelige liste 1:1 (se deres egne statuslinjer ovenfor).

**Fairlight er droppet, ikke udskudt.** Besluttet 2026-09-06: der er ikke tid til
den på kursusdagen, og der bliver ikke bygget en bonusside om den heller. Rettet i
`lektion-2-siderne.html` (tag ændret fra "bonus" til "bruges ikke", teksten om en
bonuslektion fjernet), `kursusplan.md` (tre steder) og `materialepakke.md` (bin
`99 BONUS - Fairlight` fjernet fra bin-strukturen).

## Navigation: gennemgående forrige/næste-knap

Alle ti sider (`index.html`, `program.html`, de otte lektionssider) har nu samme
`.lesson-nav`-komponent i bunden, med et sammenhængende kæde-flow:
`index → program → L1 → L2 → Edit L1 → Edit L2 → Edit L3 → L4 → L5 → L6`.
Komponenten fandtes allerede på L3 til L6 (Edit-kæden, Color, Fusion), men L1 og
L2 brugte i stedet en "Tilbage til programmet"-knap uden fremad-link, og
`index.html`/`program.html` havde slet ingen. Rettet 2026-09-06 så hele kæden er
ensartet. CSS er genbrugt uændret (`.lesson-nav`, `.lesson-nav__where`,
`.lesson-nav__spacer`, `.nav__link`), ingen nye klasser tilføjet.

## Icon-integration, sikkert-match-runde

2026-09-06: gennemgik alle 70 ikoner i `assets/icons/` (kun 11 var i brug) og
tilføjede `.heading-icon` hvor der var et sikkert match: `play-forward.png`
(L2's JKL-trin, Edit L1's "Åbn klippet ordentligt"), `mark-in.png` (Edit L1's I/O-
trin), `blade-edit-mode.png` (Edit L1's værktøjslinje-trin, dækker Blade-værktøjet
i teksten), `link-clips.png` (Edit L1's link/unlink/snap-trin), `new-timeline.png`
(Edit L1's "Opret en ny timeline"), `zoom-viewer-to-fit.png` (Edit L1's zoom-trin),
`viewer-overlay-on-off.png` (Edit L2's "Åbn Inspector", dækker fif'et om
transform-overlay), `add-keyframe.png` (Edit L2's keyframe-trin, Edit L3's
opacity-keyframe-trin), `deliver.png` (L6's Eksport-overskrift, genbrug af samme
ikon som L2's Deliver-tour). `background.png` blev omdøbt til `add-keyframe.png`
undervejs, fordi filens faktiske motiv er "Add Keyframe"-diamanten, ikke en
baggrund. Bevidst fravalgt: L1 (dialogtungt, intet toolbar-match), programmets
genvejstabel (ville rode), "Append"-trinnet i Edit L1 (intet ikon adskiller
Append fra Insert/Overwrite).

## Umiddelbart næste skridt

Ingen ny lektion venter, og Fairlight kommer ikke. Muligt næste arbejde: en
gennemgang af om alle "kommer snart"-rester er væk fra `program.html`, eller push
til git (se tidligere `.gitignore`-arbejde og commit-mønster i denne fils
historik).
