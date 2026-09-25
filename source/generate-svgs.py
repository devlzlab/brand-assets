#!/usr/bin/env python3
"""Rebuild the devlzlab daemon mark as editable SVG tiles."""
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
GRID = (
    '..m........m..',
    '..m........m..',
    '.w..........w.',
    'mw..........wm',
    'wwm........mww',
    'wwwm......mwww',
    '.wwwm....mwww.',
    '.wwwwm..mwwww.',
    '..wwwwwwwwww..',
    '....wwwwww....',
    '...w.wwww.w...',
    '....o.ww.o....',
    '...m..ww..m...',
    '....w.ww.w....',
    '....w.ww.w....',
    '......w.......',
    '......m.......',
)
assert len(GRID) == 17 and all(len(row) == 14 for row in GRID)

PITCH = 23
TILE = 20
X = (512 - 14 * PITCH) / 2
Y = (512 - 17 * PITCH) / 2
COLORS = {'w': '#f5f5f4', 'm': '#858585', 'o': '#ff5b20'}


def rect(col, row, color, *, outline=False, opacity=None):
    x, y = X + col * PITCH, Y + row * PITCH
    attrs = f'x="{x:g}" y="{y:g}" width="{TILE}" height="{TILE}"'
    if opacity is not None:
        attrs += f' opacity="{opacity:g}"'
    if outline:
        return f'<rect {attrs} fill="none" stroke="{color}" stroke-width="2.4"/>'
    return f'<rect {attrs} fill="{color}"/>'


def tiles(variant):
    parts = []
    for row, line in enumerate(GRID):
        for col, kind in enumerate(line):
            if kind == '.':
                continue
            if variant == 'fragment' and col >= 9 and row < 9 and (2 * col + row) % 5 in (0, 1):
                continue
            color = COLORS[kind]
            if variant == 'crt':
                dot = '#e7e7e5' if kind == 'w' else '#777777' if kind == 'm' else COLORS['o']
                for dy in range(4):
                    for dx in range(4):
                        cx = X + col * PITCH + 2.7 + dx * 4.9
                        cy = Y + row * PITCH + 2.7 + dy * 4.9
                        parts.append(f'<circle cx="{cx:g}" cy="{cy:g}" r="1.55" fill="{dot}"/>')
            else:
                parts.append(rect(col, row, color, outline=variant == 'outline', opacity=0.65 if kind == 'm' else None))
    if variant == 'fragment':
        fragments = (
            (12, 0, 'w'), (14, 2, 'm'), (13, 3, 'w'), (15, 4, 'w'),
            (14, 5, 'w'), (16, 6, 'm'), (13, 7, 'o'), (15, 8, 'w'),
            (12, 9, 'm'), (14, 10, 'w'), (11, 11, 'm'), (13, 12, 'w'),
        )
        for col, row, kind in fragments:
            parts.append(rect(col, row, COLORS[kind], opacity=0.7 if kind == 'm' else None))
    return '\n    '.join(parts)


def svg(title, variant='default', background=False):
    bg = '<rect x="16" y="16" width="480" height="480" rx="112" fill="#0b0b0c" stroke="#303033" stroke-width="2"/>\n    ' if background else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="{escape(title)}">
  <title>{escape(title)}</title>
  <desc>Pixel-grid daemon symbol reconstructed as editable vector squares.</desc>
  {bg}<g shape-rendering="crispEdges">
    {tiles(variant)}
  </g>
</svg>
'''


FAVICON_GRID = (
    '..w......w..',
    '.ww......ww.',
    'ww........ww',
    'wwm......mww',
    '.www....www.',
    '..wwwwwwww..',
    '...wwwwww...',
    '..wo.ww.ow..',
    '....wwww....',
    '..m..ww..m..',
    '.....ww.....',
    '......w.....',
)
assert len(FAVICON_GRID) == 12 and all(len(row) == 12 for row in FAVICON_GRID)


def favicon_svg():
    squares = []
    for row, line in enumerate(FAVICON_GRID):
        for col, kind in enumerate(line):
            if kind != '.':
                squares.append(f'<rect x="{col + 2}" y="{row + 2}" width="1" height="1" fill="{COLORS[kind]}"/>')
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" role="img" aria-label="devlzlab daemon favicon">\n  <title>devlzlab daemon favicon</title>\n  <rect width="16" height="16" rx="3" fill="#0b0b0c"/>\n  <g shape-rendering="crispEdges">\n    ' + '\n    '.join(squares) + '\n  </g>\n</svg>\n'


if __name__ == '__main__':
    files = {
        'logos/daemon/daemon.svg': svg('devlzlab daemon'),
        'logos/daemon/daemon-fragment.svg': svg('devlzlab daemon fragment', 'fragment'),
        'logos/daemon/daemon-crt.svg': svg('devlzlab daemon CRT', 'crt'),
        'logos/daemon/daemon-outline.svg': svg('devlzlab daemon outline', 'outline'),
        'icons/daemon.svg': svg('devlzlab daemon app icon', background=True),
        'icons/daemon-fragment.svg': svg('devlzlab daemon fragment app icon', 'fragment', background=True),
        'favicons/favicon.svg': favicon_svg(),
    }
    for relative, content in files.items():
        path = ROOT / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
