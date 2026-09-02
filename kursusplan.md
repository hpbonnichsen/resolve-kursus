# DaVinci Resolve 21 – endagskursus, dagsplan

**7. september 2026, kl. 9-15, Virum Gymnasium.**

Udgave: september 2026. Afløser programmet i `research/Davinci Kursus.pdf` (nov. 2022).
Bygget på deltagernes ønsker: interface og praktiske indstillinger, kort rundtur i
siderne, hovedvægt på Edit Page om formiddagen, Color og Fusion efter frokost.

## Forudsætninger

**Installation sker hjemmefra.** Deltagerne henter, installerer og starter Resolve før
kursusdagen via onboarding-siden. Det er den vigtigste enkeltændring fra 2022-planen,
hvor den første time gik med download af en gigabyte over delt wifi.

**Ét projekt hele dagen.** Alt råmateriale ligger i ét `.dra`-arkiv med lektionsopdelte
bins, hentet inden dagen. Tre projektskift var i 2022 tre steder hvor deltagere faldt af.

**Alle ressourcer fra start.** Klippene er trimmet på forhånd, timelines er oprettet,
og facit ligger i projektet. Der går ikke ét minut med opsætning på dagen.

---

## Dagens forløb

| Tid | Blok | Min |
|---|---|---|
| 09:00–09:15 | Velkomst og opstartstjek | 15 |
| 09:15–09:45 | L1 · Interface og praktiske indstillinger | 30 |
| 09:45–10:15 | L2 · Siderne kort + materialet ind i projektet | 30 |
| 10:15–10:30 | Pause | 15 |
| 10:30–11:50 | **L3 · Edit Page – dagens hovedblok** | 80 |
| 11:50–12:30 | Frokost | 40 |
| 12:30–13:15 | L4 · Color Page | 45 |
| 13:15–13:55 | L5 · Fusion | 40 |
| 13:55–14:05 | Pause | 10 |
| 14:05–14:45 | **L6 · Eget materiale + eksport** | 40 |
| 14:45–15:00 | Afrunding | 15 |

Undervisningstid: 4 timer 25 minutter. Edit Page er med 80 minutter dagens længste blok.

---

## 09:00–09:15 · Velkomst og opstartstjek

Kort præsentationsrunde og to praktiske tjek: har alle programmet åbent, og har alle
hentet materialepakken? De der mangler sættes i gang nu og hentes ind i L1. Resten
venter ikke på dem.

## 09:15–09:45 · L1 · Interface og praktiske indstillinger

Formålet er ikke at gennemgå menuer, men at give deltagerne en **mental model** af
programmet, før de rører ved det. Resolve er ikke ét program med faneblade; det er flere
programmer i én fil, samlet i den rækkefølge en film bliver til.

- Restore Project Archive: materialepakken ind i programmet
- Project Manager og hvor projekter bor
- Project Settings: timeline-opløsning og framerate
- Preferences: Media Storage, Live Save og Project Backups
- Farvestyring, hvis råmaterialet er log

Farvestyringen ligger her og ikke midt i klippearbejdet. Klipper man en time i gråt
materiale først, har man allerede lært at det ser sådan ud.

*Stilladsering: fuldt styret. Hvert klik beskrevet, skærmbillede til hvert trin.*

## 09:45–10:15 · L2 · Siderne kort + materialet ind i projektet

Rundturen vises frem, den øves ikke. Hver side får to sætninger: hvad den er til, og
hvornår man går derhen. Cut Page demonstreres som den hurtige vej, vi ikke bruger i dag.

Derefter hands-on i Media Pool: bins, scrubbing og JKL som afspilningsstyring.

*Stilladsering: fuldt styret.*

## 10:30–11:50 · L3 · Edit Page – dagens hovedblok

Målet er konkret: **et færdigt råklip før frokost.** Deltagerne skal have set noget
spille igennem fra ende til anden, mens de stadig har overskud. Det er dagens vendepunkt.

*Første halvdel, Parsons låst:* alle klip ligger allerede på timelinen i forkert
rækkefølge. Opgaven er udelukkende at flytte rundt, så historien fungerer.

- Interfacet: media pool, source viewer, timeline viewer, timeline
- Spor: øverste videospor vinder, al lyd lægges sammen
- Trimning fra kanterne, blade, ripple trim
- Lydniveauer og et enkelt fade

*Anden halvdel, Parsons åben:* brikkerne ligger i en bin, timelinen er tom. De vælger
selv hvordan klippene kommer ned.

