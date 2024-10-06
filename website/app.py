from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import subprocess
import os
import numpy as np
from appwrite.client import Client
from appwrite.services.account import Account
from appwrite.services.databases import Databases
from appwrite.id import ID

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Initialize the Appwrite client
client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')  # Replace with your Appwrite endpoint
client.set_project('667f8c85002229461ca8')  # Project ID
client.set_key('[YOUR_API_KEY]')  # Replace with your API key

@app.route('/')
def index():
    if 'email' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        data = request.json
        username = data['username']
        email = data['email']
        nickname = data['nickname']
        password = data['password']

        # Initialize Appwrite Account service
        account = Account(client)
        databases = Databases(client)

        try:
            # Create user account
            user = account.create(
                user_id=ID.unique(),
                email=email,
                password=password,
                name=username
            )

            # Save user data in the database
            databases.create_document(
                database_id='667f8d010031471a488a',
                collection_id='667f8d16003418fd93a2',
                document_id=ID.unique(),
                data={
                    'email': email,
                    'name': username,
                    'nickname': nickname,
                    'password': password,
                }
            )
            return jsonify({"message": "User registered successfully"}), 200
        except Exception as e:
            return jsonify({"message": str(e)}), 400

    return render_template('signup.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        password = data.get('password')

        print(f"Received login request with email: {email}")

        if not email or not password:
            return jsonify({"success": False, "message": "Email and password are required"}), 400

        databases = Databases(client)

        try:
            # List all documents in the collection
            result = databases.list_documents(
                database_id='667f8d010031471a488a',
                collection_id='667f8d16003418fd93a2'
            )

            print(f"Documents found: {result['documents']}")

            # Check if any document matches the email
            user = None
            for document in result['documents']:
                if document['email'] == email:
                    user = document
                    break

            if user is None:
                print(f"Email '{email}' not found in documents.")
                return jsonify({"success": False, "message": "Email not found"}), 404

            # Check if the password matches
            if user['password'] == password:
                # Store the email in session upon successful login
                session['email'] = email
                print(f"Login successful for email: {email}")
                return redirect(url_for('index'))  # Redirect to index.html after login
            else:
                print(f"Password incorrect for email: {email}")
                return jsonify({"success": False, "message": "Incorrect password"}), 401

        except Exception as e:
            print(f"Exception occurred: {str(e)}")
            return jsonify({"success": False, "message": str(e)}), 400

    return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear the session
    session.pop('email', None)
    return redirect(url_for('signup'))

@app.route('/home')
def home():
    if 'email' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))

@app.route('/start', methods=['POST'])
def start_script():
    if request.method == 'POST':
        subprocess.Popen(['python', 'merge.py'])
        return 'Script started successfully'
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])  # Allow both GET and POST requests
def show_results():
    if request.method == 'POST':
        # Handle form submission if needed
        pass

    # Determine if an additional graph exists
    additional_graph_exists = os.path.exists("final_graph.png")

    # Read BPM data from the file
    bpm_data = []
    with open("bpm_values.txt", "r") as file:
        for line in file:
            bpm = float(line.strip())
            bpm_data.append(bpm)

    # Calculate average BPM between 5 to 20 seconds
    average_bpm = np.mean(bpm_data[5:])

    return render_template('results.html', additional_graph_exists=additional_graph_exists, average_bpm=average_bpm)

if __name__ == '__main__':
    app.run(debug=True)
