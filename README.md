# Fra redigering til færdig film

Onboarding-side til et endagskursus i DaVinci Resolve for voksne begyndere.
Kursisterne får linket i en mail før kursusdagen, og siden skal svare på tre
ting: hvordan installerer jeg programmet, hvad skal jeg have gjort inden vi
mødes, og hvad er det egentlig vi skal lave.

Ren HTML og CSS. Ingen build, ingen afhængigheder, intet JavaScript.
Åbn `index.html` direkte i en browser.

```
index.html       hele siden
css/style.css    alt design
assets/          det siden udgiver
design/          mockups og kildegrafik, udgives ikke
```

## Hvorfor siden ser sådan ud

Siden er en onepager uden navigation. Det er et valg, ikke en mangel: der er
tre opgaver, de skal udføres i rækkefølge, og man kan ikke fare vild på en
side der kun har én vej igennem.

**Én knapform på hele siden.** Amber betyder handling og intet andet. Derfor
er hero-billedet heller ikke selv en klikflade — kompositionen viser en
pilleformet knap, og hvis hele fladen var klikbar, ville den knap lyve om sit
eget mål.

**Ingen tekst i billeder.** Hele hero-kompositionen er HTML og CSS.
Petroleum-cirklen er et element med `border-radius: 50%`, ikke et billede, og
overskriftens vægtskift er `font-weight` 300 mod 800. Det betyder at teksten
kan markeres, zoomes, læses op og reflowe — hvilket er afgørende, når linket
kommer fra en mail og bliver åbnet på en telefon.

**Screenshot-annotationerne er SVG oven på billedet**, ikke brændt ind i
JPEG'en. De kan rettes uden billedredigering, og de forbliver skarpe.

## Palette

Målt direkte ud af mockuppen i `design/Page_hero.PNG`.

| Token | Værdi | Rolle |
|---|---|---|
| `--bg` | `#171717` | baggrund |
| `--surface` | `#1e1e1e` | praktisk-stribe |
| `--petrol` | `#0E3D42` | hero-cirklen |
| `--amber` | `#FF9E00` | **primær** — kun handling |
| `--rust` | `#E9967A` | **sekundær** — kun struktur |
| `--ink` | `#ece3d6` | brødtekst |
| `--ink-dim` | `#9c9287` | sekundær tekst på `--bg` |
| `--ink-soft` | `#b8aea2` | kickeren i hero, som står på cirklen |

Amber ejer alt der beder om et klik. Rust ejer det der ordner uden at kalde
på et: trin-numre, skillelinjernes klipmarkering, annotationerne. Hold den
fordeling — det er den, der gør at man kan se hvad man skal gøre uden at læse.

`--ink-soft` findes udelukkende fordi `--ink-dim` kun når 3,9:1 mod
petroleum-cirklen og altså falder i WCAG AA. Brug den ikke andre steder.

## Vedligehold

**Før siden sendes ud** skal pladsholderne udfyldes i `index.html`:

- `[udfyldes]` tre steder i `.facts` — dato, tid og sted.
- `[kontakt udfyldes]` i footeren.

**Flytter Blackmagic rundt på deres downloadside**, skal begge screenshots i
`assets/` tages om, og SVG-koordinaterne i `index.html` justeres. Ringene
sidder i et `viewBox` der matcher billedets egne pixelmål, så nye screenshots
kræver nye tal i både `viewBox` og `cx`/`cy`.

**Sidens bredde** styres af `--shell` (`clamp(680px, 76vw, 1500px)`), som
sættes på `body` over 720 px. Den holder hero, skillelinjer og footer-kant
inde i samme spalte i stedet for at lade dem løbe ud i vinduskanten. `--wrap`
er tekstspalten *inde* i skallen. På telefon fylder siden fortsat hele
bredden.

**Heroens topluft** er `clamp(--s5, 11vh, 10rem)` og altså større end
bundpaddingen. Det er med vilje: kameraets stativ trækker kompositionens vægt
nedad, så symmetrisk padding ser topmast ud. Resten af første skærm kører en
fast 64 px-rytme.

**Første skærmbillede** skal rumme heroen og den praktiske stribe og intet
andet. Det styres af `#installer { padding-top: clamp(--s6, 34vh, 30rem) }`.
Afstanden er sat i `vh`, fordi pointen afhænger af skærmens højde — et fast
px-tal virkede kun på lave skærme. Loftet på 30rem holder til en synlig
skærmhøjde på ca. 1700 px; derover begynder "Første opgave" at titte frem.
Vokser den praktiske stribe med flere linjer, skal tallet regnes efter igen.

**Hero-kompositionen** er målt i procent af cirklen, ikke af skærmen.
Nosferatu ligger inde i `.hero__circle` netop derfor — flyttes den ud, går
placeringen i stykker på andre skærmbredder.

## Verificeret

- Alle tekst- og baggrundskombinationer målt mod WCAG AA. Laveste er 5,45:1.
- Ingen vandret side-scroll ved 375, 500, 721, 768, 1024, 1280, 1440, 1680
  eller 1920 px. Skallen måler 76 % på alle desktop-bredder.
- Tab-rækkefølge: spring-link → Start her → Åbn downloadsiden → Se videoen →
  videoafspilleren. Alle med synlig `:focus-visible`-ring.
- Siden står læsbar uden billeder, uden `animation-timeline` og under
  `prefers-reduced-motion: reduce`.
- 48 KB over folden, 265 KB for hele siden. Videoen hentes først ved klik
  (`preload="none"`) og hostes som GitHub Release-asset, ikke i repoet.

## Mangler

- Hosting: nyt GitHub-repo med Pages slået til.
- Nosferatu og kameraet er PNG. Som SVG ville de fylde et par KB i stedet for
  25 og kunne farves fra CSS-tokens.