- In- og out-punkter i source viewer; markers
- Insert, overwrite, place on top, append
- Link og unlink; J- og L-cut
- Overgange og hvornår man **ikke** skal bruge dem
- Inspector: transform, crop, dynamic zoom
- Én keyframe-animation

Keyframes introduceres her, fordi princippet går igen i både Color og Fusion. Lærer man
diamant-ikonet én gang, genkender man det to gange mere på dagen.

*De sidste fem minutter: "prøv det på dit eget" for dem der er hurtigt færdige.*

## 12:30–13:15 · L4 · Color Page

- Interfacet skåret ned: skjul de paneler vi ikke bruger
- Primary color wheels: lift, gamma, gain og offset
- Kontrast, pivot og mætning: de tre greb der gør mest
- Shift+D: se før og efter hele tiden
- **Shot matching:** vælg et referenceshot, grab still, split screen, ret de øvrige ind

Sidste punkt er blokkens egentlige indhold. En enkelt smuk indstilling er let; at fem
klip ligner hinanden er det, der afgør om filmen ser professionel ud.

*Stilladsering: Parsons med distraktorer, der ligger klip i binnen som ikke skal bruges.*

## 13:15–13:55 · L5 · Fusion

Dagens mest abstrakte emne. Blokken er hårdt afgrænset til **ét produkt.**

- Node graph som flowdiagram: råmateriale ind, resultat ud
- De fire nodetyper: image, effect, merge, mask. Der findes over 300 nodes; de opfører
  sig som fire
- Ét konkret greb bygget færdigt
- Tilbage til Edit Page og se det ligge i timelinen

Ingen rundtur i værktøjskassen. Deltagerne skal forlade blokken med én ting der virker
og en model der forklarer resten.

*Stilladsering: Parsons med distraktorer.*

## 14:05–14:45 · L6 · Eget materiale + eksport

Dagens payoff. Deltagerne lægger deres egne optagelser i binnen `00 Eget materiale` i
samme projekt, klipper noget kort sammen og eksporterer det.

- Import af eget materiale
- Klip det sammen på blank timeline, ingen facit
- Deliver-siden: presets, filnavn, destination
- Add to Render Queue og Render All

De går hjem med en fil de selv har lavet. Det er forskellen på at have set et program og
at have brugt det.

*Stilladsering: blank. Ingen brikker, ingen facit.*

For dem der ikke har eget materiale med, ligger der en reservebin de kan bruge i stedet.

### Regn med at billedhastigheden kolliderer her

Kursusmaterialet (Efterår) er ensrettet til 23,976 fps i pakken, så
lektion 1 til 5 er fri for problemet. Det er deltagernes eget materiale ikke: tolv
telefoner betyder formentlig mest 30 fps og enkelte 25, og det kan ikke ordnes på
forhånd, fordi filerne først dukker op på dagen.

Det er ikke et uheld, det er lektionens bedste undervisningsøjeblik. I lektion 1 fik de
at vide, at billedhastigheden låser sig. Her mærker de hvorfor. Når nogen lægger et
30 fps-klip på en 23,976 fps-timeline og synes bevægelsen ser mærkelig ud, har du et
konkret eksempel i stedet for en advarsel.

Vær klar til at svare kort på "hvorfor hakker min video": timelinen er sat til 23,976,
klippet er optaget med 30, og Resolve smider billeder væk for at få det til at passe.
Det er ikke en fejl, og det er ikke noget vi retter i dag.

## 14:45–15:00 · Afrunding

Hvor man går hen herfra, og hvad der ligger på kursussiden bagefter, herunder
bonuslektionen om Fairlight.

---

## Noter til afvikling

**Fairlight er ikke med.** Der er ikke plads på seks timer. Lydniveauer og fades ligger
i L3, og resten er en bonuslektion på siden, som deltagerne kan tage derhjemme.

**Cut Page er nedgraderet** fra 90 minutters hands-on i 2022 til en demo. Det koster den
tidlige sejr, som den gamle plan fik ud af en færdig film kl. 11:30. Sejren er flyttet
til råklippet før frokost. Hold fast i at det skal nås, ellers mangler dagen sit
vendepunkt.

**Løber Fusion over, skæres der i Fusion.** Color er det emne alle får brug for.

**L6 må ikke ryge.** Det er den eneste blok hvor de rører ved deres eget, og den de
husker. Bliver dagen forsinket, skæres der i L5 og i pauserne, ikke her.
