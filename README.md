# Pygame 2D RPG Project

## Project Structure
The project is organized as follows:

```
LICENSE
README.md
requirements.txt
TODO
audio/
    death.wav
    Fire.wav
    heal.wav
    hit.wav
    main.ogg
    sword.wav
    attack/
        claw.wav
        fireball.wav
        slash.wav
code/
    debug.py
    level.py
    main.py
    player.py
    settings.py
    support.py
    tile.py
    ui.py
    weapon.py
    __pycache__/
        debug.cpython-312.pyc
        ...
graphics/
    font/
        joystix.ttf
    Grass/
        grass_1.png
        ...
    monsters/
        bamboo/
        ...
    objects/
        0.png
        ...
    particles/
        aura/
        ...
    player/
        down/
        ...
map/
    map_Details.csv
    ...
pygame/
    lib64
    pyvenv.cfg
    ...
tiled/
    1map.tmx
    ...
```

This structure provides a clear separation of concerns, with directories for code, assets, and configuration files.

## Overview
This project is a 2D RPG game built using Pygame. Below is a detailed explanation of the various code files in the project, their purpose, and how they achieve their functionality.

## Code Files

### 1. `main.py`
This is the entry point of the game. It initializes the game, sets up the display, and runs the main game loop.
- **Initialization**: The `Game` class initializes Pygame, sets up the screen dimensions, and creates an instance of the `Level` class.
- **Main Loop**: The `run` method contains the game loop, which:
  - Handles events like quitting the game.
  - Updates the screen by filling it with a black background and calling the `run` method of the `Level` class.
  - Maintains a consistent frame rate using `pygame.time.Clock`.

### 2. `settings.py`
This file contains configuration settings for the game, such as screen dimensions, frame rate, and other constants. These settings are imported wherever needed to maintain consistency across the project.

### 3. `level.py`
This file manages the game level, including loading and updating game elements like the player, enemies, and environment.
- **Level Class**: Handles the creation and management of all game objects.
- **Game Logic**: Updates the state of the game, including player movement, interactions, and rendering of objects.

### 4. `player.py`
This file defines the player character, including its attributes, movement, and interactions.
- **Player Class**: Manages player-specific logic such as movement, animations, and actions.
- **Input Handling**: Processes user inputs to control the player.

### 5. `tile.py`
This file handles the tiles that make up the game environment.
- **Tile Class**: Represents individual tiles, including their position and appearance.
- **Rendering**: Draws tiles on the screen based on their properties.

### 6. `ui.py`
This file manages the user interface elements, such as health bars, inventory, and other HUD components.
- **UI Class**: Handles the rendering and updating of UI elements.

### 7. `weapon.py`
This file defines the weapons available in the game.
- **Weapon Class**: Manages weapon attributes, animations, and interactions.

### 8. `support.py`
This file contains utility functions that assist other parts of the project.
- **Helper Functions**: Includes reusable functions for tasks like loading assets, handling collisions, etc.

### 9. `debug.py`
This file provides debugging tools to help during development.
- **Debugging Utilities**: Includes functions to display debug information on the screen, such as FPS or object states.

## Additional Directories

### `audio/`
Contains sound effects and music used in the game.

### `graphics/`
Holds all graphical assets, including sprites, tiles, and fonts.

### `map/`
Includes map data files that define the layout of the game world.

### `tiled/`
Contains files related to the Tiled map editor, used for designing game levels.

## How It All Comes Together
The `main.py` file orchestrates the game by initializing the necessary components and running the main loop. The `Level` class in `level.py` acts as the central manager for game objects, while other files like `player.py`, `tile.py`, and `ui.py` handle specific aspects of the game. Assets from the `audio/` and `graphics/` directories are loaded and used to create an immersive experience.