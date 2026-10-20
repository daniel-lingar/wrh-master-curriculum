#!/usr/bin/env python3
"""Check Phase 4 artifacts and unchanged source; not scientific validation."""
from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
BASE = "d4b3910f49e7e4420a4968b0bdd72783cf3b5210"
ALLOWED = {
    "CURRICULUM_MAP.md", "docs/REMEDIATION_TRACKER.md",
    "docs/PHASE4_FIRST_RELEASE_RECOMMENDATION.md",
    "docs/PHASE4_EVIDENCE_DOSSIER_T3-T7.md",
    "docs/PHASE4_REVISION_PROPOSALS.md", "docs/PHASE4_IMPORT_VERIFICATION.md",
    "docs/verification/verify_phase4_artifacts.py",
}


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def check(condition, message):
    if not condition:
        raise SystemExit(message)


def main():
    sources, links = {}, set()

    def source(ref, path):
        key = (ref, path)
        if key not in sources:
            sources[key] = git("show", ref + ":" + path).decode()
        return sources[key]

    url_pattern = re.compile(
        r"https://github.com/daniel-lingar/wrh-master-curriculum/blob/"
        r"([a-f0-9]{40})/([^\s)#]+)(?:#L(\d+)(?:-L(\d+))?)?")
    documents = sorted((ROOT / "docs").glob("PHASE4_*.md"))
    for doc in documents:
        for match in url_pattern.finditer(doc.read_text()):
            ref, path, lo, hi = match.groups()
            lines = source(ref, path).splitlines()
            if lo:
                check(1 <= int(lo) <= int(hi or lo) <= len(lines),
                      "Invalid source range: " + match[0])
            links.add(match[0])

    proposal = (ROOT / "docs/PHASE4_REVISION_PROPOSALS.md").read_text()
    quote_pattern = re.compile(
        r'^- "(.*?)" — \[[^\]]*\]\(https://github.com/daniel-lingar/'
        r'wrh-master-curriculum/blob/([a-f0-9]{40})/([^#)]+)#L(\d+)(?:-L(\d+))?\)', re.M)
    count = 0
    for match in quote_pattern.finditer(proposal):
        quote, ref, path, lo, hi = match.groups()
        passage = "\n".join(source(ref, path).splitlines()[int(lo) - 1:int(hi or lo)])
        check(" ".join(quote.split()) in " ".join(passage.split()),
              f"Quotation mismatch: {path}:{lo}")
        count += 1
    check(count >= 25, "Missing representative proposal quotations")
    ids = re.findall(r"(?m)^## P4-(\d{2}) —", proposal)
    check(ids == [f"{n:02d}" for n in range(1, 14)], "Proposal IDs changed or missing")

    scope = (ROOT / "docs/PHASE4_FIRST_RELEASE_RECOMMENDATION.md").read_text()
    line_counts = 0
    for path, expected in re.findall(r"^- `([^`]+)` \((\d+) lines\)", scope, re.M):
        check(len(source(BASE, path).splitlines()) == int(expected),
              "Reported source line count mismatch: " + path)
        line_counts += 1

    changed = set(git("diff", "--name-only", BASE).decode().splitlines())
    changed.update(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
    check(changed <= ALLOWED, "Unexpected changes: " + repr(sorted(changed - ALLOWED)))
    protected = [p for p in git("ls-tree", "-r", "--name-only", BASE).decode().splitlines()
                 if p not in ALLOWED]
    for path in protected:
        check((ROOT / path).read_bytes() == git("show", BASE + ":" + path),
              "Protected file changed: " + path)
    missing = [p for p in (
        "docs/participant-workbooks/Workbook_Lessons_05_08.md",
        "docs/facilitator-guides/Facilitator_Guide_Lessons_01_04.md")
               if not (ROOT / p).exists()]
    print(json.dumps({"baseline": BASE, "pinned_links_checked": len(links),
                      "representative_proposal_quotes": count,
                      "proposal_count": len(ids), "reported_line_counts_checked": line_counts,
                      "protected_files_identical": len(protected),
                      "missing_development_companions": missing,
                      "scientific_validation": False, "delivery_approval": False}, indent=2))


if __name__ == "__main__":
    main()
