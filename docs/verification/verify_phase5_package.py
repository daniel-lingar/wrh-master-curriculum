#!/usr/bin/env python3
"""Verify the Phase 5 source snapshot and package structure; no scientific approval.

This scope guard is phase-specific. Run it on the Phase 5 snapshot after later
phases legitimately modify source, rather than loosening its protected paths.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
BASE = '7b3dd114dbf562d593cd1c12dae0d2a919c90c5f'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def check(value, message):
    if not value:
        raise SystemExit(message)


def blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def main():
    obj = json.loads((ROOT / 'docs/verification/phase5_claim_trace.json').read_text())
    components, records = obj['components'], obj['records']
    check(obj['baseline'] == BASE, 'Wrong baseline')
    check(len(components) == 12 and len({c['path'] for c in components}) == 12,
          'Expected twelve distinct package components')
    check([r['id'] for r in records] ==
          [f'WRH-D-ER-{n:03d}' for n in range(1, len(records) + 1)], 'ID gap/duplicate')
    check(len(records) >= 126, 'Imported IDs lost')
    allowed = {c['path'] for c in components} | {
        'CURRICULUM_MAP.md', 'docs/REMEDIATION_TRACKER.md',
        'docs/core-curriculum/README.md', 'docs/participant-workbooks/README.md',
        'docs/PHASE5_LANE_D_CLAIM_REGISTER.md', 'docs/PHASE5_PACKAGE_MANIFEST.md',
        'docs/PHASE5_IMPORT_VERIFICATION.md',
        'docs/verification/phase5_claim_trace.json',
        'docs/verification/verify_phase5_package.py',
    }
    changed = set(git('diff', '--name-only', BASE).decode().splitlines())
    changed.update(git('ls-files', '--others', '--exclude-standard').decode().splitlines())
    check(changed <= allowed, 'Unauthorized paths: ' + repr(sorted(changed - allowed)))
    protected = [p for p in git('ls-tree', '-r', '--name-only', BASE).decode().splitlines()
                 if p not in allowed]
    for path in protected:
        check((ROOT / path).read_bytes() == git('show', BASE + ':' + path),
              'Protected file changed: ' + path)
    manifest = (ROOT / 'docs/PHASE5_PACKAGE_MANIFEST.md').read_text()
    component_map = {c['path']: c for c in components}
    for c in components:
        data = (ROOT / c['path']).read_bytes()
        check(blob(data) == c['current_blob'], 'Component hash changed: ' + c['path'])
        check(len(data) == c['bytes'] and len(data.decode().splitlines()) == c['line_count'],
              'Component size/lines mismatch: ' + c['path'])
        check(c['current_blob'] in manifest, 'Missing manifest hash: ' + c['path'])
        check('NOT FOR DELIVERY' in '\n'.join(data.decode().splitlines()[:12]), 'Missing draft banner')
        if c['baseline_blob']:
            check(blob(git('show', BASE + ':' + c['path'])) == c['baseline_blob'],
                  'Baseline blob mismatch')
    excerpt_count = origin_count = 0
    for r in records:
        check(r['path'] in component_map, 'Claim outside package')
        check(r['current_blob'] == component_map[r['path']]['current_blob'],
              'Claim component blob mismatch')
        check(r['reviewer'] == 'PENDING — no reviewer assigned; no decision recorded.',
              'Unexpected reviewer disposition')
        for mode, source in (
                ('origin', git('cat-file', 'blob', r['origin_blob']).decode()),
                ('current', (ROOT / r['path']).read_text())):
            check(bool(r[mode + '_excerpts']), 'Missing excerpt: ' + r['id'])
            lines = source.splitlines()
            for q in r[mode + '_excerpts']:
                a, b = q['start_line'], q['end_line']
                check(1 <= a <= b <= len(lines), 'Invalid line range: ' + r['id'])
                check('\n'.join(lines[a - 1:b]) == q['quote'],
                      'Non-verbatim excerpt: ' + r['id'] + ' ' + mode)
                if mode == 'current':
                    excerpt_count += 1
                else:
                    origin_count += 1
    register = (ROOT / 'docs/PHASE5_LANE_D_CLAIM_REGISTER.md').read_text()
    ids = re.findall(r'^\| (WRH-D-ER-\d+) \|', register, re.M)
    check(ids == [r['id'] for r in records], 'Markdown/JSON ID mismatch')
    check({c['path'] for c in components} == {r['path'] for r in records},
          'At least one component omitted from representative register')
    track_count = 0
    expected_steps = ['Recognize', 'Name', 'Explain', 'Separate', 'Interrupt', 'Practice', 'Carry It']
    for c in components:
        if not re.search(r'/Lesson_\d{2}_', c['path']):
            continue
        source = (ROOT / c['path']).read_text()
        tracks = re.split(r'^## (Corrections|Reentry|Veteran|Workplace) Track\s*$', source,
                          flags=re.M)
        check(len(tracks) == 9, 'Track count mismatch: ' + c['path'])
        for name, text in zip(tracks[1::2], tracks[2::2]):
            application = text.split('### 4. Seven-Step Application', 1)[1].split('### 5.', 1)[0]
            steps = re.findall(r'^\*\*([^*]+)\*\*\s*$', application, re.M)
            check(steps == expected_steps, 'Seven-step mismatch: ' + c['path'] + ' ' + name)
            track_count += 1
    workbook_lessons = 0
    for c in components:
        if not c['id'].startswith('WB'):
            continue
        source = (ROOT / c['path']).read_text()
        blocks = re.split(r'^# CORE LESSON \d+\s*$', source, flags=re.M)[1:]
        check(len(blocks) == 4, 'Workbook lesson count')
        for text in blocks:
            sections = re.findall(r'^## (\d+)\. ', text, re.M)
            check(sections == [str(n) for n in range(1, 16)], 'Workbook section sequence')
            workbook_lessons += 1
    guide = (ROOT / 'docs/facilitator-guides/Facilitator_Guide_Lessons_05_08.md').read_text()
    for n in range(5, 9):
        check(f'## Development teaching plan — D-{n:02d}' in guide, 'Missing guide plan')
    check(guide.count('| Track | Lesson scenario | Track Carry-Forward |') == 4,
          'Missing setting tables')
    forbidden = ('Knowing the difference prevents wasted effort and unnecessary conflict.',
                 'They do not erase personal choice.', 'Both eliminate agency.',
                 'The score measures **skill application**')
    all_components = '\n'.join((ROOT / c['path']).read_text() for c in components)
    check(not any(t in all_components for t in forbidden), 'Selected obsolete assertion remains')
    catalog = json.loads((ROOT / 'assets/data/sessions.json').read_text())
    check(catalog['count'] == 0 and catalog['sessions'] == [] and
          catalog['status'] == 'withdrawn_pending_independent_review', 'Catalog not withdrawn')
    check('**Gates satisfied: 0 of 6.' in
          (ROOT / 'docs/REMEDIATION_TRACKER.md').read_text(), 'Gate status changed')
    print(json.dumps({'components': len(components), 'representative_entries': len(records),
                      'current_verbatim_excerpts': excerpt_count,
                      'origin_verbatim_excerpts': origin_count,
                      'four_track_applications': track_count, 'workbook_lessons': workbook_lessons,
                      'protected_baseline_files': len(protected),
                      'scientific_validation': False, 'delivery_approval': False}, indent=2))


if __name__ == '__main__':
    main()
