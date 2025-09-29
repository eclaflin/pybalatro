# pybalatro
A Python-based, Balatro-inspired engine built as a learning project in OOP, data modeling, and game logic.

---

## Overview

pybalatro` is an educational project that recreates the core mechanics of the card game *Balatro* in Python.  

The focus is not on graphics or UI, but on:
- Practicing **object-oriented programming fundamentals**
- Designing **extensible, testable systems**
- Modeling **game state and scoring logic**
- Building out a project with **professional repo structure and documentation**

This project is not affiliated with, or endorsed by, the creators of *Balatro*. It is for learning and portfolio purposes only.  

---

## Features (Planned)
- Core card objects (Cards, Jokers, Consumables)
- Deck, hand, and discard mechanics
- Scoring engine that applies card and modifier logic
- CLI-based gameplay loop
- Unit test coverage for all major components
- Developer documentation (`docs/`) and devlog

---

## Project Structure

```
pybalatro/
├── pybalatro/ # Source code package
│ ├── init.py
│ ├── cards.py
│ ├── deck.py
│ ├── scoring_engine.py
│ └── ...
├── tests/ # Unit tests
│ └── test_cards.py
├── docs/ # Architecture notes, devlog, etc.
│ ├── architecture.md
│ └── devlog.md
├── README.md
├── LICENSE
├── pyproject.toml
└── requirements.txt
```

---

## Development Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/pybalatro.git
cd pybalatro
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

---

## Documentation

See [docs folder](docs/)


---

## License

This project is licensed under the MIT License – see the LICENSE file for details.

---

## Acknowledgements

Inspirede by the game *Balatro* by LocalThunk
