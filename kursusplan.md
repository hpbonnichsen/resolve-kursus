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

Undervisningstid: 4 timer 25 minutter. Edit Page er med 80 minutter dagens længste
blok, nu delt i tre navngivne dele (Edit L1/L2/L3), der matcher bin-strukturen i
`.dra`-pakken.

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

Bygget på Efterår, ikke OMO. Bin-strukturen i `.dra`-pakken hedder `03 EDIT` med tre
undermapper, **L1, L2, L3**. Det navnesammenfald med kursets egne overordnede
lektionsnumre er med vilje HP's egen organisering i Resolve, ikke en fejl. På
kursussiden kaldes de **Edit L1/L2/L3** for at holde dem adskilt fra kursets L1-L6.

Alle tre dele deler ét fast tidsrum på 80 minutter. Bekræftet med HP 2026-09-05:
tiden udvides ikke, og intet flyttes til Color eller Fusion. Edit L2 og L3 holdes
derfor bevidst på **overbliksniveau**, samme greb som virkede for trim-værktøjer og
zoom sidst: vist og navngivet, ikke øvet i dybden.

Rækkefølgen inde i Edit L1 er grundet i research: både Blackmagics "Beginner's Guide"
og HP's eget hæfte fra 2022 underviser i drag/JKL/I-O, før de introducerer
Insert/Append som begreb, ikke omvendt. Se `lektioner/l3-assets.md` for den fulde
begrundelse.

**Edit L1 – de rå håndgreb og en genskabt intro (ca. 40 min), fuldt styret.**

- Ny timeline; hover for preview i binnen; åbn i source viewer
- JKL til at finde stedet; Mark In / Mark Out
- Træk klippet ned på timelinen; gentag med 2-3 klip mere
- Reorder via swap-genvejen (Shift+Ctrl+, / Shift+Ctrl+.)
- Append og Overwrite, nu hvor der er noget at føje til
- Overblik over knapper og trim-værktøjer: **Selection, Trim, Blade** (ikke Dynamic
  Trim: den involverer JKL-tasterne på en anden måde end det, de lige har lært, og
  forvirrer mere end den hjælper her, samme vurdering som i 2022-hæftet)
- Link/unlink af lyd og billede; snap til/fra; zoom ind/ud af timeline

**Ændret puzzle-design:** ikke længere en blank timeline. De ser en FACIT-timeline
med filmens færdige intro, og en PUZZLE-timeline hvor **de fleste klip er fjernet**.
Opgaven er at genskabe introen ved at genindsætte det manglende med det, de lige har
lært. Det er HP's egen implementering, bygget i praksis. Se `lektioner/l3-assets.md`,
som skal opdateres til at matche (den beskriver stadig en helt blank timeline).

**Edit L2 – udvidet, overblik (ca. 25 min).**

- Inspector, transitions, freeze frame
- Simpel keyframing, handles
- Slow motion, clip attributes-effekten
- Title basics

**Edit L3 – composite, bro til Color (ca. 15 min).**

- Simpel composite-øvelse
- Glidende overgang ind i Color-sidens tankegang, så L4 ikke starter fra nul

*De sidste minutter, hvis nogen er hurtigt færdige: "prøv det på dit eget."*

## 12:30–13:15 · L4 · Color Page

Bin: `04 COLOR PAGE`. Fokus er **nodes**, samme princip som Fusion bygger videre på
efter frokost, nu i sin enkleste form. Interfacet skåret ned først: skjul de paneler
vi ikke bruger.

- Primary color wheels: lift, gamma, gain og offset
- Kontrast, pivot og mætning: de tre greb der gør mest
- Nodes: hvad de er, og hvorfor man lægger justeringer i serie i stedet for at
  proppe alt ind i én
- Shift+D: se før og efter hele tiden
- **Shot matching:** vælg et referenceshot, grab still, split screen, ret de øvrige ind

Derefter fri leg: deltagerne farvegraderer selv, med det de lige har lært, uden en
facit at ramme.

*Stilladsering: Parsons med distraktorer, der ligger klip i binnen som ikke skal bruges.*

## 13:15–13:55 · L5 · Fusion

Bin: `05 FUSION`, opdelt som Edit i navngivne dele (`L1` set i mappestrukturen, flere
formentlig på vej). Tre byggetrin i stigende sværhedsgrad, samme rækkefølge som
Blackmagic-bogens eget Fusion-kapitel bruger:

1. **Titel**: det letteste at komme i gang med, og det der bekræfter node-modellen
   fra Color
2. **Custom transition**: en overgang bygget i Fusion i stedet for valgt fra en liste
3. **En mere avanceret comp**: en simpel VFX-effekt, det dagens mest abstrakte emne
   ender med at vise er muligt

- Node graph som flowdiagram: råmateriale ind, resultat ud
- De fire nodetyper: image, effect, merge, mask. Der findes over 300 nodes; de opfører
  sig som fire
- Tilbage til Edit Page og se resultatet ligge i timelinen

40 minutter til tre trin er stramt. Løber det over, skæres der i trin 3, ikke i
titel eller transition. De to første er dem, der cementerer node-forståelsen.

*Stilladsering: Parsons med distraktorer.*

## 14:05–14:45 · L6 · Eget materiale + eksport

Dagens payoff, bygget om HP's kaffevideo. Deltagerne blev i onboardingen bedt om
selv at filme noget i samme stil (`index.html`, "Optag noget selv"), så "eget
materiale" er reelt deres egen version af den samme øvelse, ikke vilkårligt medbragt
footage.

- Import af eget materiale (eller kaffevideoen som reserve)
- Klip det sammen på blank timeline, ingen facit
- Deliver-siden: presets, filnavn, destination
- Add to Render Queue og Render All

De går hjem med en fil de selv har lavet. Det er forskellen på at have set et program og
at have brugt det.

*Stilladsering: blank. Ingen brikker, ingen facit.*

For dem der ikke har eget materiale med, ligger der en reservebin med kaffevideo-
klippene, de kan bruge i stedet.

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
