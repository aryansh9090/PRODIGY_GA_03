from flask import Flask, render_template, request, jsonify
from markov import MarkovChain

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    text = data.get('text', '')
    length = int(data.get('length', 50))
    order = int(data.get('order', 3))

    if not text.strip():
        return jsonify({'error': 'Please provide some training text.'})

    markov = MarkovChain(order=order)
    markov.train(text)
    
    generated_text = markov.generate(length=length)
    
    if not generated_text:
        return jsonify({'error': 'Not enough text to generate output with the specified order.'})

    return jsonify({'result': generated_text})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
