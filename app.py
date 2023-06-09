from flask import Flask, request, jsonify, render_template
import testing_tweets as tt
import math

app = Flask(__name__)

def process_input(input_text):

    # Process the input text and generate the output text
    risk_factor = tt.main(input_text, 50)
    output_text = f'@{input_text}\'s risk factor: {risk_factor}'
    
    # Return the output text as a JSON response
    return math.floor(risk_factor * 1000) / 10

@app.route('/', methods=['GET', 'POST'])
def index():
    output = None
    if request.method == 'POST':
        user_input = request.form['user_input']
        output = process_input(user_input)
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run()