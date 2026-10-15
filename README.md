# J-Retro-Emulator

An all-in-one retro emulator for Nintendo and Sega consoles and handhelds, packaged as a single Linux AppImage. It runs completely offline. There is nothing to install and no account to make.

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

Your library, settings and saves are stored in `~/.config/js-emulators`.

## Download and run

1. Download [`JsEmulators-x86_64.AppImage`](https://github.com/JulianSoriano/J-Retro-Emulator/raw/main/dist/JsEmulators-x86_64.AppImage) (87 MB). It lives in the [`dist/`](dist/) folder of this repo.
2. Make it executable, then run it:

   ```bash
   chmod +x JsEmulators-x86_64.AppImage
   ./JsEmulators-x86_64.AppImage
   ```

   Or right-click the file, open **Properties → Permissions** and turn on **Allow executing file as program**, then double-click it.

> **Why the `chmod`?** Browsers can't mark downloads as executable. Until you do, a Linux file manager may offer to open the AppImage with a disk-image tool (for example GNOME Disks asking to "Restore Disk Image"). Cancel that and use one of the options above instead. Never restore it to a drive.

Requires a 64-bit (x86_64) Linux system. On some distributions you also need FUSE 2 (`sudo dnf install fuse` on Fedora, `sudo apt install libfuse2` on Debian or Ubuntu). If you'd rather not install it, run the AppImage with `--appimage-extract-and-run`.

### Verify the download (optional)

```
347c42bdb824c5ceca8d84042bb8ea864868804b860f04141984b874fbceee2c  JsEmulators-x86_64.AppImage
```

Check it with `sha256sum JsEmulators-x86_64.AppImage`, or compare with [`dist/SHA256SUMS`](dist/SHA256SUMS).

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
| **Ctrl+R** | Reload the app |

## Your games

No games are included. Use ROMs from cartridges you own. Dumping your own cartridges is the usual way to get them.

## Known limits

- Checked with the built-in demo cartridge and with Game Boy and Game Boy Advance ROMs loaded through the app. Commercial SNES, Master System, Game Gear, Game Boy and Game Boy Advance games have **not** been tested yet.
- x86_64 Linux only. It has been run on a virtual display, so please report anything odd on a real desktop (Fedora is the main target).

## Built with

[Electron](https://www.electronjs.org/) for the desktop window and WebAssembly builds of libretro emulation cores. See each core's own project for its license.
