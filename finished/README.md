# Pixel Runner

A 2D side-scrolling runner game built with Python and Pygame, based on the [Clear Code Pygame tutorial](https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=6912s&ab_channel=ClearCode).

## Gameplay

Run endlessly while dodging obstacles to rack up the highest score you can.

- **Obstacles:** Ground-level snails and mid-air flies spawn from the right and move left
- **Scoring:** +1 point for every second you survive
- **Game over:** Colliding with any obstacle ends the run; press Space/Enter to restart

## Controls

| Key              | Action     |
| ---------------- | ---------- |
| Space / Enter    | Jump       |
| Space / Enter    | Start game / Restart after game over |

## Running the Game

```bash
pip install pygame
python main.py
```

Requires Python 3.x.

## Project Structure

```
Pygame Runner/
├── main.py                         # Main game (active version)
├── graphics/
│   ├── Sky.png                     # Background sky
│   ├── ground.png                  # Ground surface
│   ├── player/                     # Player sprites (walk, jump, stand)
│   ├── fly/                        # Fly obstacle sprites (2 frames)
│   └── snail/                      # Snail obstacle sprites (2 frames)
├── audio/
│   ├── music.wav                   # Background music loop
│   └── jump.wav                    # Jump sound effect
├── font/
│   └── Pixeltype.ttf               # Pixel-style UI font
└── finished/
    ├── runner_class only.py        # Cleaned-up class-based version
    └── runner_video.py             # Full tutorial reference with comments
```

## How It Works

### Architecture

The game uses Pygame's sprite system with two main classes:

- **Player** (`pygame.sprite.Sprite`) — handles input, gravity physics, jump mechanics, and walk/jump animation cycling
- **Obstacle** (`pygame.sprite.Sprite`) — handles leftward movement, 2-frame animation, and self-destruction when off-screen

Collisions are detected via `pygame.sprite.spritecollide()` between the player and obstacle sprite groups.

### Game Loop

1. **Event processing** — quit handling, jump input, obstacle spawning (every 900ms)
2. **Update** — apply gravity, move obstacles, animate sprites, check collisions
3. **Render** — draw sky/ground background, sprites, and score text
4. **Intro screen** — shown before first game and after each game over, displays title, instructions, and last score

### Key Constants

| Parameter        | Value          |
| ---------------- | -------------- |
| Resolution       | 800 x 400     |
| FPS              | 60             |
| Gravity          | +1 per frame   |
| Jump force       | -20            |
| Obstacle speed   | 6 px/frame     |
| Spawn interval   | 900ms          |
| Snail y-position | 300            |
| Fly y-position   | 210            |

## Versions

| File | Description |
| ---- | ----------- |
| `main.py` | Active version — minimal and beginner-friendly |
| `finished/runner_class only.py` | Cleaner class-based structure with better organization |
| `finished/runner_video.py` | Comprehensive tutorial reference with commented-out procedural alternatives |

All three versions are functionally equivalent.
