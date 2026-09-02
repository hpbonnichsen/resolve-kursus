#!/usr/bin/env python3
"""Konverter en YouTube-SRT til laesbar Markdown.

YouTubes auto-undertekster bruger et rullende to-linjers format, hvor hver
saetning gentages i flere cues. Scriptet fjerner gentagelserne, samler teksten
til afsnit og saetter en tidsstemplet overskrift med jaevne mellemrum.

Brug:  python3 srt2md.py input.srt output.md [minutter-pr-afsnit]
"""
import re
import sys
import textwrap

TIME = re.compile(r"(\d{2}):(\d{2}):(\d{2})[,.](\d{3})\s*-->")


def parse(path):
    """Returner [(sekunder, linje)] uden de rullende gentagelser."""
    out, seen, start = [], set(), 0
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        m = TIME.match(line)
        if m:
            h, mi, s, _ = map(int, m.groups())
            start = h * 3600 + mi * 60 + s
            continue
        line = line.strip()
        if not line or line.isdigit() or line in seen:
            continue
        seen.add(line)
        out.append((start, line))
    return out


def stamp(sec):
    return f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}"


def main():
    src, dst = sys.argv[1], sys.argv[2]
    step = int(sys.argv[3]) * 60 if len(sys.argv) > 3 else 300

    cues = parse(src)
    if not cues:
        sys.exit(f"Ingen tekst fundet i {src}")

    title = src.rsplit("/", 1)[-1].rsplit(".", 2)[0]
    md = [f"# {title}\n", f"Varighed: {stamp(cues[-1][0])} — {sum(len(t.split()) for _, t in cues)} ord.\n"]

    section, buf = -1, []

    def flush():
        if buf:
            md.append(textwrap.fill(" ".join(buf), 88) + "\n")
            buf.clear()

    for sec, text in cues:
        if sec // step > section:
            flush()
            section = sec // step
            md.append(f"## [{stamp(section * step)}]\n")
        buf.append(text)
    flush()

    open(dst, "w", encoding="utf-8").write("\n".join(md))
    print(f"Skrev {dst}")


if __name__ == "__main__":
    main()
