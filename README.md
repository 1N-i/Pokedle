# 🎮 Pokédle

![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)
![API](https://img.shields.io/badge/API-PokeAPI-red?style=for-the-badge)

A Python-based command-line game where you guess the secret Pokémon based on stats and attributes using real-time data from the [PokéAPI](https://pokeapi.co/).

## 📋 Summary
- [Technologies](#-technologies)
- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [How to Play](#-how-to-play)
- [Future Improvements](#-future-improvements)
- [How to Run](#-how-to-run)

---

## 🛠 Technologies
- **Python 3.x**: Core game logic and execution.
- **Requests Library**: For handling HTTP communication with the API.
- **JSON**: For parsing Pokémon data structures.

## ✨ Features
- **Dynamic Filtering:** Choose which generations (1 through 9) you want to include in the pool.
- **Smart Feedback System:** - **Text Attributes:** Checks for exact matches (Types, Color).
  - **Numeric Stats:** Tells you if the secret value is higher (↑) or lower (↓) than your guess.
- **Live Data:** Fetches up-to-date Pokémon info (BST, Height, Weight, Generation) directly from the API.
- **Replayability:** Game loop allows for continuous play without restarting the script.

## 📂 Project Architecture
The project is organized into specific modules:
* `main.py`: The entry point. Contains the game loop, user input handling, and the comparison logic (checking if guesses are correct, higher, or lower).
* `search.py`: The "engine" of the project. Handles API requests, translates generation numbers, and creates the structured data dictionary for the game.

## 🎮 How to Play
1. Run the script.
2. Select the generations you want to guess from (e.g., `1, 2, 3` or `9`).
3. Type the name or the pokedex number of a Pokémon.
4. The game will compare your guess with the secret Pokémon:
   - `✓` : Correct match.
   - `X` : Incorrect match.
   - `↑` : The secret value is higher.
   - `↓` : The secret value is lower.
5. Keep guessing until you find the secret Pokémon!

## 🔮 Future Improvements
* [ ] "Give Up" option to reveal the answer.
* [ ] Add a hint system that gives the pokedex entry after some tries.

## 🚀 How to Run

- **Clone the repository:**
Use the command below to clone the project and enter its folder:

```bash 
pip install requests
