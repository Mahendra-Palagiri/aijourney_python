"""Read-only verification of the curated visual inventory and recoverable archives."""
import hashlib
import json
import re
import math
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
manifest = json.loads(Path(__file__).with_name('curated-visuals.json').read_text())
paths = [(ROOT / entry['path']).resolve() for entry in manifest['assets']]
assert len(paths) == len(set(paths)), 'Duplicate active asset'
png_count = 0
weekly_count = 0
for entry, path in zip(manifest['assets'], paths):
    assert ROOT in path.parents and path.is_file(), path
    if path.suffix == '.png':
        with Image.open(path) as image:
            assert image.format == 'PNG', path
            if entry['type'] in ('weekly', 'worked_diagram'):
                assert image.size == (2560, 1600), (path, image.size)
            image.verify()
        png_count += 1
    if entry['type'] == 'weekly':
        assert len(list(path.parent.glob('0.1.*'))) == 1, path
        weekly_count += 1
    if entry.get('source'):
        assert (ROOT / entry['source']).is_file(), entry['source']
    if entry.get('renderer'):
        prefix = re.match(r'\d+\.\d+\.', path.name).group(0)
        assert len(list(path.parent.glob(prefix + '*'))) == 1, path

for entry in manifest['archive']:
    source = Path(entry['source']).resolve()
    target = Path(entry['destination']).resolve()
    assert ROOT in source.parents and ROOT in target.parents
    assert not source.exists(), source
    assert target.is_file(), target
    assert hashlib.sha256(target.read_bytes()).hexdigest() == entry['sha256'], target

for entry in manifest.get('replacedOriginals', []):
    target = (ROOT / entry['archivePath']).resolve()
    assert ROOT in target.parents and target.is_file(), target
    assert hashlib.sha256(target.read_bytes()).hexdigest() == entry['sha256'], target

for entry in manifest.get('refinementArchives', []):
    target = (ROOT / entry['archivePath']).resolve()
    assert ROOT in target.parents and target.is_file(), target
    assert hashlib.sha256(target.read_bytes()).hexdigest() == entry['sha256'], target

audit = json.loads((ROOT / 'docs/lesson-visual-progress.json').read_text())
assert sum(item['status'] == 'superseded_archived' for item in audit['lessons']) == 76
assert sum(item['status'] == 'retained' for item in audit['lessons']) == 7
for filename in ('README.md', 'STATUS.md'):
    document = Path(__file__).with_name(filename)
    if not document.exists():
        continue
    for link in re.findall(r'\]\(([^)]+)\)', document.read_text()):
        if '://' not in link and not link.startswith('#'):
            assert (document.parent / link.split('#')[0]).resolve().exists(), (filename, link)

assert weekly_count == 10
assert len(manifest['archive']) == 76
assert {entry['week'] for entry in manifest['weeks']} == set(range(1, 15))
# Numerical facts shown in the corrected Day 1 diagram.
assert abs(((191 / 255) - .5) / .5 - .4980392156862745) < 1e-12
assert (.75 - .5) / .5 == .5
# Subset membership in the illustrative Day 2 diagram.
indices = [7, 2, 9, 0, 5, 1, 8, 4, 6, 3]
assert sorted(indices) == list(range(10))
assert not set(indices[:8]) & set(indices[8:])
assert indices[0] == 7 and indices[8] == 6
# Check the arithmetic the new diagrams teach, independently of their drawing code.
assert math.isclose((64*1 + 16*3) / 80, 1.4)
assert math.isclose(sum([.80,.84,.82,.78,.86])/5, .82)
assert math.isclose(2*(math.log(4/3)+1), 2.5753641449035616)
assert math.isclose((1*2+2*1) / (math.sqrt(5)*math.sqrt(5)), .8)
scores = [.1,.2,.35,.45,.55,.65,.75,.9]
labels = [0,1,0,1,0,1,1,1]
wins = sum(p > n for p, py in zip(scores,labels) if py == 1
           for n, ny in zip(scores,labels) if ny == 0)
assert wins == 12 and wins / 15 == .8
assert math.isclose(34/14, 2.4285714285714284)
assert math.isclose(34/15, 2.2666666666666666)
assert 1+6+11 == 18 and 16*16*16 == 4096
input_cells = [[1,2,0],[0,3,1],[2,1,4]]
output_cells = [[input_cells[r][c]+input_cells[r+1][c+1] for c in range(2)] for r in range(2)]
assert output_cells == [[4,3],[1,7]]
assert sum(map(sum, output_cells))/4 == 3.75
for x1,x2,expected in [(0,0,0),(1,1,0),(1,0,1),(0,1,1)]:
    assert max(0,x1-x2)+max(0,x2-x1) == expected
report = (ROOT / '4-DeepLearningFoundations/week12/7.0.retrospective.md').read_text()
assert all(value in report for value in ('0.7218','0.6949','0.8145','0.8340'))
assert manifest['qualityReview']['pendingPackages'] == []
print(json.dumps({'verified_pngs': png_count, 'existing_html': len(paths) - png_count,
                  'weekly_guides': weekly_count, 'archived_daily_cards': len(manifest['archive']),
                  'archived_replaced_originals': len(manifest.get('replacedOriginals', [])),
                  'pre_refinement_backups': len(manifest.get('refinementArchives', [])),
                  'links_and_examples': 'pass'}))
