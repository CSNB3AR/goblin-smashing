#!/usr/bin/env python3
"""Audit a chapter file against the new chapter format.

Usage: python3 tools/chapter_check.py chapters/chapter-04.md [more files]

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
    "Haya Interply", "Embercore", "trophy", "confetti",
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
    if not re.fullmatch(r"\*\*\[END CHAPTER [A-Z ]+\]\*\*", tail):
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
    print(f"\n== {path} ({words} words) ==")
    print("MUST FIX:" if issues else "MUST FIX: none")
    for n, m in sorted(issues):
        print(f"  {n}: {m}")
    print(f"LOOK AT ({len(looks)}; about {words // 150} is fine):")
    for n, m in sorted(looks):
        print(f"  {n}: {m}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for p in sys.argv[1:]:
        check(p)
