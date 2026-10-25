#!/usr/bin/env python3
"""Audit a chapter file against the new chapter format.

Usage: python3 tools/chapter_check.py chapters/chapter-04-new.md [--source chapters/chapter-03.md] [more files]\n--source prints the length change against the old chapter and warns on growth over 5 percent.

Reports, by line: rule breaks that are certain (em dashes, stale terms, narrator
pronoun leaks) and lines worth a human look (figures, filter words, repeated
body cues, unquoted thoughts). It never edits anything.
"""
import re
import sys

STALE = [
    "Winter Bash", "Crystal League", "Worlds", "World Championship", "esports",
    "scrim", "meta", "5v5", "3v3", "five-on-five", "three-on-three",
    "seven-day", "seven days", "Rookie of the Year", "Snowy Plains",
    "Siege mode", "Pro League", "pro league", "roster", "analyst",
    "Haya Interply", "Embercore", "trophy", "graph paper",
]
FILTER = r"\b(felt|realized|seemed|noticed|watched as|could tell)\b"
FIGURE = r"\b(like a|like an|as if|as though|almost like|the way (a|an|the))\b"
CUES = [
    "heel of my hand", "rubbed my eyes", "pressed my palm", "ran a hand",
    "jaw tightened", "jaw set", "swallowed", "exhaled", "let out a breath",
    "my hands were shaking", "hands shook", "blinked hard", "squinted",
    "raked", "scratched my", "touched my beard", "tugged", "my earring",
    "twisted a loc", "pressed my thumb",
]
CRUTCHES = {
    "jaw": r"\bjaw\b",
    "stomach": r"\bstomach (dropped|turned|lurched|clenched)|\bstomach drop",
    "pulse": r"\bpulse\b",
    "breath out/held": r"breath(ed)? out|let out a breath|held my breath|breath caught|exhaled",
    "shoulders": r"\bshoulders (came up|dropped|tightened|sagged|were wound)",
    "knee": r"\bknee (was )?bouncing",
    "hands flat": r"\bhands? (went )?flat",
    "throat": r"\bthroat (tight|closed|did)",
    "heat neck": r"heat (climbed|crawled|rose|crept)",
    "blinked hard": r"blinked hard",
}
LEAK = r"\b(he|his|him|himself)\b"
BOLD_TOKEN = re.compile(r"\*\*\*?\[.*?\]\*\*\*?")


def strip_dialogue(line):
    return re.sub(r"[\"“][^\"”]*[\"”]", "", line)


def check(path):
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    words = len(re.findall(r"\w+", text))
    issues, looks, pron = [], [], []
    cue_hits = {c: [] for c in CUES}

    first = next((l for l in lines if l.strip()), "")
    if not re.match(r"# Chapter \w+: .+", first):
        issues.append((1, f"title should read '# Chapter Three: Title', got: {first[:50]}"))
    tail = [l for l in lines if l.strip()][-1] if text.strip() else ""
    if not re.fullmatch(r"\*\*\[END CHAPTER [A-Z ]+(, PART \w+)?\]\*\*", tail):
        issues.append((len(lines), f"last line should be **[END CHAPTER N]**, got: {tail[:50]}"))

    for n, line in enumerate(lines, 1):
        if not line.strip():
            continue
        plain = BOLD_TOKEN.sub("", line)
        if "—" in plain or "–" in plain:
            issues.append((n, "em/en dash outside bold system text"))
        for term in STALE:
            if re.search(r"\b" + re.escape(term) + r"\b", line, re.I if term.islower() else 0):
                issues.append((n, f"stale or banned term: {term}"))
        narr = strip_dialogue(plain)
        if re.search(LEAK, narr, re.I) and not re.search(r"\*\"", narr):
            pron.append(n)
        if re.search(r"\bTatsuya\b", narr):
            looks.append((n, "'Tatsuya' in narration"))
        if re.search(FILTER, narr):
            looks.append((n, "filter word"))
        if re.search(FIGURE, narr, re.I):
            looks.append((n, "figure of speech: check it comes from his world"))
        if re.search(r"\bI (thought|wondered)\b", narr) and '*"' not in narr:
            looks.append((n, "thought as narration: direct thoughts take *\"...\"*"))
        if (len(plain.split()) <= 22 and re.search(r"\bI\b|\bmy\b", plain)
                and '"' not in plain and not plain.startswith(("*", "#", "**"))
                and re.search(r"[.?!]$", plain.strip())):
            looks.append((n, "short first-person line: a thought? take *\"...\"* if direct"))
        low = line.lower()
        for c in CUES:
            if c in low:
                cue_hits[c].append(n)

    for c, ns in cue_hits.items():
        if len(ns) >= 3:
            looks.append((ns[0], f"cue '{c}' used {len(ns)} times (lines {ns})"))

    if pron:
        looks.append((pron[0], f"he/his/him in narration on {len(pron)} lines, "
                      f"narrator leak or another man (Leon, Eren, Dad): {pron}"))
    crut = {k: [i + 1 for i, l in enumerate(lines) if re.search(v, l, re.I)]
            for k, v in CRUTCHES.items()}
    for k, ns in crut.items():
        if len(ns) > 1:
            issues.append((ns[1], f"crutch cue '{k}' used {len(ns)} times (cap is 1): lines {ns}"))
    print(f"\n== {path} ({words} words) ==")
    print("MUST FIX:" if issues else "MUST FIX: none")
    for n, m in sorted(issues):
        print(f"  {n}: {m}")
    print(f"LOOK AT ({len(looks)}; about {words // 150} is fine):")
    for n, m in sorted(looks):
        print(f"  {n}: {m}")


def compare(path, source):
    new = len(open(path, encoding="utf-8").read().split())
    old = len(open(source, encoding="utf-8").read().split())
    pct = (new - old) / old * 100
    flag = "  <- GREW MORE THAN 5%, fold new beats into old lines" if pct > 5 else ""
    print(f"LENGTH: {old} -> {new} words ({pct:+.1f}%){flag}")


if __name__ == "__main__":
    args = sys.argv[1:]
    source = None
    if "--source" in args:
        i = args.index("--source")
        source = args[i + 1]
        del args[i:i + 2]
    if not args:
        sys.exit(__doc__)
    for p in args:
        check(p)
        if source:
            compare(p, source)
