# Markov Chain Text Generator

This project implements a text generator using Markov Chains with a modern web interface built in Flask.

## What is a Markov Chain?

A Markov chain is a mathematical system that transitions from one state to another according to certain probabilistic rules. The defining characteristic of a Markov chain is that no matter how the process arrived at its present state, the possible future states are fixed and have set probabilities. 

In the context of text generation:
- The system reads a text and builds a model of word transitions.
- If the "N-gram size" (or Order) is 1, it looks at a single word and finds all the words that follow it in the training text.
- To generate text, it starts with a random word, picks the next word based on the possibilities seen in the training data, then uses *that* new word to pick the next one, and so on.
- Higher orders (e.g., 2 or 3) look at pairs or triplets of words to determine the next word, producing more coherent but less "random" output.

## Project Structure

- `app.py`: The Flask web server that serves the UI and handles text generation requests.
- `markov.py`: The core logic for the Markov Chain generator.
- `templates/index.html`: A beautiful, responsive web interface for interacting with the generator.
- `sample.txt`: A sample training text file about space exploration.

## How to Run

1. Make sure you have Python installed.
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. You can paste text directly into the text area or use the **"Load Text File"** button to load a file (like the included `sample.txt`).
2. Adjust the **N-gram Size (Order)**. An order of 1 creates very random text, while 2 or 3 creates text that sounds more like the original.
3. Adjust the **Output Length**.
4. Click **Generate Text** and see what it creates!
