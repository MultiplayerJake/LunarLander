# Lunar Lander

A small arcade-style [Lunar Lander](https://en.wikipedia.org/wiki/Lunar_Lander_(video_game_genre)) game built with **Python** and **pygame**. Pilot your lander down onto a flat patch of randomly generated terrain — but watch your fuel, because you only get 10 seconds of burn per attempt.

## Demo — Watch it in action

https://github.com/user-attachments/assets/d06bd698-a88e-4bd8-8f28-101ffdbf8ada

## Features

- 🎮 Simple, twitch-friendly controls: thrust up, rotate left/right
- ⛽ Limited fuel — the gauge shifts from green to red as it runs low
- 🏔️ Randomly generated terrain on every round, so no two runs are the same
- 🎯 A flat landing target marked with an arrow
- 📊 End-of-round stats: **landing velocity**, **landing roll**, and **offset from target**
- 🔁 Crash and retry instantly — the loop never ends

## Requirements

- Python 3.x
- [pygame](https://pypi.org/project/pygame/) (the only external dependency — `math` and `random` are part of the Python standard library)

## Installation

Clone the repository and install pygame:

```bash
git clone https://github.com/MultiplayerJake/LunarLander.git
cd LunarLander
pip install pygame
```

> **Tip:** On some systems (especially macOS/Linux) you may need `pip3 install pygame` or `python3 -m pip install pygame` instead.

## How to run

The game loads its assets (images and font) using **relative paths**, so you must start it with `SpaceLanders/` as your current working directory.

**Windows (PowerShell / CMD)** — from the repo root:

```powershell
cd SpaceLanders
python main.py
```

**macOS / Linux** — from the repo root:

```bash
cd SpaceLanders
python3 main.py
```

A window titled **"Lander"** (800 × 400, 60 FPS) will open. Press **↑** to start.

## Controls

| Key | Action |
|-----|--------|
| `↑` (Up arrow) | Start / retry — and thrust upward while flying |
| `←` (Left arrow) | Rotate left |
| `→` (Right arrow) | Rotate right |

Thrusting and turning both consume fuel — you have **up to 10 seconds** of total burn (`MAX_FUEL = 10`) before you're coasting on fumes. Holding thrust and rotation together drains the tank faster.

## How to play

1. Press **↑** to launch.
2. Rotate with **←/→** and fire the main engine with **↑** to steer toward the flat landing zone (marked by an arrow on the terrain).
3. Touch down gently, roughly upright and close to the target. The steeper your impact, the worse your stats — and hard contact with the terrain is a crash.
4. After each round you'll see your **landing velocity**, **landing roll**, and **offset from target**. Press **↑** to retry with brand-new terrain.
## Project structure

```
LunarLander/
├── .gitignore
├── LICENSE
├── README.md
├── SpaceLanders/
    ├── main.py          # Game entry point (run this)
    └── assets/
        ├── lander.png
        ├── main_engine.png
        ├── rcs_left.png
        ├── rcs_right.png
        ├── rocket.png
        └── flat_pointer.png
```

## Running the tests

The test suite runs the real game headlessly (no window opens):

```bash
pip install pytest
python -m pytest Tests
```

`Tests/smoke_game.py` is a standalone end-to-end check that boots the game, plays a round, and quits cleanly:

```bash
python Tests/smoke_game.py
```

## License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for details.
