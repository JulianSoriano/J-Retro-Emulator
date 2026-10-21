# User guide

A step-by-step guide to using J's Emulators. No technical knowledge needed.

## 1. Open the emulator

- **Online:** https://juliansoriano.github.io/J-Retro-Emulator/
- **Offline:** download `index.html` from this repository (right-click the "Raw" button and choose "Save link as"), then double-click the saved file. It opens in your browser and needs no internet.

Use a current version of Chrome, Edge, Firefox or Safari.

## 2. Load a game

You need a ROM file, which is a copy of a game you own (this project includes no games). Either:
- press **Open ROM** (top right) and pick the file, or
- **drag the file** onto the screen.

You can pick a `.zip` too; the emulator takes the game out of it. The console is chosen from the file ending:

| Console | File endings |
|---|---|
| NES | `.nes` `.unf` `.unif` |
| Super Nintendo | `.sfc` `.smc` `.fig` `.swc` |
| Game Boy | `.gb` |
| Game Boy Color | `.gbc` |
| Game Boy Advance | `.gba` `.agb` |
| Sega Genesis / Mega Drive | `.md` `.gen` `.bin` `.smd` |
| Sega Master System | `.sms` `.sg` |
| Sega Game Gear | `.gg` |

The first time you open a game for a console, that console's emulation engine starts up (a second or less).

## 3. The Library

Every game you open is remembered in the **Library** panel. Click one to play it again. The little cross removes a game from the list. The library lives in your browser only; no game is ever uploaded anywhere.

## 4. Playing

**Keyboard (defaults)**

| Action | Player 1 | Player 2 |
|---|---|---|
| D-pad | Arrow keys | I / J / K / L |
| Nintendo B / A / Y / X | Z / X / A / S | N / M / H / U |
| Nintendo L / R | Q / W | Y / O |
| Sega A / B / C | Z / X / C | B / N / M |
| Sega X / Y / Z | A / S / D | T / Y / U |
| Start | Enter | P |
| Select / Mode | Right Shift | T / O |

**Changing keys:** in the **Controls** panel, click a key and press the new one. Sega and Nintendo consoles keep separate layouts. **Defaults** puts them back.

**Gamepad:** plug one in and press any button. It is detected automatically. Buttons follow an Xbox-style layout.

**Touch screens:** on-screen buttons appear for phones and tablets.

**Other keys**

| Key | Does |
|---|---|
| **Esc** | Pause / resume |
| **Tab** (hold) | Fast forward |
| **F2** | Save state to the chosen slot |
| **F4** | Load state from the chosen slot |
| **F11** | Full screen |

**Picture filters (under the screen, next to Full screen)**

Three buttons sit right under the game, so you never have to scroll for them. A lit (gold) button is on.

- **Scanlines** (on by default): the thin dark lines of an old TV. Turn off for a clean picture.
- **Smooth:** softens the blocky pixels.
- **Voxel** (NES games only): shows the game as solid 3D. Characters and enemies stand up as tall blocks, the scenery is a gentle relief with soft shadows under the characters, and the status bar at the top stays flat. The view is fixed, looking almost straight at the screen, so it stays steady and sharp. Scanlines are hidden while it's on. It needs WebGL2 and is heavier on the graphics chip than the normal view; if the game stutters, turn it off. Save-state pictures stay flat.

**Genesis input:** for Genesis games a small panel on the right has "Six-button pads". Turn it off if an older Genesis game ignores your buttons.

Your choices are remembered by the browser.

## 5. Two kinds of saving

**Battery saves** are the game's own saving, like saving at a save point in Zelda. The emulator keeps these automatically every couple of seconds. Nothing to do.

**Save states** are a snapshot of the whole console at one moment, so you can save anywhere, even mid-fight, and come back to that exact spot.

1. Pick a slot (1 to 4) in the **Save states** panel.
2. Press **Save** (or **F2**). The slot shows a small picture and the time.
3. Later, press **Load** (or **F4**) to return to that moment.

Each game has its own 4 slots. A save made in one version of an emulation engine may not load in a different version.

## 6. Backing up and moving saves

Saves are stored inside your browser. They survive closing and reopening, but **clearing the browser's site data deletes them**, and a different browser or computer starts empty.

To back up a save state: **Save states, then Editor**, choose the slot, press **Download state**. To restore it: **Editor, then Import state**, then **Save to slot**.

## 7. The state editor (optional, advanced)

The editor lets you look inside a save state and change values, for example to set your lives to 9.

1. Open **Editor** and pick **Running game (now)** or a slot.
2. Use **Find a value**. Example: you have 3 lives. Search for **Equals 3**.
3. Close the editor, lose a life, and reopen it (your search is kept). Search **Equals 2** or **Went down**.
4. Repeat until only a few results remain, pick one, type a new value, and press **Write**.
5. Press **Load into game** to apply it, or **Save to slot** to keep it.

Changed bytes show in gold until applied, and **Undo changes** reverts them. Editing is safe: it works on a copy, so nothing changes until you load it.

## 8. Troubleshooting

| Problem | What to try |
|---|---|
| Nothing happens when I open a ROM | Check the file ending is in the table above. Some `.bin` files are not Genesis games. |
| No sound | Click the page once (browsers block sound until you interact), and check the speaker button and volume slider. |
| A Genesis game ignores buttons | Turn off "six-button pads". |
| Game runs slowly | Close other heavy tabs. Fast forward (Tab) should be off. If Voxel is on, turn it off. |
| The Voxel button is missing | It only appears for NES games. |
| My saves are gone | Browser site data was probably cleared, or you're in a different browser or a private window. Restore from a downloaded state. |
| "State from a different version" | That save was made with a different engine version and can't be loaded. |
