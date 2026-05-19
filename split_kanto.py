#!/usr/bin/env python3
"""
Split Kanto.json into individual Pokémon files
Creates one JSON file per Pokémon (0001_bulbasaur.json through 0151_mew.json)
"""

import json
import sys

def split_kanto():
    try:
        # Read Kanto.json
        with open('pokemon/Kanto.json', 'r', encoding='utf-8') as f:
            kanto_data = json.load(f)
        
        pokemon_list = kanto_data['pokemon']
        
        for pokemon in pokemon_list:
            pokedex_num = pokemon['pokedex_number']
            pokemon_name = pokemon['name']['english'].lower().replace(' ', '_')
            filename = f"pokemon/{pokedex_num}_{pokemon_name}.json"
            
            # Write individual Pokemon file
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(pokemon, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Successfully created {len(pokemon_list)} individual Pokémon files")
        print(f"✓ Files created in: pokemon/")
        print(f"✓ Naming format: pokemon/XXXX_pokemon_name.json")
        print(f"\nExamples:")
        print(f"  - pokemon/0001_bulbasaur.json")
        print(f"  - pokemon/0002_ivysaur.json")
        print(f"  - pokemon/0151_mew.json")
        
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
    success = split_kanto()
    sys.exit(0 if success else 1)
