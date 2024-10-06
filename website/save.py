from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add a secret key for session management

# MySQL Connection Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dbms",
    database="health_data"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('detail.html')

@app.route('/save_details', methods=['POST'])
def save_details():
    try:
        # Print request form data for debugging
        print(request.form)

        # Get data from the form
        age = request.form['age']
        sex = request.form.get('sex') == '1'  # '1' for male, '0' for female
        diabetes = 'diabetes' in request.form  # Checkbox value handling
        famhistory = 'famhistory' in request.form
        smoking = 'smoking' in request.form
        obesity = 'obesity' in request.form
        alcohol = 'alcohol' in request.form
        exercise = request.form['exercise']
        diet = request.form['diet']
        heartproblem = 'heartproblem' in request.form
        bmi = request.form['bmi']
        physicalactivity = request.form['physicalactivity']
        sleep = request.form['sleep']
        bp1 = request.form['bp1']
        bp2 = request.form['bp2']

        # Get session email
        email = session.get('email')

        # Insert data into MySQL table
        insert_query = """
        INSERT INTO user_details 
        (age, sex, diabetes, famhistory, smoking, obesity, alcohol, exercise_hours, diet, heart_problem, bmi, physical_activity, sleep_hours, blood_pressure_systolic, blood_pressure_diastolic, email) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = (age, sex, diabetes, famhistory, smoking, obesity, alcohol, exercise, diet, heartproblem, bmi, physicalactivity, sleep, bp1, bp2, email)
        cursor.execute(insert_query, data)
        db.commit()

        return redirect(url_for('index'))

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return "An error occurred while processing your request.", 500  # HTTP status 500 for internal server error

if __name__ == '__main__':
    app.run(debug=True, port=6500)
