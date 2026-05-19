#!/usr/bin/env python3
"""
Generate Mega Evolution files for Pokémon that have them
Creates new JSON files for each Mega variant
"""

import json
import os

MEGA_EVOLUTION_DATABASE = {
    3: ["mega"],          # Venusaur
    6: ["mega_x", "mega_y"], # Charizard
    9: ["mega"],          # Blastoise
    15: ["mega"],         # Beedrill
    18: ["mega"],         # Pidgeot
    26: ["mega_x", "mega_y"], # Raichu
    36: ["mega"],         # Clefable
    65: ["mega"],         # Alakazam
    71: ["mega"],         # Victreebel
    80: ["mega"],         # Slowbro
    94: ["mega"],         # Gengar
    115: ["mega"],        # Kangaskhan
    121: ["mega"],        # Starmie
    127: ["mega"],        # Pinsir
    130: ["mega"],        # Gyarados
    142: ["mega"],        # Aerodactyl
    149: ["mega"],        # Dragonite
    150: ["mega_x", "mega_y"] # Mewtwo
}

# Pokemon name mapping
POKEMON_NAMES = {
    3: "venusaur",
    6: "charizard",
    9: "blastoise",
    15: "beedrill",
    18: "pidgeot",
    26: "raichu",
    36: "clefable",
    65: "alakazam",
    71: "victreebel",
    80: "slowbro",
    94: "gengar",
    115: "kangaskhan",
    121: "starmie",
    127: "pinsir",
    130: "gyarados",
    142: "aerodactyl",
    149: "dragonite",
    150: "mewtwo"
}

def create_mega_files():
    created_count = 0
    
    for pokemon_id, mega_forms in MEGA_EVOLUTION_DATABASE.items():
        # Read the base Pokemon file
        base_filename = f"pokemon/{pokemon_id:04d}_{POKEMON_NAMES[pokemon_id]}.json"
        
        if not os.path.exists(base_filename):
            print(f"✗ Base file not found: {base_filename}")
            continue
        
        with open(base_filename, 'r', encoding='utf-8') as f:
            base_pokemon = json.load(f)
        
        # Create Mega variant files
        for mega_form in mega_forms:
            if mega_form == "mega":
                filename = f"pokemon/{pokemon_id:04d}_mega_{POKEMON_NAMES[pokemon_id]}.json"
                name_suffix = " Mega"
            elif mega_form == "mega_x":
                filename = f"pokemon/{pokemon_id:04d}_mega_{POKEMON_NAMES[pokemon_id]}_x.json"
                name_suffix = " Mega X"
            elif mega_form == "mega_y":
                filename = f"pokemon/{pokemon_id:04d}_mega_{POKEMON_NAMES[pokemon_id]}_y.json"
                name_suffix = " Mega Y"
            
            # Create Mega variant structure
            mega_pokemon = {
                "id": pokemon_id,
                "pokedex_number": f"{pokemon_id:04d}",
                "name": {
                    "english": base_pokemon["name"]["english"] + name_suffix
                },
                "type": base_pokemon["type"],  # Placeholder, user will update
                "base": base_pokemon["base"],  # Placeholder, user will update
                "forms": {
                    "normal": base_pokemon["forms"]["normal"],
                    "mega": {},
                    "regional": {},
                    "other": {}
                },
                "stats": base_pokemon["stats"],  # Placeholder, user will update
                "meta": {
                    "height": None,
                    "weight": None,
                    "description": None,
                    "is_mega_evolution": True,
                    "mega_variant": mega_form
                }
            }
            
            # Write Mega file
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(mega_pokemon, f, indent=2, ensure_ascii=False)
            
            print(f"✓ Created: {filename}")
            created_count += 1
    
    print(f"\n✓ Successfully created {created_count} Mega Evolution files")
    print("\nFiles created:")
    print("  Venusaur: 0003_mega_venusaur.json")
    print("  Charizard: 0006_mega_charizard_x.json, 0006_mega_charizard_y.json")
    print("  Blastoise: 0009_mega_blastoise.json")
    print("  Beedrill: 0015_mega_beedrill.json")
    print("  Pidgeot: 0018_mega_pidgeot.json")
    print("  Raichu: 0026_mega_raichu_x.json, 0026_mega_raichu_y.json")
    print("  Clefable: 0036_mega_clefable.json")
    print("  Alakazam: 0065_mega_alakazam.json")
    print("  Victreebel: 0071_mega_victreebel.json")
    print("  Slowbro: 0080_mega_slowbro.json")
    print("  Gengar: 0094_mega_gengar.json")
    print("  Kangaskhan: 0115_mega_kangaskhan.json")
    print("  Starmie: 0121_mega_starmie.json")
    print("  Pinsir: 0127_mega_pinsir.json")
    print("  Gyarados: 0130_mega_gyarados.json")
    print("  Aerodactyl: 0142_mega_aerodactyl.json")
    print("  Dragonite: 0149_mega_dragonite.json")
    print("  Mewtwo: 0150_mega_mewtwo_x.json, 0150_mega_mewtwo_y.json")

if __name__ == "__main__":
    create_mega_files()
