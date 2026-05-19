# Pokémon Directory Structure

This folder contains all Pokémon data for PS3D, organized by region and generation.

## File Organization

### Structure Overview
```
pokemon/
├── 3d_models/              # 3D model assets and textures
│   ├── models/            # 3D model files (.fbx, .obj, etc.)
│   ├── textures/          # Texture files (.png, .jpg, etc.)
│   └── animations/        # Animation files (.anim, etc.)
├── Kanto.json             # Complete Kanto region data (all 151 Pokémon)
├── 0001_bulbasaur.json    # Individual Pokémon data files
├── 0002_ivysaur.json
└── 0151_mew.json
```

## File Types

### Individual Pokémon Files (0001-0151)
Named format: `XXXX_pokemon_name.json`

Each file contains:
- **id**: Numeric ID
- **pokedex_number**: Zero-padded number (0001-0151)
- **name**: English name
- **type**: List of types (e.g., ["Grass", "Poison"])
- **base**: Base stats (HP, Attack, Defense, Sp. Attack, Sp. Defense, Speed)
- **forms**: Container for different forms:
  - **normal**: Standard form with model/texture/animation paths
  - **mega**: Mega Evolution variants (empty slots ready to fill)
  - **regional**: Regional variants like Alola, Galar, Paldea (empty slots)
  - **other**: Additional forms like gender differences, special forms
- **stats**: Duplicate of base stats for quick access
- **meta**: Additional metadata (height, weight, description)

### Kanto.json
Complete regional file containing all 151 original Pokémon with region and generation metadata.

### 3D Models Directory
Organized for easy asset management:
- **models/**: 3D geometry files (e.g., `0001_bulbasaur.fbx`)
- **textures/**: Texture maps (e.g., `0001_bulbasaur.png`)
- **animations/**: Animation data (e.g., `0001_bulbasaur.anim`)

## Naming Conventions

All files follow consistent naming:
- **Pokédex numbers**: Zero-padded 4 digits (0001-0151)
- **Pokémon names**: Lowercase, spaces replaced with underscores
- **Examples**:
  - 0001_bulbasaur.json
  - 0006_charizard.json
  - 0151_mew.json

## Navigation Guide

### Finding a Specific Pokémon
```
By number: pokemon/0001_bulbasaur.json
By name: pokemon/0XXX_pokemon_name.json
Combined: pokemon/Kanto.json (search for "english": "PokémonName")
```

### Adding Variants (Megas, Regionals, etc.)
Edit the individual Pokémon file and populate the relevant form object:

```json
"forms": {
  "normal": { ... },
  "mega": {
    "mega_x": {
      "name": "Mega Charizard X",
      "types": ["Fire", "Dragon"],
      "stats": { ... },
      "model_path": "3d_models/models/0006_charizard_mega_x.fbx"
    }
  },
  "regional": {
    "alola": {
      "name": "Alolan Charizard",
      "types": ["Fire", "Dragon"],
      "stats": { ... }
    }
  }
}
```

### Adding 3D Assets
Place files in `pokemon/3d_models/` following the structure:
- Models: `pokemon/3d_models/models/XXXX_pokemon_name.fbx`
- Textures: `pokemon/3d_models/textures/XXXX_pokemon_name.png`
- Animations: `pokemon/3d_models/animations/XXXX_pokemon_name.anim`

## Battle Gimmicks in PS3D

PS3D introduces several battle mechanics and systems:

### Current Gimmicks

#### 1. Type System
- 18 types with specific advantages and disadvantages
- Dual-type Pokémon supported
- Type matchups affect damage calculation

#### 2. Stat-Based Battling
- Six stats: HP, Attack, Defense, Sp. Attack, Sp. Defense, Speed
- Speed determines turn order
- Stats determine effectiveness in battle

#### 3. Form Variations
- **Normal Forms**: Base Pokémon appearance
- **Mega Evolution**: Temporary stat boosts during battle (Gen VI+)
- **Regional Variants**: Pokémon adapted to specific regions
- **Other Forms**: Gender differences, seasonal forms, etc.

#### 4. 3D Battle Visualization
- Real-time 3D models for all Pokémon
- Animated attacks and interactions
- Dynamic camera angles during battles

### Planned/Future Gimmicks
- Ability system (individual Pokémon capabilities)
- Held items and item interactions
- Status conditions (burn, poison, paralysis, etc.)
- Move physics and real-time collision detection
- Environmental effects in 3D arenas
- Multiplayer battle system

---

## Quick Start

### Creating Pokémon Data
1. Use `python3 generate_kanto.py` to regenerate Kanto.json from pokedex.json
2. Use `python3 split_kanto.py` to create individual Pokémon files from Kanto.json

### Modifying a Pokémon
1. Edit the individual JSON file: `pokemon/XXXX_name.json`
2. Changes apply immediately to that Pokémon

### Adding a New Region
1. Create a new Python script similar to `generate_kanto.py`
2. Filter pokedex.json for the desired generation
3. Generate region files (e.g., Johto.json, Hoenn.json)

## File Statistics

- **Kanto Region**: 151 Pokémon
- **Individual Files**: 151 JSON files
- **Total Entries**: 152 files (including Kanto.json)

---

For questions or updates to this structure, refer to the parent README.md file.
