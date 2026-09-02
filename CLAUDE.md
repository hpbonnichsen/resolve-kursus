# Projektbriefing – DaVinci Resolve-kursus

Læs denne fil først i en ny session. Den er skrevet, så arbejdet kan fortsætte på en
anden computer uden at genopdage beslutningerne, vi allerede har taget.

## Hvad projektet er

Et endagskursus i DaVinci Resolve for voksne begyndere, **7/9 2026, kl. 9-15, Virum
Gymnasium**. Siden er både onboarding før dagen og selve undervisningsmaterialet på
dagen. Seks lektionssider, ét materialearkiv deltagerne henter på forhånd.

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
| L3 · Edit Page | Ramme og struktur besluttet, se `lektioner/l3-assets.md`. **Venter på HP:** klippenavne i rækkefølge, FACIT-timelinens længde, evt. markers. Først derefter skrives trinlisten |
| L4 · Color, L5 · Fusion, L6 · Eget materiale | Ikke påbegyndt |

## Nøglebeslutninger, med begrundelse, så de ikke skal tages om

- **Dato/tid: 7/9 2026, 9-15.** Ikke 9-16, som en tidligere version af planen antog.
- **Framerate: 23,976 fps**, ikke 24. Matcher Efterårs egen optagelseshastighed.
- **L3 bygger på Efterår, ikke Blackmagics "Beginner's Guide"-bog.** Bogen (i
  `research/`, ikke committet, se `.gitignore`) blev brugt som research for at finde
  den rigtige rækkefølge at undervise i (JKL/I/O før Append, ikke omvendt, bekræftet
  af både bogen og HP's eget hæfte fra 2022), men selve OMO-materialet bruges ikke.
  Det løste også et uafklaret rettighedsspørgsmål, se `materialepakke.md`.
- **L3 Del 2 er en blank timeline, ikke en delvist bygget en.** Deltagerne skal
  gennemføre hele byggeprocessen selv. Se `lektioner/l3-assets.md` for den fulde
  begrundelse.
- **Arbejdsformen er stepwise, én lektion ad gangen:** ramme til godkendelse → trinliste
  i ren tekst → HP tager skærmbilleder/bygger i Resolve → HTML bygges → HP bygger
  timelines/bins i Resolve. Ingen lektion skrives i ét hug.
- **Ingen JavaScript på siden.** Foldning løses med `<details>`, ikke script.
- **Ingen 'em-dash' noget sted** (det lange bindestreg-tegn amerikansk typografi bruger),
  hverken på siden eller i planlægningsdokumenterne.
  Dansk tegnsætning i stedet: kolon, komma, punktum, eller almindelig tankestreg (–)
  kun i overskrifter/etiketter.

## Filkort

```
index.html                  onboarding før dagen
program.html                dagens program, download, genveje
lektion-1-interface.html    L1, færdig
lektion-2-siderne.html      L2, færdig
lektion-3-edit.html         L3, ikke bygget endnu
css/style.css               hele designsystemet, se README for tokens
assets/                     billeder, ikoner (assets/icons/, baggrund fjernet)
kursusplan.md               dagsplan
materialepakke.md           byggevejledning til .dra-arkivet
lektioner/                  asset-specs pr. lektion, arbejdsdokumenter
research/                   kildemateriale, IKKE committet (se .gitignore)
```

## Umiddelbart næste skridt

Vent på svar fra HP på de tre spørgsmål i bunden af `lektioner/l3-assets.md`. Når de
kommer, skriv L3's trinliste i ren tekst (matcher formatet i `lektioner/l1-interface.md`
og `lektioner/l2-assets.md`), til godkendelse, før HTML bygges.
