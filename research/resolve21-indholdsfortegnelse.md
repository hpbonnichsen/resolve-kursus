# Indholdsfortegnelse — Making Videos in Resolve 21 (Full Course for Beginners)

Kilde: YouTube-video `gjxiH2Tm4JE`, 1 t 24 min. Fuldt transskript i
[resolve21-fuldt-kursus.md](resolve21-fuldt-kursus.md). Alle tidsstempler er klikbare
og springer til det rigtige sted i videoen.

Videoen bruger et Star Wars-fanfilmsklip som gennemgående øvelsesmateriale — alle
eksempler er fra samme lille scene, som deltagerne henter og redigerer med.

---

## 1. Kom i gang — [00:00:00](https://youtu.be/gjxiH2Tm4JE?t=0)

| Tid | Emne |
|---|---|
| [00:00:55](https://youtu.be/gjxiH2Tm4JE?t=55) | Download af Resolve 21; gratis vs. Studio (295 $ engangsbeløb) |
| [00:01:30](https://youtu.be/gjxiH2Tm4JE?t=90) | Project Manager: hvor projekter oprettes, åbnes og gemmes |
| [00:02:03](https://youtu.be/gjxiH2Tm4JE?t=123) | Hurtigste vej ind: træk footage direkte i timeline |
| [00:02:33](https://youtu.be/gjxiH2Tm4JE?t=153) | Quick Export med YouTube-preset — færdig video på to minutter |
| [00:03:28](https://youtu.be/gjxiH2Tm4JE?t=208) | Sidernes logik: hver side er reelt et selvstændigt program |

Gennemgang af Media, Cut, Edit, Photo (ny i 21), Fusion, Color, Fairlight og Deliver.
Pointe han vender tilbage til: Cut, Photo og Media kan ignoreres 90 % af tiden, og
overflødige sider kan skjules under Workspace → Show Page.

## 2. Edit-siden — [00:07:11](https://youtu.be/gjxiH2Tm4JE?t=431)

| Tid | Emne |
|---|---|
| [00:07:11](https://youtu.be/gjxiH2Tm4JE?t=431) | Import af media; bins som mappestruktur |
| [00:08:27](https://youtu.be/gjxiH2Tm4JE?t=507) | Interfacets fire dele: media pool, source viewer, timeline viewer, timeline |
| [00:09:42](https://youtu.be/gjxiH2Tm4JE?t=582) | In- og out-punkter i source viewer |
| [00:10:11](https://youtu.be/gjxiH2Tm4JE?t=611) | Trimning direkte i timeline, rækkefølge, fjern tomrum |
| [00:16:25](https://youtu.be/gjxiH2Tm4JE?t=985) | Spor: øverste videospor vinder, al lyd lægges sammen; sporhøjde |
| [00:18:30](https://youtu.be/gjxiH2Tm4JE?t=1110) | Split af klip: barberblad og Ctrl+\ |
| [00:19:43](https://youtu.be/gjxiH2Tm4JE?t=1183) | Ripple trim (Ctrl+Shift+[ og ]) — hans mest brugte genvej |
| [00:22:13](https://youtu.be/gjxiH2Tm4JE?t=1333) | Link/unlink af lyd og billede; J-cut og L-cut; roll |
| [00:23:42](https://youtu.be/gjxiH2Tm4JE?t=1422) | Cross dissolve — og hvorfor den er det forkerte værktøj til at blødgøre et klip |
| [00:24:36](https://youtu.be/gjxiH2Tm4JE?t=1476) | Inspector: transform, position, rotation, crop |
| [00:25:48](https://youtu.be/gjxiH2Tm4JE?t=1548) | Dynamic zoom — automatisk bevægelse på klip og stillbilleder |
| [00:26:39](https://youtu.be/gjxiH2Tm4JE?t=1599) | Effects-panelet: træk en effekt på et klip, juster, slå fra, slet |
| [00:27:40](https://youtu.be/gjxiH2Tm4JE?t=1660) | Titler og tekst: font, tracking, stroke, drop shadow, baggrund |

**Farvestyring — [00:12:48](https://youtu.be/gjxiH2Tm4JE?t=768)** ligger midt i dette afsnit som en sidevej: hvorfor
log-footage ser gråt ud, [00:13:38](https://youtu.be/gjxiH2Tm4JE?t=818) opsætning under Project Settings → Color Management
(DaVinci YRGB Color Managed + HDR DaVinci Wide Gamut Intermediate), og [00:14:58](https://youtu.be/gjxiH2Tm4JE?t=898)
Input Color Space pr. klip. To menuvalg, ingen teori — og billedet bliver brugbart at
klippe i.

## 3. Fusion — [00:29:33](https://youtu.be/gjxiH2Tm4JE?t=1773)

| Tid | Emne |
|---|---|
| [00:29:33](https://youtu.be/gjxiH2Tm4JE?t=1773) | Åbn et klip fra timeline i Fusion; ændringen lever i timelinen |
| [00:32:12](https://youtu.be/gjxiH2Tm4JE?t=1932) | Node graph som flowdiagram: MediaIn → MediaOut |
| [00:33:12](https://youtu.be/gjxiH2Tm4JE?t=1992) | Første node kobles ind i flowet; over 300 nodes findes — de fleste er ligegyldige |
| [00:34:59](https://youtu.be/gjxiH2Tm4JE?t=2099) | **De fire nodetyper** — hele afsnittets bærende idé |
| [00:34:59](https://youtu.be/gjxiH2Tm4JE?t=2099) | Image: råmateriale (footage, background, text) |
| [00:36:07](https://youtu.be/gjxiH2Tm4JE?t=2167) | Effect: ændrer det der løber igennem (blur, color corrector, transform) |
| [00:38:02](https://youtu.be/gjxiH2Tm4JE?t=2282) | Merge: lægger ét billede over et andet — Fusions svar på lag |
| [00:39:56](https://youtu.be/gjxiH2Tm4JE?t=2396) | Mask: styrer gennemsigtighed; tekst placeret bag en person |

## 4. Color — [00:42:08](https://youtu.be/gjxiH2Tm4JE?t=2528)

Videoens længste og mest gennemarbejdede afsnit (24 min).

| Tid | Emne |
|---|---|
| [00:42:08](https://youtu.be/gjxiH2Tm4JE?t=2528) | Color-sidens layout aflæst i fire dele; skjul paneler for at få ro |
| [00:45:19](https://youtu.be/gjxiH2Tm4JE?t=2719) | Primary color wheels — det eneste panel begyndere behøver |
| [00:46:08](https://youtu.be/gjxiH2Tm4JE?t=2768) | Lift, gamma, gain og offset: lysstyrke pr. toneområde |
| [00:47:27](https://youtu.be/gjxiH2Tm4JE?t=2847) | Farvehjulene: temperatur og tint pr. toneområde |
| [00:49:00](https://youtu.be/gjxiH2Tm4JE?t=2940) | Contrast, pivot, saturation; Shift+D slår grade fra og til |
| [00:52:00](https://youtu.be/gjxiH2Tm4JE?t=3120) | Hans arbejdsgang på ét billede: lysstyrke → kontrast → mætning → temperatur |
| [00:54:18](https://youtu.be/gjxiH2Tm4JE?t=3258) | **Shot matching:** saml alle klip i en gruppe |
| [00:54:56](https://youtu.be/gjxiH2Tm4JE?t=3296) | Group post clip — én justering rammer alle klip |
| [00:55:55](https://youtu.be/gjxiH2Tm4JE?t=3355) | Vælg et referenceshot med fælles elementer |
| [00:57:07](https://youtu.be/gjxiH2Tm4JE?t=3427) | Grab Still og Play Still: split screen til sammenligning |
| [00:58:58](https://youtu.be/gjxiH2Tm4JE?t=3538) | Serielle nodes som adskilte trin; node labels |
| [01:01:13](https://youtu.be/gjxiH2Tm4JE?t=3673) | **ECTO-metoden** — fire navngivne, tomme nodes som tjekliste: Exposure, Contrast, Temperature/saturation, Other |
| [01:03:36](https://youtu.be/gjxiH2Tm4JE?t=3816) | Shot for shot mod referencen; Ctrl+D viser før/efter |

Hans konklusion: arbejdsgangen betyder mere end værktøjskendskabet. Ingen lægger mærke
til en vignette, hvis klippene ikke matcher hinanden.

## 5. Fairlight — [01:06:42](https://youtu.be/gjxiH2Tm4JE?t=4002)

| Tid | Emne |
|---|---|
| [01:06:42](https://youtu.be/gjxiH2Tm4JE?t=4002) | Samme timeline som Edit-siden — ændringer slår igennem begge veje |
| [01:08:01](https://youtu.be/gjxiH2Tm4JE?t=4081) | Store spor og volumenkurve med Alt-klik |
| [01:09:06](https://youtu.be/gjxiH2Tm4JE?t=4146) | Sporfoldere (nyt i Resolve 21) til projekter med mange spor |
| [01:10:00](https://youtu.be/gjxiH2Tm4JE?t=4200) | Opbygning af lydsiden: ét spor pr. karakter, ambience, effekter, navngivning |
| [01:12:28](https://youtu.be/gjxiH2Tm4JE?t=4348) | Mixeren: faders pr. spor |
| [01:13:04](https://youtu.be/gjxiH2Tm4JE?t=4384) | Busser: rut flere spor gennem én kanal og læg fælles effekt på (reverb) |
| [01:15:34](https://youtu.be/gjxiH2Tm4JE?t=4534) | Dynamics/kompressor — dialogue level expander og makeup gain |
| [01:16:31](https://youtu.be/gjxiH2Tm4JE?t=4591) | EQ pr. spor; hørbare eksempler på telefon- og naborumslyd |

## 6. Deliver — [01:18:02](https://youtu.be/gjxiH2Tm4JE?t=4682)

| Tid | Emne |
|---|---|
| [01:18:02](https://youtu.be/gjxiH2Tm4JE?t=4682) | Deliver-siden og presets |
| [01:19:16](https://youtu.be/gjxiH2Tm4JE?t=4756) | Delingsversion: H.265 Master, sat til UHD så YouTube komprimerer mildere |
| [01:20:33](https://youtu.be/gjxiH2Tm4JE?t=4833) | Arkivversion: ProRes 422 HQ med alle timeline-spor som separate lydspor |
| [01:21:39](https://youtu.be/gjxiH2Tm4JE?t=4899) | Render queue og Render All — begge versioner på én gang |

## 7. Afslutning — [01:22:23](https://youtu.be/gjxiH2Tm4JE?t=4943)

Reklame for hans betalte community (Ground Control Film School) og gentagelse af
tilbuddet om gratis øvelsesmateriale. Intet fagligt indhold.

---

## Tidsfordeling

| Afsnit | Varighed |
|---|---|
| Kom i gang | 7 min |
| Edit | 22 min |
| Fusion | 13 min |
| Color | 24 min |
| Fairlight | 11 min |
| Deliver | 4 min |
| Afslutning | 2 min |
