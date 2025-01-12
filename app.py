from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling CGPA calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Fetch data from the form
        grades = request.form.getlist('grades')
        credits = request.form.getlist('credits')

        # Convert inputs to numeric values
        grades = list(map(float, grades))
        credits = list(map(float, credits))

        # Calculate total grade points and total credits
        total_grade_points = sum(grade * credit for grade, credit in zip(grades, credits))
        total_credits = sum(credits)

        # Compute CGPA
        cgpa = total_grade_points / total_credits if total_credits > 0 else 0

        return render_template('index.html', cgpa=round(cgpa, 2))
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)