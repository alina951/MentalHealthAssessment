from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    # Logic to start the quiz (this can be extended)
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        overall_mood = request.form.get('overall_mood')
        happiness_scale = request.form.get('happinessScale')

        # Process the quiz results (you can expand this logic)
        score = 0  # Dummy scoring logic
        recommendation = "Keep up the good work!"  # Dummy recommendation

        return render_template('result.html', score=score, recommendation=recommendation)

    return render_template('quiz.html')

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    try:
        overall_mood = request.form['overall_mood']
        happiness_scale = request.form['happinessScale']

        # Calculate score and recommendation based on inputs (dummy logic)
        score = int(happiness_scale)  # Example scoring
        recommendation = "Keep up the good work!"  # Example recommendation

        return render_template('result.html', score=score, recommendation=recommendation)
    except Exception as e:
        print("Error:", e)
        return "An error occurred while processing your request."

if __name__ == '__main__':
    app.run(debug=True)
