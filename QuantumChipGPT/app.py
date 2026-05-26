from flask import Flask, render_template, request
from qiskit import QuantumCircuit
from transformers import pipeline

import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

# ==========================================
# LOAD GPT-2 MODEL
# ==========================================

generator = pipeline(
    "text-generation",
    model="gpt2"
)

# ==========================================
# HOME ROUTE
# ==========================================

@app.route("/", methods=["GET", "POST"])
def home():

    image = None

    if request.method == "POST":

        # ==========================================
        # GET USER PROMPT
        # ==========================================

        user_prompt = request.form["prompt"]

        # ==========================================
        # GPT-2 PROCESSING
        # ==========================================

        ai_response = generator(
            user_prompt,
            max_new_tokens=20,
            num_return_sequences=1,
            pad_token_id=50256
        )

        print(ai_response)

        # ==========================================
        # AI-BASED QUANTUM CIRCUIT LOGIC
        # ==========================================

        if "space" in user_prompt.lower():

            data = {
                "qubits": 4,
                "gates": [
                    ["h", 0],
                    ["cx", 0, 1],
                    ["cx", 1, 2],
                    ["cx", 2, 3]
                ]
            }

        elif "encryption" in user_prompt.lower():

            data = {
                "qubits": 4,
                "gates": [
                    ["h", 0],
                    ["cx", 0, 1],
                    ["cx", 1, 2],
                    ["cx", 2, 3]
                ]
            }

        elif "neural" in user_prompt.lower():

            data = {
                "qubits": 6,
                "gates": [
                    ["h", 0],
                    ["h", 1],
                    ["cx", 0, 2],
                    ["cx", 1, 3],
                    ["cx", 2, 4],
                    ["cx", 3, 5]
                ]
            }

        else:

            data = {
                "qubits": 4,
                "gates": [
                    ["h", 0],
                    ["cx", 0, 1],
                    ["cx", 1, 2],
                    ["cx", 2, 3]
                ]
            }

        # ==========================================
        # CREATE QUANTUM CIRCUIT
        # ==========================================

        qubits = data["qubits"]
        gates = data["gates"]

        qc = QuantumCircuit(qubits)

        for gate in gates:

            if gate[0] == "h":
                qc.h(gate[1])

            elif gate[0] == "x":
                qc.x(gate[1])

            elif gate[0] == "cx":
                qc.cx(gate[1], gate[2])

        # ==========================================
        # REALISTIC QUANTUM CHIP LAYOUT
        # ==========================================

        plt.figure(figsize=(14, 8))

        ax = plt.gca()

        # BACKGROUND
        ax.set_facecolor("#f2f2f2")

        # REMOVE AXES
        plt.axis("off")

        # ==========================================
        # QUBIT PAD POSITIONS
        # ==========================================

        qubit_positions = {
            0: (-6, 0),
            1: (0, 4),
            2: (0, -4),
            3: (6, 0)
        }

        # ==========================================
        # DRAW QUBIT PADS
        # ==========================================

        for q, (x, y) in qubit_positions.items():

            # OUTER PAD
            rect1 = plt.Rectangle(
                (x - 0.7, y - 0.7),
                1.4,
                1.4,
                color="#9e9e9e"
            )

            ax.add_patch(rect1)

            # INNER PAD
            rect2 = plt.Rectangle(
                (x - 0.35, y - 0.35),
                0.7,
                0.7,
                color="#4fc3f7"
            )

            ax.add_patch(rect2)

            # LABEL
            plt.text(
                x,
                y - 1.2,
                f"Q{q}",
                ha="center",
                fontsize=14,
                color="black",
                fontweight="bold"
            )

        # ==========================================
        # DRAW WAVEGUIDE CONNECTIONS
        # ==========================================

        # HORIZONTAL RESONATOR
        x = np.linspace(-5.2, 5.2, 1000)

        y = 0.4 * np.sin(6 * x)

        plt.plot(
            x,
            y,
            color="#5c5c5c",
            linewidth=3
        )

        # SECOND RESONATOR
        y2 = -0.4 * np.sin(6 * x)

        plt.plot(
            x,
            y2,
            color="#5c5c5c",
            linewidth=3
        )

        # VERTICAL CONNECTION TOP
        y3 = np.linspace(0.7, 3.3, 500)

        x3 = 0.4 * np.sin(6 * y3)

        plt.plot(
            x3,
            y3,
            color="#5c5c5c",
            linewidth=3
        )

        # VERTICAL CONNECTION BOTTOM
        y4 = np.linspace(-3.3, -0.7, 500)

        x4 = 0.4 * np.sin(6 * y4)

        plt.plot(
            x4,
            y4,
            color="#5c5c5c",
            linewidth=3
        )

        # ==========================================
        # TITLE
        # ==========================================

        plt.title(
            "Superconducting Quantum Chip Layout",
            fontsize=22,
            fontweight="bold",
            color="#222222",
            pad=20
        )

        # ==========================================
        # SAVE IMAGE
        # ==========================================

        image = "static/chip.png"

        plt.savefig(
            image,
            bbox_inches="tight",
            dpi=300,
            facecolor="#f2f2f2"
        )

        plt.close()

        # ==========================================
        # RETURN OUTPUT
        # ==========================================

        return render_template(
            "index.html",
            image=image
        )

    return render_template("index.html")

# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)