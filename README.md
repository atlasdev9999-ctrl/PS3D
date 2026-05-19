# 🟢 Pokémon Foundations (PF)
> **The Core Engine Backbone:** Powered by PS3D (Pokémon Software 3D)

Welcome to the official repository for **Pokémon Foundations**, the absolute bedrock for modern 3D game development. This project serves as a spiritual successor to *Pokémon Essentials* and *Pokémon Studio*, providing a high-fidelity desktop creator workspace for PC developers.

---

## 🧬 Identity & Mascot Concept
*   **The Official Mascot:** Zygarde (The Order Pokémon).
*   **The Philosophy:** Just as Zygarde is made of individual cells that assemble into perfect forms, this engine functions identically—streaming individual data blocks and code assets to assemble a high-fidelity 3D game.
*   **The Visual Theme:** Strict Default Dark Mode (`#121212` canvas) accented by high-contrast Zygarde Neon Green (`#39FF14`) for active selections and UI highlights.

---

## ⚙️ 7 Core Features
1. **3D World & Map Builder:** Supports full-proportion free-camera *Sword & Shield* 3D layouts or locked-grid *BDSP*-style chibi setups, equipped with terrain sculpting and auto-colliders.
2. **Advanced Database Manager:** Automated public JSON Pokédex importing, multi-language inline translation matrices, and automated NPC trainer squad cloner/difficulty level-scalers.
3. **Dual-Combat Paradigm Toggle:** A global master switch allowing creators to choose between **System A (Turn-Based)** tactical stadium combat or **System B (Real-Time Action-RPG)** seamless overworld combat.
4. **Visual Event & Dialogue Editor:** A node-based, flowchart-style connecting canvas (similar to Unreal Engine Blueprints) to script complex cutscenes and trainer behaviors without code.
5. **Quest & Objective Tracker:** Step-by-step checklist goals for players with dropdown reward matrices to distribute money, items, or gift Pokémon.
6. **GitHub Repository Streamer:** Keeps the initial editor download tiny by storing heavy assets on GitHub. On first boot, an animation of Zygarde cells assembling tracks data streaming.
7. **One-Click Multi-Platform Compiler:** Exports separate, fully optimized player applications for Windows (`.exe`), Mac, Linux, and Android (`.apk`).

---

## 🗂️ Repository Architecture & Branches
To safeguard project assets and ensure community fairness, code files are organized under strict version-control rules:

*   `dev`: Active sandbox branch for coding schemas, database definitions, and framework logic.
*   `main`: Locked, production-ready release branch that the desktop app pulls from.
*   `releases`: Read-only snapshot versions so downstream updates do not break ongoing user projects.

### Active Directories (Under `/dev`)
*   `/pokemon` — Core unified JSON schema templates for Pokémon data structures.
*   `/moves` — Dual-combat Move data engine schemas (Turn-based + Real-time logic).
*   `/items` — Item database declarations.

---

## ⚖️ Legal License
This project is licensed under the **GNU General Public License v3.0 (GNU GPLv3)**.

### Why this license is used:
*   **Forces Transparency:** Anyone who forks or alters this engine is legally required to keep their improvements public and completely free under the exact same license.
*   **Blocks Bad Actors:** Completely blocks entities from making a profit, selling this code, or hiding engine enhancements behind a paywall.
*   **Liability Shield:** Provides a strict "No Warranty" clause that protects project contributors from corporate platform liabilities.
