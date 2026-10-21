# How everything works

This page explains the project from the top down, first in plain words and then in more detail for anyone who wants to change it.

## The big picture

An **emulator** is a program that pretends to be an old game console. The game file (the ROM) is the cartridge, and the emulator is the console.

J's Emulators is a single web page. It does three jobs:

1. **Emulation:** it runs the real game code using an "emulation core", a small program that imitates one family of consoles.
2. **The shell:** everything around it: the screen, sound, buttons, game library, save slots and editor.
3. **Storage:** it keeps your games and saves inside your browser.

Everything happens on your own computer. The page never sends your games or saves anywhere.

## Parts

| Part | What it is | Where |
|---|---|---|
| The page | The whole interface and all the logic, written in HTML, CSS and JavaScript | `src/index.html` |
| Four emulation cores | The console imitators, compiled to WebAssembly (a fast browser format) | `src/cores/*.wasm` |
| The one-file build | The page with the four cores embedded inside it | `index.html` (generated) |
| Build script | Joins the page and the cores into the one file | `tools/build_single_file.py` |

### The four cores

| Core | Consoles |
|---|---|
| FCEUmm | NES |
| Snes9x 2010 | Super Nintendo |
| mGBA | Game Boy, Game Boy Color, Game Boy Advance |
| Genesis Plus GX | Genesis / Mega Drive, Master System, Game Gear |

They are existing open-source emulators (built in the "libretro" style), turned into WebAssembly so a browser can run them. Each has its own licence; see its own project.

## What happens when you open a game

1. **Read the file.** The page reads the ROM (and takes it out of a zip if needed).
2. **Pick the console.** The file ending decides it (for example `.gba` means Game Boy Advance). That decides which core to use.
3. **Start the core.** The page decodes that core from the text embedded in the page and starts it. Only one core is kept in memory at a time.
4. **Give it the game.** The ROM bytes are copied into the core's memory and the core is told to load them.
5. **Remember it.** The ROM goes into the Library (stored in your browser) so you can reopen it with one click.
6. **Run.** The main loop starts.

## The main loop

A browser calls the page about 60 times a second. Each time:

1. **Read the controls:** keyboard and gamepad state become a set of pressed buttons for each player.
2. **Run one frame:** the core runs the game for 1/60 of a second and produces a picture and some sound.
3. **Draw:** the picture is copied onto the screen canvas (with optional scanlines or smoothing).
4. **Play sound:** the audio goes into a small buffer that the speakers drain.

Speed is kept steady by watching that sound buffer. If it's running low the page runs an extra frame; if it's too full it waits. That keeps the game at the right speed and the sound from crackling. Fast forward simply runs 4 frames per step.

## The voxel view (NES)

An optional view that rebuilds the NES picture as solid 3D, using what the console itself knows about the scene. The idea comes from the voxel renderer in the open-source nesrecomp project (separating characters from scenery, standing them up as solid objects, keeping the status bar flat); the code here is our own.

- **Reading the console's data.** Each frame the page takes a save state and pulls out three things: the sprite list (OAM, up to 64 characters/objects with position and flip flags), the sprite size/table settings, and the picture tiles (CHR). Sprite pixels are rebuilt from the tiles, producing a mask the same size as the screen: "this pixel belongs to a sprite". If a game's tiles can't be read, it falls back to treating whatever differs from the colour around each sprite as the sprite.
- **Layers.** Scenery becomes a low stepped relief (brighter = slightly higher). Sprite pixels become tall solid blocks so characters and enemies stand out in front. Scenery just down-right of a sprite is darkened, which reads as a contact shadow.
- **Flat status bar.** Many games park an invisible "sprite 0" under the status bar to time the screen split. When it stays put for a few frames, everything above it is drawn flat.
- **Drawing.** The graphics chip draws one cube per pixel (about 57,000) in one instanced WebGL2 call, reading the picture and the mask as textures. Only the faces turned toward the camera are drawn.
- **Camera.** Fixed, almost straight on with a very slight lean. Blocks sit edge to edge with no gaps and the canvas is drawn at the screen's real pixel size with no smoothing, which keeps the picture crisp.
- The normal flat picture is still drawn behind the scenes every frame (the save-state thumbnails use it). The voxel view is a second canvas shown on top.

## Saving

There are two kinds, and both are stored in your browser's **IndexedDB** (a small database that belongs to the page's site).

**Battery saves (SRAM).** Many games have a small battery-backed memory. Every couple of seconds the page copies it out of the core and stores it if it changed. When you reopen the game it's put back.

**Save states.** The core can copy its entire memory and chip state into a block of bytes, and later restore it. That block is a save state. Pressing Save stores it with a screenshot as a "slot" record for that game. Loading hands the bytes back to the core.

Each game is identified by a fingerprint (hash) of its contents, so its saves follow the game and not the filename.

Stored databases: `roms` (your library), `states` (slots 1 to 4 per game) and `sram` (battery saves). Settings such as key layouts and volume are kept in the browser's `localStorage`.

If IndexedDB is not available (for example a private window), the emulator still works; it just can't remember things after you close the page.

## The save state editor

A save state is just bytes, so you can look at them and change them. The editor shows a hex view of a copy of the state. "Find a value" works like a cheat-search tool: you search for a number (your lives, say), change it in the game, and search again to narrow down which byte is the lives counter. Then you write a new value and load the edited copy back into the game. Because it edits a copy, nothing changes until you press **Load into game**.

Downloaded states are wrapped in a plain zip file so browsers will download them reliably.

## Controls

Each console family (Sega or Nintendo) has its own key map, kept separately. The page translates keys, gamepad buttons and touch buttons into the same set of button numbers the cores expect. Defaults are in the code (`DEFAULT_KEYS`) and your changes are saved in `localStorage`. Gamepads are read by button position in an Xbox-style layout.

## The one-file build

Browsers can't easily load extra files when a page is opened straight from your disk, so the release is one self-contained file.

`tools/build_single_file.py` does two things:

1. It changes the page's core loader so it first looks for an embedded copy of the core inside the page.
2. It appends each `.wasm` core to the end of the page as base64 text (a way of writing binary data as ordinary letters), which makes the file about a third bigger than the cores alone.

To rebuild after changing `src/index.html`:

```
python3 tools/build_single_file.py
```

This rewrites `index.html`. The build needs only Python 3.

> The page has a spare loader that fetches `name.wasm` from the same folder, and the original app also had a plain-JavaScript fallback for browsers that block WebAssembly. The one-file build leaves that fallback out to keep the file at about 13 MB; nearly all current browsers allow WebAssembly.

## GitHub Pages

GitHub Pages serves the repository as a website. Because the app is the single file `index.html` at the top of the repo, Pages can serve it as is. The `.nojekyll` file tells Pages not to process the files. To publish your own copy: **Settings, then Pages, then Deploy from a branch, branch `main`, folder `/ (root)`**.

## Limits and honest notes

- Checked with a built-in demo cartridge and with NES, Game Boy and Game Boy Advance games. Commercial SNES, Master System, Game Gear and Genesis games are untested.
- Nothing here is cycle-perfect hardware emulation; the cores are well-known and accurate enough for most games, but some games have quirks.
- N64, arcade and other systems are not supported.
- Save states are tied to the core version that made them.
- Fonts are loaded from Google Fonts when online; offline the page uses a standard font.

## Credits and legal

- Emulation cores: FCEUmm, Snes9x, mGBA and Genesis Plus GX, each under its own open-source licence.
- No games or BIOS files are included. Use ROMs you own.
