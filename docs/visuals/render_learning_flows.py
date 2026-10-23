"""Render deterministic lesson diagrams from their editable specifications.

Run from the repository root with its Python environment. Sources and lesson
specifications live alongside this script. Existing PNGs are not overwritten
unless --refresh explicitly regenerates this renderer's own diagram targets.
"""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
FONT = '/System/Library/Fonts/Supplemental/Arial Unicode.ttf'
W, H = 2400, 1500
INK, MUTED = '#132D4F', '#405876'
COLORS = ['#1669B2', '#087F8C', '#7453AB', '#BD781B', '#236B69']
TINTS = ['#EDF5FE', '#EAF8F7', '#F3EFFB', '#FFF6E8', '#EDF7F3']


def font(size):
    return ImageFont.truetype(FONT, size)


def wrap(draw, text, size, width):
    lines = []
    for paragraph in text.split('\n'):
        line = ''
        for word in paragraph.split():
            trial = (line + ' ' + word).strip()
            if draw.textlength(trial, font=font(size)) > width and line:
                lines.append(line)
                line = word
            else:
                line = trial
        lines.append(line)
    return lines


def textbox(draw, box, text, size=34, color=INK, align='left', minimum=25):
    x, y, width, height = box
    while size >= minimum:
        lines = wrap(draw, text, size, width)
        step = round(size * 1.35)
        if len(lines) * step <= height and all(draw.textlength(s, font=font(size)) <= width for s in lines):
            break
        size -= 1
    else:
        raise ValueError(f'Text does not fit: {text}')
    for line in lines:
        xx = x + (width - draw.textlength(line, font=font(size))) / 2 if align == 'center' else x
        draw.text((xx, y), line, font=font(size), fill=color)
        y += step
    return size


def arrow(draw, x1, y, x2, color):
    draw.line((x1, y, x2 - 13, y), fill=color, width=6)
    draw.polygon([(x2, y), (x2 - 17, y - 11), (x2 - 17, y + 11)], fill=color)


def render(item, check_only=False, refresh=False):
    if not check_only:
        return {'output': item['output'], 'status': 'retired_use_render_weekly_guides'}
    target = Path(item['output']).resolve()
    if ROOT not in target.parents:
        raise ValueError('Output outside canonical repository')
    if target.exists() and not check_only and not refresh:
        return {'output': str(target), 'status': 'existing_not_overwritten'}
    im = Image.new('RGB', (W, H), '#FFFFFF')
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, W, 15), fill=COLORS[0])
    label = f"WEEK {item['week']:02d}  /  {item.get('kind', 'Day').upper()} {item.get('day_label', item['day'])}"
    textbox(dr, (85, 52, 2200, 55), label, 31, COLORS[0])
    textbox(dr, (85, 115, 2210, 155), item['title'], 65, minimum=43)
    textbox(dr, (85, 270, 2200, 50), 'THE MAIN FLOW', 29, MUTED)
    flow = item['flow']
    gap = 48
    width = (2230 - gap * (len(flow) - 1)) / len(flow)
    for i, entry in enumerate(flow):
        name, detail = entry.split('|', 1)
        x, y = 85 + i * (width + gap), 340
        dr.rounded_rectangle((x, y, x + width, y + 265), 22, fill=TINTS[i % 5], outline='#CDDCEB', width=2)
        dr.ellipse((x + 22, y + 20, x + 74, y + 72), fill=COLORS[i % 5])
        textbox(dr, (x + 22, y + 24, 52, 45), str(i + 1), 30, '#FFFFFF', 'center')
        textbox(dr, (x + 24, y + 95, width - 48, 82), name, 37, minimum=27)
        textbox(dr, (x + 24, y + 183, width - 48, 65), detail, 27, MUTED, minimum=24)
        if i < len(flow) - 1:
            arrow(dr, x + width + 7, y + 132, x + width + gap - 8, COLORS[0])
    dr.rounded_rectangle((85, 638, 2315, 747), 20, fill='#132D4F')
    textbox(dr, (115, 659, 2170, 74), item['example'], 35, '#FFFFFF', 'center', 28)
    for i, spec in enumerate(item['panels']):
        heading, *lines = spec.split('|')
        x, y, width = 85 + i * 760, 793, 710
        dr.rounded_rectangle((x, y, x + width, 1250), 22, fill=TINTS[i], outline='#D8E3EE', width=2)
        dr.rectangle((x + 28, y + 29, x + 36, y + 80), fill=COLORS[i])
        textbox(dr, (x + 55, y + 28, width - 88, 93), heading, 37, minimum=28)
        available = 300 / max(1, len(lines))
        for j, line in enumerate(lines):
            yy = y + 128 + j * available
            dr.ellipse((x + 29, yy + 13, x + 39, yy + 23), fill=COLORS[i])
            textbox(dr, (x + 55, yy, width - 89, available - 9), line, 31, minimum=25)
    dr.line((85, 1296, 2315, 1296), fill='#D9E3EF', width=2)
    textbox(dr, (85, 1320, 2200, 85), item['takeaway'], 33, INK, 'center', 26)
    textbox(dr, (85, 1435, 2200, 42), 'LEARNING OVERVIEW  •  Read alongside the lesson  •  Examples are illustrative unless stated', 24, MUTED, 'center', 23)
    if check_only:
        return {'output': str(target), 'status': 'layout_validated'}
    target.parent.mkdir(parents=True, exist_ok=True)
    im.save(target, 'PNG', optimize=True)
    return {'output': str(target), 'status': 'rendered', 'size': [W, H]}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--week', type=int)
    parser.add_argument('--check-layout', action='store_true')
    parser.add_argument('--refresh', action='store_true', help='Regenerate only code-authored diagrams listed in specs')
    args = parser.parse_args()
    items = json.loads(Path(__file__).with_name('learning-flow-specs.json').read_text())
    for item in items:
        if args.week is None or item['week'] == args.week:
            print(json.dumps(render(item, args.check_layout, args.refresh)))
