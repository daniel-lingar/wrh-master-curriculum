#!/usr/bin/env python3
"""Check Phase 3 source integrity; this cannot verify evidence or reading activity."""

from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[2]
BASE = "9ee354b42f622dcdc789f017ca8dc189bb649f0c"
PREFIX = f"https://github.com/daniel-lingar/wrh-master-curriculum/blob/{BASE}/"
ALLOWED = {
    "docs/EVIDENCE_REGISTER.md",
    "docs/REMEDIATION_TRACKER.md",
    "docs/PHASE3_FINDINGS_REPORT.md",
    "docs/PHASE3_READING_LEDGER.md",
    "docs/PHASE3_REVIEW_BACKLOG.md",
    "docs/PHASE3_PROPOSED_EDITORIAL_ACTIONS.md",
    "docs/PHASE3_IMPORT_VERIFICATION.md",
    "docs/verification/verify_phase3_inventory.py",
}


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT).decode()


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def locator(path, lo, hi):
    return PREFIX + path + f"#L{lo}" + (f"-L{hi}" if hi != lo else "")


def main():
    register = (ROOT / "docs/EVIDENCE_REGISTER.md").read_text()
    parts = re.split(r"(?m)^### WRH-ER-", register)[1:]
    ids = [int(part.split(" ", 1)[0]) for part in parts]
    require(ids == list(range(1, max(ids) + 1)), "Missing or duplicate entry IDs")
    old = git("show", BASE + ":docs/EVIDENCE_REGISTER.md")
    pattern = r"(?ms)^### WRH-ER-001.*?(?=^## Phase 2 status summary)"
    require(re.search(pattern, old)[0] == re.search(pattern, register)[0],
            "Earlier entries ER-001–015 changed")

    sources = {}

    def source(path):
        if path not in sources:
            sources[path] = git("show", BASE + ":" + path)
        return sources[path]

    locations = defaultdict(set)
    quotes = {}
    priorities, kinds, tags = Counter(), Counter(), Counter()
    count = exact = additional_links = 0
    primary = re.compile(
        r'1\. \*\*Exact claim \(verbatim\):\*\* "(.*?)" — `([^`]+)` '
        r'\(\[baseline passage\]\(([^)]+)\)\), line (\d+)(?:[–-](\d+))?\.', re.S)
    additional = re.compile(
        r'`([^`]+)` line (\d+)(?:[–-](\d+))? '
        r'\(\[baseline passage\]\(([^)]+)\)\)')

    for part in parts[15:]:
        entry = int(part.split(" ", 1)[0])
        label = f"ER-{entry:03d}"
        field = part.split("\n2.")[0]
        match = primary.search(field)
        require(match is not None, f"{label}: malformed field 1")
        quote, path, url, lo, hi = match.groups()
        lo, hi = int(lo), int(hi or lo)
        records = [(path, lo, hi, url)]
        more = [(p, int(a), int(b or a), u)
                for p, a, b, u in additional.findall(field[match.end():])]
        records.extend(more)
        require(len(re.findall(r"`[^`]+` line \d+", field[match.end():])) == len(more),
                f"{label}: additional locator lacks immutable link")
        total = re.search(r"Additional occurrences \((\d+) more; (\d+) total\)", field)
        if more:
            require(total and (int(total[1]), int(total[2])) == (len(more), len(records)),
                    f"{label}: incorrect occurrence summary")
        else:
            require(total is None, f"{label}: empty additional-occurrence summary")
        additional_links += len(more)
        query = re.compile(re.escape(" ".join(quote.split())).replace(r"\ ", r"\s+"))
        quotes[entry] = query
        for p, a, b, u in records:
            require(u == locator(p, a, b), f"{label}: incorrect baseline URL")
            text = source(p)
            lines = text.splitlines(keepends=True)
            require(1 <= a <= b <= len(lines), f"{label}: line range outside source")
            fragment = "".join(lines[a - 1:b])
            matches = list(query.finditer(fragment))
            require(len(matches) == 1, f"{label}: missing or ambiguous quotation at {p}:{a}")
            offset = sum(map(len, lines[:a - 1]))
            key = (p, offset + matches[0].start(), offset + matches[0].end())
            require(key not in locations[entry], f"{label}: duplicate source span")
            locations[entry].add(key)
            count += 1
            exact += quote in fragment
        for number in range(1, 8):
            require(re.search(rf"^{number}\. \*\*", part, re.M),
                    f"{label}: missing schema field {number}")
        for required in ("Not investigated in Phase 3",
                         "6. **Independent reviewer:** PENDING",
                         "7. **Revision version:** PENDING"):
            require(required in part, f"{label}: missing status {required}")
        priority = re.search(r"Phase 3 inventory priority: (P[123])", part)
        kind = re.search(r"\*\*Kind \(Phase 3 inventory classification\):\*\* ([^.]+)", part)
        tag = re.search(r"Claim types recorded: ([^.]+)", part)
        require(priority and kind and tag, f"{label}: missing triage metadata")
        priorities[priority[1]] += 1
        kinds[kind[1]] += 1
        tags.update(t.strip() for t in tag[1].split(","))

    ledger = (ROOT / "docs/PHASE3_READING_LEDGER.md").read_text()
    ledger_paths = set()
    for line in ledger.splitlines():
        if not line.startswith("| "):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3 or not re.fullmatch(r"`[0-9a-f]{40}`", cells[2]):
            continue
        path, blob = cells[1].strip("`"), cells[2].strip("`")
        require(blob == git("rev-parse", BASE + ":" + path).strip(),
                f"Ledger blob mismatch: {path}")
        require(path not in ledger_paths, f"Duplicate ledger path: {path}")
        ledger_paths.add(path)
        if len(cells) == 8:
            require(int(cells[3]) == len(source(path).splitlines()),
                    f"Ledger line count mismatch: {path}")
    numbered = {p for p in git("ls-tree", "-r", "--name-only", BASE).splitlines()
                if re.fullmatch(r"Part-(?:I|II|III|IV)/Session_\d+_.+\.md", p)
                and p != "Part-I/Session_12_Pilot_Portal.md"}
    corpus = numbered | {"Part-IV/Crisis_Package.md"}
    expected_ledger = corpus | {"Part-I/Session_12_Pilot_Portal.md"}
    require(ledger_paths == expected_ledger, "Ledger omits or adds a corpus document")
    for entry, query in quotes.items():
        for path in corpus:
            for match in query.finditer(source(path)):
                require((path, match.start(), match.end()) in locations[entry],
                        f"ER-{entry:03d}: unlisted exact-wording location in {path}")

    changed = set(git("diff", "--name-only", BASE).splitlines())
    changed.update(git("ls-files", "--others", "--exclude-standard").splitlines())
    require(changed <= ALLOWED, "Unexpected changed files: " + repr(sorted(changed - ALLOWED)))
    print(json.dumps({"baseline": BASE, "entries": len(parts), "new_entries": len(quotes),
                      "entry_location_records": count, "raw_exact_matches": exact,
                      "whitespace_normalized_only": count - exact,
                      "additional_immutable_links": additional_links,
                      "multi_location_entries": sum(len(v) > 1 for v in locations.values()),
                      "ledger_blobs_verified": len(ledger_paths),
                      "numbered_session_files": len(numbered),
                      "priorities": dict(priorities), "kinds": dict(kinds),
                      "tags": dict(tags), "earlier_15_unchanged": True,
                      "protected_paths_unchanged": True}, indent=2))


if __name__ == "__main__":
    main()
