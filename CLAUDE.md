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
| L3 · Edit L1 | **Færdig**, `lektion-3-edit.html`. Rigtige skærmbilleder fra HP's "Hund på efterårstur"-projekt. Linket fra `program.html` begge steder (programmet og lektionsoversigten) |
| L3 · Edit L2 | Ikke bygget. Indholdsudkast (Inspector, Transform, Crop, titler/effekter) gemt i `lektioner/udkast/edit-l2-inspector-titler.html` til genbrug, inkl. to brugbare billeder (`assets/l3-6-inspector.jpg`, `assets/l3-7-titel-effekt.jpg`) |
| L3 · Edit L3 | Ikke bygget. Indhold ifølge `kursusplan.md`: simpel composite-øvelse, bro til Color |
| L4 · Color, L5 · Fusion, L6 · Eget materiale | Ikke påbegyndt. Indhold og fokus er besluttet (se `kursusplan.md`), sider ikke bygget |

**Edit L1 er færdig og består af to dele i samme fil**, adskilt af `<hr>` men uden
separate sider: "De rå håndgreb" (drag/JKL/I-O, swap, Append, trim-værktøjer,
link/snap, zoom) og "Genskab filmens åbning" (FACIT + PUZZLE-timeline hvor 15 klip
er fjernet, deltagerne genindsætter dem fra en råklip-bin). 40 minutter i alt.

**Edit L2 og L3 har ikke egne HTML-sider endnu.** `program.html`s undernavigation
viser dem som "(kommer snart)", uden links, indtil de er bygget. Byg dem efter samme
mønster som Edit L1 (egen fil eller nyt afsnit, ramme → trinliste → assets → HTML),
ikke som en fjerde sektion i `lektion-3-edit.html`. Den fejl (Inspector-indhold
liggende som "Del 3" i Edit L1's fil) er allerede rettet én gang, 2026-09-05.

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
lektion-3-edit.html         Edit L1, færdig (kun L1, se status ovenfor)
css/style.css               hele designsystemet, se README for tokens
assets/                     billeder, ikoner (assets/icons/, baggrund fjernet)
kursusplan.md               dagsplan
materialepakke.md           byggevejledning til .dra-arkivet
lektioner/                  asset-specs pr. lektion, arbejdsdokumenter
lektioner/udkast/           indhold flyttet ud af en side, til senere genbrug
research/                   kildemateriale, IKKE committet (se .gitignore)
```

## Umiddelbart næste skridt

Byg Edit L2 (Inspector, transitions, freeze frame, keyframing, handles, slow
motion, clip attributes, title basics) som sin egen side. Start med udkastet i
`lektioner/udkast/edit-l2-inspector-titler.html`, som allerede har Inspector- og
titel-indhold med rigtige billeder, men mangler resten af listen fra
`kursusplan.md`. Følg samme proces som hidtil: ramme til godkendelse først.
