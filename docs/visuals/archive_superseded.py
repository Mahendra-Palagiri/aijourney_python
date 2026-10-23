"""Recoverably relocate only the explicitly listed, untracked batch PNGs."""
import hashlib
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
ARCHIVE=ROOT/'docs/visuals/archive/text-card-batch'
plan=json.loads(Path(__file__).with_name('archive_plan.json').read_text())
tracked=set(subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0'))
checks=[]
for item in plan:
    src=Path(item['source']).resolve();dst=Path(item['destination']).resolve()
    assert ROOT in src.parents and ARCHIVE in dst.parents
    assert src.name.endswith('.Learning_Flow.png') and src.is_file()
    assert str(src.relative_to(ROOT)) not in tracked, f'Refusing to move tracked original: {src}'
    assert not dst.exists(), f'Archive target already exists: {dst}'
    checks.append((src,dst,hashlib.sha256(src.read_bytes()).hexdigest()))
for src,dst,sha in checks:
    dst.parent.mkdir(parents=True,exist_ok=True)
    src.rename(dst)
    assert hashlib.sha256(dst.read_bytes()).hexdigest()==sha
print(json.dumps([{'source':str(src),'destination':str(dst),'sha256':sha} for src,dst,sha in checks]))
