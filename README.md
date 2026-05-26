**"Team details:**
Team Name- Team AIQ
---
Team Lead- P.Pavani
---
Team Members -
| M.Priyanka |
| srinija |
| Charishma |
| Sravani sai |

# QuantumChipGPT

**AI-Powered Quantum Chip Architecture Generator**

QuantumChipGPT is a Flask web application that combines a GPT-2 language model with Qiskit to generate visual superconducting quantum chip layouts based on natural language prompts.

---

## Features

- Natural language input to describe a desired quantum chip architecture
- GPT-2 processes the prompt to guide circuit generation
- Qiskit builds the corresponding quantum circuit
- Matplotlib renders a realistic superconducting chip layout diagram
- Clean, futuristic web UI served via Flask

---

## Tech Stack

| Layer | Technology |
|---|---|
| Web Framework | Flask |
| Language Model | GPT-2 (via Hugging Face Transformers) |
| Quantum Circuit | Qiskit |
| Visualization | Matplotlib |
| Numerics | NumPy |

---

## Project Structure

```
.
├── app.py            # Flask backend — GPT-2 inference, circuit logic, chip rendering
├── index.html        # Jinja2 frontend template
├── requirements.txt  # Python dependencies
└── static/
    └── chip.png      # Generated chip image (created at runtime)
```

> **Note:** Place `index.html` inside a `templates/` folder for Flask to locate it correctly.

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/quantumchipgpt.git
cd quantumchipgpt
```

**2. Create and activate a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Create the static folder**

```bash
mkdir static
```

**5. Move the template**

```bash
mkdir templates
mv index.html templates/
```

---

## Running the App

```bash
python app.py
```

Then open your browser and go to: `http://127.0.0.1:5000`

---

## Usage

1. Type a description of your desired quantum chip architecture into the text box.
2. Click **Generate Quantum Chip**.
3. The app generates a quantum circuit and renders a superconducting chip layout image.

### Supported Prompt Keywords

| Keyword in prompt | Circuit generated |
|---|---|
| `space` | 4-qubit linear entanglement chain |
| `encryption` | 4-qubit linear entanglement chain |
| `neural` | 6-qubit parallel entanglement network |
| *(anything else)* | 4-qubit default entanglement chain |

**Example prompts:**
- `Design a space communication quantum chip`
- `Create an encryption-optimized quantum architecture`
- `Build a neural quantum processing unit`

---

## Requirements

```
numpy
flask
qiskit
transformers
torch
matplotlib
networkx
```

> GPT-2 weights (~500 MB) are downloaded automatically on first run via Hugging Face.

---

## Notes

- The first launch may take a minute as GPT-2 downloads its model weights.
- The `static/chip.png` file is overwritten on each generation.
- This project is a demonstration and does not run circuits on real quantum hardware.

---

## License

MIT License — free to use, modify, and distribute.
