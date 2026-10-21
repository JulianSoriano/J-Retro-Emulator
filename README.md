# J-Retro-Emulator

An all-in-one retro emulator for Nintendo and Sega consoles and handhelds that runs in your web browser. It is a single web page with everything built in, so there is nothing to install and no account to make.

**Play it online:** https://juliansoriano.github.io/J-Retro-Emulator/

## Documentation

- **[User guide](docs/USER_GUIDE.md):** how to load games, controls, save states, backups and the state editor, with troubleshooting
- **[How it works](docs/HOW_IT_WORKS.md):** what is inside, how a game runs, how saving works and how the one-file build is made

## Quick start

1. Open the link above (or download `index.html` and double-click it to use it offline).
2. Press **Open ROM** or drag a game file onto the screen.
3. Play. **F2** saves a state, **F4** loads it. Hold **Tab** to fast forward.

## Supported systems

| Brand | Systems | ROM file types |
|---|---|---|
| Nintendo | NES | `.nes` `.unf` `.unif` |
| Nintendo | Super Nintendo (SNES) | `.sfc` `.smc` `.fig` `.swc` |
| Nintendo | Game Boy | `.gb` |
| Nintendo | Game Boy Color | `.gbc` |
| Nintendo | Game Boy Advance | `.gba` `.agb` |
| Sega | Genesis / Mega Drive | `.md` `.gen` `.bin` `.smd` |
| Sega | Master System | `.sms` `.sg` |
| Sega | Game Gear | `.gg` |

ROMs can also be loaded straight from a `.zip`.

Emulation cores (compiled to WebAssembly): FCEUmm (NES), Snes9x (SNES), mGBA (Game Boy, Game Boy Color, Game Boy Advance) and Genesis Plus GX (Genesis, Master System, Game Gear).

## Features

- Game library that remembers the games you have opened
- Save states per game: **F2** saves, **F4** loads, with a slot picker and a state editor
- Battery saves (SRAM) kept between sessions
- Keyboard controls with a remappable layout (Sega and Nintendo layouts are kept separately) and gamepad support
- Two-player keyboard defaults
- Fast forward (hold **Tab**), pause (**Esc**), fullscreen (**F11**) and a volume control
- Drag and drop a ROM onto the screen to play
- Picture filters right under the screen, beside Full screen: scanlines (on by default), smooth, and an optional **voxel** view for NES games that gives every pixel depth as a lit 3D block

Your library, settings and save states are kept in your browser, on your computer. Nothing is uploaded anywhere.

## Ways to run it

**On GitHub Pages (easiest):** open the link above, then drag a ROM onto the page or press **Open ROM**.

**Offline:** download [`index.html`](https://github.com/JulianSoriano/J-Retro-Emulator/raw/main/index.html) (13 MB; right-click the link and choose "Save link as"), then double-click the saved file. All four emulation cores are built into the file, so it works without internet.

**Hosting your own copy with GitHub Pages:** in your repository go to **Settings, then Pages**, choose **Deploy from a branch**, pick the `main` branch and the `/ (root)` folder, and save. The page appears at `https://<your-username>.github.io/<repository-name>/` after a minute or two.

## Saves and backups

- Save states, battery saves, your game library and settings live in the browser you used, on that site (the online page and a saved offline copy each keep their own). Different browsers keep separate libraries.
- Clearing the browser's site data deletes them. Use the state editor's **Download state** to back up important saves, and **Import state** to bring them back.

## Controls (defaults)

| Action | Player 1 | Player 2 |
|---|---|---|
| D-pad | Arrow keys | I / J / K / L |
| Nintendo B / A / Y / X | Z / X / A / S | N / M / H / U |
| Nintendo L / R | Q / W | Y / O |
| Sega A / B / C | Z / X / C | B / N / M |
| Sega X / Y / Z | A / S / D | T / Y / U |
| Start | Enter | P |
| Select / Mode | Right Shift | T / O |

All keys can be changed in the app's controls panel.

## Other keys

| Key | Does |
|---|---|
| **F2** / **F4** | Save / load state |
| **Tab** (hold) | Fast forward |
| **Esc** | Pause |
| **F11** | Fullscreen |

## Your games

No games are included. Use ROMs from cartridges you own. Dumping your own cartridges is the usual way to get them.

## Known limits

- Checked with the built-in demo cartridge and with NES, Game Boy and Game Boy Advance ROMs loaded through the app. Commercial SNES, Master System, Game Gear and Genesis games have **not** been tested yet.
- Needs a modern browser with WebAssembly (all current versions of Chrome, Edge, Firefox and Safari).
- The page asks Google Fonts for its fonts when you're online. Offline, it uses a standard font.

## Project layout

| Path | What it is |
|---|---|
| `index.html` | The finished one-file emulator (generated, this is what Pages serves) |
| `src/index.html` | The readable app source |
| `src/cores/` | The four emulation cores (WebAssembly) |
| `tools/build_single_file.py` | Builds `index.html` from `src/` |
| `docs/` | User guide and how-it-works |

To rebuild after editing the source: `python3 tools/build_single_file.py`

## Built with

WebAssembly builds of libretro emulation cores (FCEUmm, Snes9x, mGBA and Genesis Plus GX). See each core's own project for its license.
