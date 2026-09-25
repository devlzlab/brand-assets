# devlzlab brand assets

These PNG files preserve the original logo concept sheets.

| File | Content |
| --- | --- |
| [daemon-icon-grid.png](concepts/daemon-icon-grid.png) | Initial daemon icon concepts |
| [cyberpunk-icon-exploration-grid.png](concepts/cyberpunk-icon-exploration-grid.png) | Cyberpunk icon explorations |
| [cyberpunk-app-icon-grid.png](concepts/cyberpunk-app-icon-grid.png) | Refined app icon concepts |
| [daemon-platform-shadow-triptych.png](concepts/daemon-platform-shadow-triptych.png) | Daemon, platform, and shadow variations |
| [daemon-pixel-icon-specimen-sheet.png](concepts/daemon-pixel-icon-specimen-sheet.png) | Daemon pixel icon specimen sheet |

These are raster concept sheets, separate from the SVG assets below.

## SVG assets

The SVG files reconstruct the daemon symbol from the final PNG specimen sheet. They contain editable vector shapes and no embedded raster image.

- [Default mark](logos/daemon/daemon.svg)
- [Fragment mark](logos/daemon/daemon-fragment.svg)
- [CRT mark](logos/daemon/daemon-crt.svg)
- [Outline mark](logos/daemon/daemon-outline.svg)
- [Default app icon](icons/daemon.svg), with a dark rounded background
- [Fragment app icon](icons/daemon-fragment.svg), with the same dark rounded background
- [Favicon](favicons/favicon.svg), simplified for 16 × 16 pixels

The transparent marks use light tiles and are intended for dark backgrounds. Run `python3 source/generate-svgs.py` to regenerate the SVG files.
