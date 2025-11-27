
# UniversalConverter - A3 Complete Project

This repository contains a complete, polished refactoring project for the A3 assignment:
- `codigo-original/` : intentionally messy legacy code (for "before")
- `codigo-refatorado/` : cleaned, well-structured package using Strategy/Factory patterns
- `Relatorio_A3_detalhado.pdf` : full report (in project root)
- `Apresentacao_speaker_notes.md` : suggestion of what each member should say (in root)
- `tests/` : extensive pytest suite

## Features
- Temperature, Length, and Weight conversions
- Canonical base units used internally (Kelvin, Meter, Kilogram)
- Clear separation of responsibilities
- CLI and optional Flask web endpoint
- Comprehensive unit tests

## How to run locally
1. (Optional) create a virtualenv:
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate    # Windows

2. Install dependencies:
   pip install -r codigo-refatorado/requirements.txt

3. Run tests:
   pytest -q codigo-refatorado/tests

4. Run CLI:
   python codigo-refatorado/run_converter.py 100 c f

5. (Optional) Run Flask app:
   export FLASK_APP=codigo-refatorado/universal_converter/webapp.py
   python -m flask run
