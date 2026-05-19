#!/usr/bin/env python3
"""
Generate Kanto.json from pokedex.json
Extracts the original 151 Pokémon and creates a structured JSON file
with slots for mega forms and additional data.
"""

import json
import sys

def generate_kanto():
    try:
        # Read the original pokedex
        with open('pokedex.json', 'r', encoding='utf-8') as f:
            all_pokemon = json.load(f)
        
        # Filter to first 151 (Kanto region)
        kanto_pokemon = [p for p in all_pokemon if p['id'] <= 151]
        
        # Create enhanced structure with spaces for mega forms and variants
        kanto_data = {
            "region": "Kanto",
            "generation": 1,
            "total_pokemon": len(kanto_pokemon),
            "pokemon": []
        }
        
        for pokemon in kanto_pokemon:
            pokemon_entry = {
                "id": pokemon['id'],
                "pokedex_number": f"{pokemon['id']:04d}",
                "name": pokemon['name'],
                "type": pokemon['type'],
                "base": pokemon['base'],
                "forms": {
                    "normal": {
                        "model_path": f"3d_models/models/{pokemon['id']:04d}_{pokemon['name']['english'].lower().replace(' ', '_')}.fbx",
                        "texture_path": f"3d_models/textures/{pokemon['id']:04d}_{pokemon['name']['english'].lower().replace(' ', '_')}.png",
                        "animation_path": f"3d_models/animations/{pokemon['id']:04d}_{pokemon['name']['english'].lower().replace(' ', '_')}.anim"
                    },
                    "mega": {},
                    "regional": {},
                    "other": {}
                },
                "stats": pokemon['base'],
                "meta": {
                    "height": None,
                    "weight": None,
                    "description": None
                }
            }
            kanto_data["pokemon"].append(pokemon_entry)
        
        # Write to Kanto.json
        with open('pokemon/Kanto.json', 'w', encoding='utf-8') as f:
            json.dump(kanto_data, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Successfully generated Kanto.json with {len(kanto_pokemon)} Pokémon")
        print(f"✓ File saved to: pokemon/Kanto.json")
        print(f"\nStructure includes:")
        print(f"  - Pokédex numbers (0001-0151)")
        print(f"  - Base stats from original pokedex")
        print(f"  - Placeholder paths for:")
        print(f"    • 3D models")
        print(f"    • Textures")
        print(f"    • Animations")
        print(f"  - Empty slots for:")
        print(f"    • Mega forms")
        print(f"    • Regional variants")
        print(f"    • Other forms")
        
        return True
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return False
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    success = generate_kanto()
    sys.exit(0 if success else 1)
