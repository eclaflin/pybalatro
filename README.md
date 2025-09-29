# pybalatro

A Python-based, Balatro-inspired engine built as a learning project in OOP, data modeling, and game logic.

---

## Overview

`pybalatro` is an educational project that recreates the core mechanics of the card game *Balatro* in Python.  

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
│ └── ...
├── tests/ # Unit tests
├── docs/ # Architecture notes, devlog, etc.
├── .gitignore
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

# AI Mentorship Logs

The `ai-mentorship/` [folder](docs/ai-mentorship/) contains summarized logs of guided discussions with an AI mentor during the development of `pybalatro`.  

The goal of these sessions was **mentorship and architectural guidance**, not automatic code generation. All code in this project was written by me; the AI assisted only with **boilerplate, scaffolding, and documentation suggestions**.  

These logs are included to demonstrate the **design thinking process**, show how key decisions were made, and provide transparency about the tools used to enhance learning and maintain structured development.

---

## License

This project is licensed under the MIT License – see the LICENSE file for details.

---

## Acknowledgements

Inspirede by the game *Balatro* by LocalThunk
